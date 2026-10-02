"""Shared runner for the gnuplot behavioural tests (stdlib only).

Each test runs ./executable (the workspace root, i.e. /workspace/executable)
once inside a fresh temporary directory with LC_ALL=C.UTF-8 and HOME set to
that directory, and compares stdout, stderr, exit status and any checked files
byte for byte with the golden output recorded from the reference gnuplot 5.4.9.
"""
import base64
import difflib
import json
import os
import subprocess
import tempfile
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXECUTABLE = Path(os.environ.get("PROGRAMBENCH_EXECUTABLE", HERE.parent.parent / "executable")).resolve()
TIMEOUT = float(os.environ.get("PROGRAMBENCH_CASE_TIMEOUT", "10"))


def _dec(d):
    if d is None:
        return None
    return base64.b64decode(d["b64"]) if "b64" in d else d["text"].encode()


@lru_cache(maxsize=None)
def _golden(category):
    return {c["id"]: c for c in json.loads((HERE / "golden" / f"{category}.json").read_text(encoding="utf-8"))}


def _diff(label, want, got):
    a = want.decode(errors="replace").splitlines(keepends=True)
    b = got.decode(errors="replace").splitlines(keepends=True)
    lines = list(difflib.unified_diff(a, b, f"expected {label}", f"actual {label}", n=1))
    return "".join(lines[:60])


def check(case_id):
    case = _golden(case_id.split(".")[0])[case_id]
    exp = case["expected"]
    with tempfile.TemporaryDirectory(prefix="gp-case-") as d:
        for name, content in case["files"].items():
            p = Path(d) / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(_dec(content))
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "HOME": d, "TMPDIR": d}
        r = subprocess.run([str(EXECUTABLE), *case["argv"]], cwd=d, input=_dec(case["stdin"]),
                           capture_output=True, timeout=TIMEOUT, env=env)
        got_files = {}
        for name in case["check_files"]:
            p = Path(d) / name
            got_files[name] = p.read_bytes() if p.exists() else None
    problems = []
    if r.returncode != exp["exit_code"]:
        problems.append(f"exit status: expected {exp['exit_code']}, got {r.returncode}")
    for stream, got in (("stdout", r.stdout), ("stderr", r.stderr)):
        want = _dec(exp[stream])
        if got != want:
            problems.append(_diff(stream, want, got))
    for name, want_enc in exp["files"].items():
        want, got = _dec(want_enc), got_files[name]
        if want != got:
            if want is None or got is None:
                problems.append(f"file {name}: expected {'absent' if want is None else 'present'}")
            else:
                problems.append(_diff(name, want, got))
    assert not problems, "\n".join(problems)
