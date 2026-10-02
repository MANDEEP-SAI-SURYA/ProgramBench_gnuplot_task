#!/usr/bin/env python3
"""Turn golden cases into ProgramBench test branches.

usage: build_branches.py GOLDEN_DIR REPO_ROOT

GOLDEN_DIR is the output of gen_goldens.py (one <category>.json per category).
Writes, for instance gnuplot__gnuplot.a1bafa4:

  test_authoring/<iid>/branches/<branch>/eval/...     readable branch sources
  blobs/<iid>/tests/<branch>.tar.gz                   what the harness copies into /workspace
  src/programbench/data/tasks/<iid>/tests.json        branch -> test names (ProgramBench schema)

Each branch tarball unpacks to

  eval/run.sh                 runs pytest, writes eval/results.xml (JUnit)
  eval/__init__.py
  eval/tests/__init__.py
  eval/tests/_harness.py      runs ./executable for one case and compares outputs
  eval/tests/golden/<cat>.json
  eval/tests/test_<cat>.py    one test function per case

so test ids are eval.tests.test_<cat>.test_<name>, exactly like upstream tasks.
"""
import hashlib
import io
import json
import re
import shutil
import sys
import tarfile
from pathlib import Path

IID = "gnuplot__gnuplot.a1bafa4"

BRANCHES = {
    "cli_and_programs": ["cli", "program"],
    "expressions_and_formatting": ["expr", "expr_print", "format"],
    "errors_and_show": ["errors", "show"],
    "table_output": ["table", "table_matrix", "table3d"],
    "smoothing_stats_fit": ["smooth", "smooth_matrix", "stats", "stats_matrix", "fit", "fit_matrix"],
    "dumb_terminal": ["dumb", "dumb_matrix", "dumb3d", "multiplot"],
    "vector_terminals": ["terminals", "svg"],
}

RUN_SH = """#!/usr/bin/env bash
# Run from /workspace (the directory that contains ./executable).
set -u
cd "$(dirname "$0")/.."
TIMEOUT_ARGS=""
if python3 -c "import pytest_timeout" 2>/dev/null; then TIMEOUT_ARGS="--timeout=60 --timeout-method=thread"; fi
XDIST_ARGS=""
if python3 -c "import xdist" 2>/dev/null; then XDIST_ARGS="-n auto"; fi
python3 -m pytest eval/tests -v -p no:cacheprovider --rootdir="$PWD" \\
  --junitxml=eval/results.xml -o junit_family=xunit1 $TIMEOUT_ARGS $XDIST_ARGS
exit 0
"""

HARNESS = '''"""Shared runner for the gnuplot behavioural tests (stdlib only).

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
    assert not problems, "\\n".join(problems)
'''


def ident(name):
    s = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    return s if not s[0].isdigit() else "_" + s


def branch_id(name):
    return hashlib.sha1(f"{IID}/{name}".encode()).hexdigest()[:12]


def preview(case):
    files = case["files"]
    script = files.get("t.gp", {}).get("text")
    lines = [f"argv: {case['argv']}"]
    if script is not None:
        lines.append("t.gp:")
        lines += ["    " + l for l in script.splitlines()[:25]]
        if script.count("\n") > 25:
            lines.append("    ...")
    stdin = case["stdin"].get("text", "")
    if stdin:
        lines.append("stdin: " + repr(stdin[:200]))
    return "\n    ".join(lines).replace('"""', "'''").replace("\\", "\\\\")


def main():
    golden_dir, root = Path(sys.argv[1]), Path(sys.argv[2])
    authoring = root / "test_authoring" / IID / "branches"
    blobs = root / "blobs" / IID / "tests"
    for p in (authoring, blobs):
        shutil.rmtree(p, ignore_errors=True)
        p.mkdir(parents=True)
    all_cats = {p.stem for p in golden_dir.glob("*.json")}
    used = {c for cats in BRANCHES.values() for c in cats}
    assert all_cats == used, (all_cats - used, used - all_cats)
    tests_json = {"branches": {}}
    for bname, cats in BRANCHES.items():
        bid = branch_id(bname)
        bdir = authoring / bid
        tdir = bdir / "eval" / "tests"
        (tdir / "golden").mkdir(parents=True)
        (bdir / "eval" / "run.sh").write_text(RUN_SH)
        (bdir / "eval" / "run.sh").chmod(0o755)
        (bdir / "eval" / "__init__.py").write_text("")
        (tdir / "__init__.py").write_text("")
        (tdir / "_harness.py").write_text(HARNESS)
        (bdir / "BRANCH.md").write_text(f"# branch {bid} ({bname})\n\ncategories: {', '.join(cats)}\n")
        names = []
        for cat in cats:
            cases = json.loads((golden_dir / f"{cat}.json").read_text(encoding="utf-8"))
            shutil.copy(golden_dir / f"{cat}.json", tdir / "golden" / f"{cat}.json")
            out = [f'"""Behavioural tests: {cat} ({len(cases)} cases, golden outputs in golden/{cat}.json)."""',
                   "from eval.tests._harness import check", ""]
            seen = set()
            for c in cases:
                fn = "test_" + ident(c["id"].split(".", 1)[1])
                assert fn not in seen, fn
                seen.add(fn)
                out += ["", f"def {fn}():", f'    """{preview(c)}\n    """', f'    check("{c["id"]}")', ""]
                names.append(f"eval.tests.test_{cat}.{fn}")
            (tdir / f"test_{cat}.py").write_text("\n".join(out))
        tests_json["branches"][bid] = {"ignored": False, "ignore_reason": "", "tests": sorted(names), "ignored_tests": []}
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz", format=tarfile.PAX_FORMAT) as tf:
            for p in sorted((bdir / "eval").rglob("*")):
                ti = tf.gettarinfo(str(p), arcname=str(p.relative_to(bdir)))
                ti.uid = ti.gid = 0
                ti.uname = ti.gname = "root"
                ti.mtime = 0
                if p.is_file():
                    with p.open("rb") as f:
                        tf.addfile(ti, f)
                else:
                    tf.addfile(ti)
        (blobs / f"{bid}.tar.gz").write_bytes(buf.getvalue())
        print(f"{bid}  {bname:<28} {len(names):>4} tests  ({', '.join(cats)})")
    task_dir = root / "src" / "programbench" / "data" / "tasks" / IID
    task_dir.mkdir(parents=True, exist_ok=True)
    (task_dir / "tests.json").write_text(json.dumps(tests_json, indent=2, sort_keys=True))
    print("total", sum(len(b["tests"]) for b in tests_json["branches"].values()))


if __name__ == "__main__":
    main()
