"""Evaluate one submission of one instance, ProgramBench style.

Pipeline (same steps and step names as upstream programbench.eval.eval):

  wipe_workspace -> extract submission -> remove_hashed_files -> clear_stale_executable
  -> compile (network blocked) -> hash_executable
  for every active test branch, in a fresh copy of the post-compile workspace:
      copy branch tar in -> restore_executable -> verify_executable_hash
      -> clean_stale_results -> run_tests (eval/run.sh) -> results_read (eval/results.xml)

Two backends:
  * local  (default): runs on the host in temp directories; needs bash, python3 + pytest and
           whatever toolchain compile.sh uses. Network is cut with `unshare -rn` when possible.
  * docker: runs every step in the instance image (programbench/<id>:task_cleanroom_v6, built
           from images/<id>/task_cleanroom) with `--network none` for compile.

A test passes only if it is reported as passed in the JUnit XML. Tests listed in tests.json
but missing from the XML are recorded as failures (never silently skipped); tests in the XML
that tests.json does not list are reported as warnings and not scored.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import tarfile
import tempfile
import time
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from programbench.constants import (
    BRANCH_TIMEOUT,
    CLEANROOM_TAG,
    COMPILE_TIMEOUT,
    DOCKER_EXECUTABLE,
    WORKSPACE_DIR,
)
from programbench.exceptions import EvalStepError
from programbench.utils.anti_cheat import references_to_reference, remove_hashed_files, sha256, structure_report
from programbench.utils.blob_store import get_blob_dir
from programbench.utils.internet_control import no_network_prefix
from programbench.utils.load_data import get_active_branches, get_ignored_tests


def extract_submission(src: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dest, symlinks=True, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git"))
    elif src.name.endswith(".zip"):
        with zipfile.ZipFile(src) as z:
            z.extractall(dest)
            for info in z.infolist():  # zipfile drops the exec bit
                mode = info.external_attr >> 16
                if mode:
                    (dest / info.filename).chmod(mode & 0o7777)
    else:
        with tarfile.open(src) as t:
            t.extractall(dest, filter="tar") if hasattr(tarfile, "data_filter") else t.extractall(dest)
    entries = [p for p in dest.iterdir()]
    if len(entries) == 1 and entries[0].is_dir() and not (dest / "compile.sh").exists():
        inner = entries[0]  # archive with a single top-level folder
        for p in inner.iterdir():
            p.rename(dest / p.name)
        inner.rmdir()


def parse_junit(xml_text: str, branch: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    out = []
    for case in root.iter("testcase"):
        name = ".".join(x for x in (case.get("classname", ""), case.get("name", "")) if x)
        status, extra = "passed", {"time": float(case.get("time") or 0)}
        for child in case:
            if child.tag in ("failure", "error", "skipped"):
                status = {"failure": "failure", "error": "error", "skipped": "skipped"}[child.tag]
                extra["message"] = (child.get("message") or "")[:2000]
                extra["text"] = (child.text or "")[:8000]
                break
        out.append({"name": name, "branch": branch, "status": status, "extra": extra})
    return out


class Evaluator:
    def __init__(self, instance: dict, submission: Path, *, backend: str = "local", image_tag: str = CLEANROOM_TAG,
                 keep_workdir: bool = False, prebuilt: Path | None = None):
        self.inst = instance
        self.iid = instance["instance_id"]
        self.submission = submission
        self.backend = backend
        self.image = f"{instance['image_name']}:{image_tag}"
        self.keep = keep_workdir
        self.prebuilt = prebuilt  # test an already-built binary (gold checks); skips compile + anti-cheat
        self.clean_hashes = set(instance.get("eval_clean_hashes") or [])
        self.result: dict = {"test_results": [], "error_code": None, "error_details": None, "log": [],
                             "solution_branch": "submission", "test_branches": get_active_branches(instance),
                             "test_branch_errors": {}, "executable_hash": None, "warnings": [], "structure": None,
                             "verifier": None}

    # ---------------------------------------------------------------- helpers
    def _step(self, name: str, cmd: list[str] | str, cwd: Path, *, timeout: int = 600, network: bool = True,
              accept_failure: bool = False, branch: str | None = None) -> subprocess.CompletedProcess:
        argv = ["bash", "-c", cmd] if isinstance(cmd, str) else cmd
        if self.backend == "docker":
            argv = [DOCKER_EXECUTABLE, "run", "--rm", "--init", *(["--network", "none"] if not network else []),
                    "-v", f"{cwd}:{WORKSPACE_DIR}", "-w", WORKSPACE_DIR, self.image, *argv]
        elif not network:
            argv = [*no_network_prefix(), *argv]
        t = time.time()
        try:
            r = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout)
        except subprocess.TimeoutExpired as e:
            self._log(name, argv, time.time() - t, (e.stdout or b"") + (e.stderr or b""), -1, branch)
            raise EvalStepError(f"{name}_timeout", f"{name} exceeded {timeout}s")
        self._log(name, argv, time.time() - t, r.stdout + r.stderr, r.returncode, branch)
        if r.returncode != 0 and not accept_failure:
            raise EvalStepError(f"{name}_failed", (r.stderr or r.stdout).decode(errors="replace")[-3000:])
        return r

    def _log(self, step, argv, wall, output, rc, branch=None):
        entry = {"step": step, "command": " ".join(argv[-3:]) if isinstance(argv, list) else argv,
                 "wall_time": round(wall, 3), "output": output.decode(errors="replace")[-20000:], "returncode": rc,
                 "exception_info": ""}
        if branch:
            entry["branch"] = branch
        self.result["log"].append(entry)

    def _inject_not_run(self, branch: str, code: str) -> None:
        for name in self.inst["branches"][branch]["tests"]:
            self.result["test_results"].append(
                {"name": name, "branch": branch, "status": "not_run", "extra": {"message": code}})

    # ---------------------------------------------------------------- pipeline
    def _compile(self, ws: Path) -> bytes:
        extract_submission(self.submission, ws)
        self.result["structure"] = structure_report(ws)
        removed = remove_hashed_files(ws, self.clean_hashes)
        self._log("remove_hashed_files", ["internal"], 0, ("\n".join(removed)).encode(), 0)
        if (ws / "executable").exists() or (ws / "executable").is_symlink():
            (ws / "executable").unlink()
            self.result["warnings"].append("submission shipped ./executable; removed before compiling")
        if not (ws / "compile.sh").exists():
            raise EvalStepError("no_compile_script", "compile.sh not found at submission root")
        self._step("compile", "chmod +x ./compile.sh && ./compile.sh", ws, timeout=COMPILE_TIMEOUT, network=False)
        exe = ws / "executable"
        if not exe.exists():
            raise EvalStepError("no_executable", "compile.sh did not produce ./executable")
        h = sha256(exe.resolve())
        self.result["executable_hash"] = h
        self._log("hash_executable", ["sha256sum", "./executable"], 0, h.encode(), 0)
        if h in self.clean_hashes:
            raise EvalStepError("reference_executable", "./executable is the reference binary")
        hits = references_to_reference(ws, self.clean_hashes)
        if hits:
            raise EvalStepError("reference_wrapper", "submission refers to the reference binary: " + "; ".join(hits[:3]))
        data = exe.resolve().read_bytes()
        exe.unlink()  # stashed; restored per branch like upstream
        return data

    def _run_branch(self, ws: Path, exe_bytes: bytes, branch: str, work: Path) -> None:
        bws = work / f"branch-{branch}"
        shutil.copytree(ws, bws, symlinks=True)
        blob_dir = get_blob_dir(self.iid)
        tar = blob_dir / "tests" / f"{branch}.tar.gz" if blob_dir else None
        if not tar or not tar.exists():
            raise EvalStepError("missing_test_blob", f"no test archive for branch {branch}")
        with tarfile.open(tar) as t:
            t.extractall(bws, filter="tar") if hasattr(tarfile, "data_filter") else t.extractall(bws)
        exe = bws / "executable"
        exe.write_bytes(exe_bytes)
        exe.chmod(0o755)
        if sha256(exe) != self.result["executable_hash"]:
            raise EvalStepError("executable_hash_mismatch", "restored executable differs")
        (bws / "eval" / "results.xml").unlink(missing_ok=True)
        self._step("run_tests", "chmod +x ./eval/run.sh && ./eval/run.sh", bws, timeout=BRANCH_TIMEOUT,
                   accept_failure=True, branch=branch)
        xml = bws / "eval" / "results.xml"
        if not xml.exists():
            raise EvalStepError("results_missing", "eval/results.xml was not produced")
        got = {r["name"]: r for r in parse_junit(xml.read_text(), branch)}
        expected = self.inst["branches"][branch]["tests"]
        for name in expected:
            self.result["test_results"].append(got.get(name) or {
                "name": name, "branch": branch, "status": "failure", "extra": {"message": "test missing from JUnit XML"}})
        extra = set(got) - set(expected)
        if extra:
            self.result["warnings"].append(f"Branch {branch}: {len(extra)} test(s) in JUnit XML not in tests.json")
        if not self.keep:
            shutil.rmtree(bws, ignore_errors=True)

    def run(self) -> dict:
        work = Path(tempfile.mkdtemp(prefix=f"programbench-{self.iid}-"))
        ws = work / "workspace"
        try:
            try:
                if self.prebuilt:
                    ws.mkdir(parents=True)
                    exe_bytes = self.prebuilt.read_bytes()
                    self.result["executable_hash"] = sha256(self.prebuilt)
                    self.result["solution_branch"] = "prebuilt"
                else:
                    exe_bytes = self._compile(ws)
            except EvalStepError as e:
                self.result["error_code"], self.result["error_details"] = e.error_code, e.error_details
                for b in self.result["test_branches"]:
                    self._inject_not_run(b, e.error_code)
                return self.result
            r = self._step("verifier_versions", "python3 -c 'import sys, pytest; print(pytest.__version__, sys.version.split()[0])'",
                           ws, accept_failure=True)
            parts = r.stdout.decode().split()
            self.result["verifier"] = {"pytest": parts[0], "python": parts[1]} if len(parts) == 2 else None
            for b in self.result["test_branches"]:
                try:
                    self._run_branch(ws, exe_bytes, b, work)
                except EvalStepError as e:
                    self.result["test_branch_errors"][b] = {"error_code": e.error_code, "error_details": e.error_details}
                    self._inject_not_run(b, e.error_code)
            return self.result
        finally:
            if not self.keep:
                shutil.rmtree(work, ignore_errors=True)


def score(result: dict, inst: dict) -> tuple[int, int]:
    """(passed, total) over non-ignored tests: flat and unweighted, like upstream."""
    ignored = get_ignored_tests(inst)
    rel = [t for t in result["test_results"] if f"{t['branch']}/{t['name']}" not in ignored]
    return sum(t["status"] == "passed" for t in rel), len(rel)


def write_result(result: dict, out: Path) -> None:
    out.write_text(json.dumps(result, indent=1))
