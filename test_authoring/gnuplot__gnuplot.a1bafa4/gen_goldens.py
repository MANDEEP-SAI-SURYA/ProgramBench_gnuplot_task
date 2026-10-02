#!/usr/bin/env python3
"""Generate golden expectations by running the reference binary.

usage: gen_goldens.py REFERENCE_BINARY OUT_DIR

* stdin values starting with @@JSON@@ are replaced by the reference's own
  `--to-json` output for the rest of the string (used by from_json cases);
* each case is run twice, non-deterministic cases are rejected;
* cases a do-nothing stub would pass (exit 0, no output, files unchanged) are dropped.
"""
import base64
import json
import os
import subprocess
import sys
import tempfile
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from cases_src import CASES  # noqa: E402

ENV = {"PATH": "/usr/bin:/bin", "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"}


def b(x):
    return x if isinstance(x, bytes) else x.encode()


def enc(data: bytes) -> dict:
    try:
        return {"text": data.decode("utf-8")}
    except UnicodeDecodeError:
        return {"b64": base64.b64encode(data).decode()}


def run(binary, case):
    with tempfile.TemporaryDirectory() as d:
        for name, content in case["files"].items():
            p = Path(d) / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b(content))
        t = time.time()
        r = subprocess.run([binary, *case["argv"]], cwd=d, input=b(case["stdin"]), capture_output=True, timeout=20, env={**ENV, "HOME": d})
        dt = time.time() - t
        files_after = {}
        for name in case["check_files"]:
            p = Path(d) / name
            files_after[name] = enc(p.read_bytes()) if p.exists() else None
        return {"stdout": enc(r.stdout), "stderr": enc(r.stderr), "exit_code": r.returncode, "files": files_after}, dt


def main():
    binary, out = os.path.abspath(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    ids = [c["id"] for c in CASES]
    assert len(ids) == len(set(ids)), [i for i, n in Counter(ids).items() if n > 1]
    by_cat, problems, dropped = defaultdict(list), [], []
    for case in CASES:
        if isinstance(case["stdin"], str) and case["stdin"].startswith("@@JSON@@"):
            src = case["stdin"][len("@@JSON@@"):]
            case["stdin"] = subprocess.run([binary, "--to-json"], input=src.encode(), capture_output=True, check=True).stdout
        e1, dt = run(binary, case)
        e2, _ = run(binary, case)
        if e1 != e2:
            problems.append(f"{case['id']}: non-deterministic")
        unchanged = all(e1["files"][n] == enc(b(case["files"][n])) if n in case["files"] else e1["files"][n] is None
                        for n in case["check_files"])
        if e1["exit_code"] == 0 and e1["stdout"] == {"text": ""} and e1["stderr"] == {"text": ""} and unchanged:
            dropped.append(case["id"])
            continue
        if dt > 2:
            problems.append(f"{case['id']}: slow ({dt:.1f}s)")
        by_cat[case["category"]].append({
            "id": case["id"], "argv": case["argv"], "stdin": enc(b(case["stdin"])),
            "files": {k: enc(b(v)) for k, v in case["files"].items()},
            "check_files": case["check_files"], "expected": e1,
        })
    for cat, cases in by_cat.items():
        (out / f"{cat}.json").write_text(json.dumps(cases, indent=1, ensure_ascii=False) + "\n")
    total = sum(len(v) for v in by_cat.values())
    print(f"{total} cases in {len(by_cat)} categories -> {out}")
    print("per category:", dict(sorted((k, len(v)) for k, v in by_cat.items())))
    print(f"dropped as dummy-passable ({len(dropped)}): {dropped}")
    for p in problems:
        print("PROBLEM:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
