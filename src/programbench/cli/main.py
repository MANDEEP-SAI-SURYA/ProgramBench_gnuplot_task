"""programbench CLI (stdlib argparse; run as `python3 -m programbench` or `programbench`).

  eval RUN_DIR...              evaluate <run>/<instance_id>/submission.tar.gz -> <instance_id>.eval.json
  info RUN_DIR...              summarise eval.json files (score per instance and per test module)
  pack CODEBASE RUN_DIR        package an agent's codebase into <run>/<instance_id>/submission.tar.gz
  check-executable PATH        run all test branches against a prebuilt binary (e.g. the reference)
  gold                         gold self-checks: reference binary + gold submission must score 100%
  blob list                    list the local test blobs (stand-in for the HF test dataset)
  images build                 docker build the instance images (task_cleanroom_v6, task_v6)
"""
import argparse
import json
import subprocess
import sys
import tarfile
from collections import defaultdict
from pathlib import Path

from programbench.constants import (
    BLOB_DIR,
    CLEANROOM_TAG,
    DOCKER_EXECUTABLE,
    IMAGES_DIR,
    REPO_ROOT,
    TASK_TAG,
    TEST_RUNS_DIR,
)
from programbench.eval.eval import Evaluator, score, write_result
from programbench.utils.instance_filters import filter_instances
from programbench.utils.load_data import load_all_instances

SUBMISSION_NAMES = ("submission.tar.gz", "submission.zip", "submission")


def _find_submission(d: Path) -> Path | None:
    return next((d / n for n in SUBMISSION_NAMES if (d / n).exists()), None)


def _print_result(iid: str, result: dict, inst: dict) -> None:
    passed, total = score(result, inst)
    by_mod: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for t in result["test_results"]:
        mod = t["name"].rsplit(".", 1)[0].replace("eval.tests.", "")
        by_mod[mod][1] += 1
        by_mod[mod][0] += t["status"] == "passed"
    print(f"\n== {iid}")
    if result.get("error_code"):
        print(f"   ERROR {result['error_code']}: {(result.get('error_details') or '')[:300]}")
    for b, e in result.get("test_branch_errors", {}).items():
        print(f"   branch {b} error {e['error_code']}: {e['error_details'][:200]}")
    for w in result.get("warnings", []):
        print(f"   warning: {w}")
    s = result.get("structure")
    if s:
        langs = ", ".join(f"{k} {v['nonblank_loc']} LOC/{v['files']} files" for k, v in s["languages"].items())
        print(f"   submission: {s['files']} files, {s['nonblank_loc']} non-blank source LOC ({langs})")
    for mod, (p, n) in sorted(by_mod.items()):
        print(f"   {mod:<22} {p:>4}/{n:<4} {100 * p / n:6.1f}%  {'#' * int(20 * p / n)}")
    print(f"   SCORE {passed}/{total} = {100 * passed / max(total, 1):.2f}%   executable_hash={result.get('executable_hash')}")


def cmd_eval(a) -> int:
    instances = load_all_instances()
    rc = 0
    for src in a.sources:
        run = Path(src).resolve()
        ids = filter_instances(sorted(d.name for d in run.iterdir() if d.is_dir() and d.name in instances),
                               a.filter, a.slice)
        if not ids:
            print(f"no known instance directories with a submission under {run}", file=sys.stderr)
            rc = 1
        for iid in ids:
            d = run / iid
            out = d / f"{iid}.eval.json"
            sub = _find_submission(d)
            if sub is None:
                continue
            if out.exists() and not a.force:
                print(f"{iid}: {out.name} exists (use -f to re-evaluate)")
            else:
                print(f"{iid}: evaluating {sub} [{a.backend}]", flush=True)
                result = Evaluator(instances[iid], sub, backend=a.backend, image_tag=a.image_tag,
                                   keep_workdir=a.keep).run()
                write_result(result, out)
            result = json.loads(out.read_text())
            _print_result(iid, result, instances[iid])
            rc |= 1 if result.get("error_code") else 0
    return rc


def cmd_info(a) -> int:
    instances = load_all_instances()
    for src in a.sources:
        for out in sorted(Path(src).glob("*/*.eval.json")):
            iid = out.parent.name
            if iid in instances:
                _print_result(iid, json.loads(out.read_text()), instances[iid])
    return 0


def cmd_pack(a) -> int:
    instances = load_all_instances()
    iid = a.instance or next(iter(instances))
    code, dest = Path(a.codebase).resolve(), Path(a.run_dir) / iid
    if not (code / "compile.sh").exists():
        print(f"warning: {code}/compile.sh does not exist", file=sys.stderr)
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(dest / "submission.tar.gz", "w:gz") as t:
        for p in sorted(code.iterdir()):
            if p.name in (".git", "executable"):
                continue
            t.add(p, arcname=p.name)
    print(dest / "submission.tar.gz")
    return 0


def cmd_check_executable(a) -> int:
    instances = load_all_instances()
    iid = a.instance or next(iter(instances))
    result = Evaluator(instances[iid], Path(a.path), prebuilt=Path(a.path).resolve()).run()
    if a.output:
        write_result(result, Path(a.output))
    _print_result(iid, result, instances[iid])
    passed, total = score(result, instances[iid])
    return 0 if passed == total else 1


def cmd_gold(a) -> int:
    instances = load_all_instances()
    rc = 0
    for iid in filter_instances(list(instances), a.filter, ""):
        inst = instances[iid]
        ref = IMAGES_DIR / iid / "task_cleanroom" / "workspace" / iid.split("__")[1].split(".")[0]
        checks = [("reference binary", Evaluator(inst, ref, prebuilt=ref))]
        gold = TEST_RUNS_DIR / "correct" / iid
        sub = _find_submission(gold) if gold.exists() else None
        if sub and not a.skip_source:
            checks.append(("gold submission (built from source)", Evaluator(inst, sub, backend=a.backend)))
        for label, ev in checks:
            print(f"{iid}: {label}", flush=True)
            res = ev.run()
            passed, total = score(res, inst)
            _print_result(iid, res, inst)
            rc |= passed != total
    return rc


def cmd_blob(a) -> int:
    for d in sorted(BLOB_DIR.iterdir()):
        for t in sorted((d / "tests").glob("*.tar.gz")):
            print(f"{d.name}/tests/{t.name}  {t.stat().st_size} bytes")
    return 0


def cmd_images(a) -> int:
    instances = load_all_instances()
    for iid, inst in instances.items():
        for sub, tag in (("task_cleanroom", CLEANROOM_TAG), ("task", TASK_TAG)):
            ctx = IMAGES_DIR / iid / sub
            print(f"building {inst['image_name']}:{tag} from {ctx}", flush=True)
            r = subprocess.run([DOCKER_EXECUTABLE, "build", "-t", f"{inst['image_name']}:{tag}", "-f",
                                str(ctx / "Dockerfile"), str(REPO_ROOT)])
            if r.returncode:
                return r.returncode
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="programbench", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("eval", help="evaluate run directories")
    p.add_argument("sources", nargs="+")
    p.add_argument("--backend", choices=["local", "docker"], default="local")
    p.add_argument("--image-tag", default=CLEANROOM_TAG)
    p.add_argument("-f", "--force", action="store_true")
    p.add_argument("--filter", default="")
    p.add_argument("--slice", default="")
    p.add_argument("--keep", action="store_true", help="keep temporary workspaces for debugging")
    p.set_defaults(fn=cmd_eval)
    p = sp.add_parser("info", help="summarise existing eval.json files")
    p.add_argument("sources", nargs="+")
    p.set_defaults(fn=cmd_info)
    p = sp.add_parser("pack", help="package a codebase as a submission")
    p.add_argument("codebase")
    p.add_argument("run_dir")
    p.add_argument("--instance", default="")
    p.set_defaults(fn=cmd_pack)
    p = sp.add_parser("check-executable", help="run the tests against a prebuilt binary")
    p.add_argument("path")
    p.add_argument("--instance", default="")
    p.add_argument("-o", "--output", default="")
    p.set_defaults(fn=cmd_check_executable)
    p = sp.add_parser("gold", help="reference + gold submission must pass 100%%")
    p.add_argument("--filter", default="")
    p.add_argument("--skip-source", action="store_true", help="only check the reference binary (fast)")
    p.add_argument("--backend", choices=["local", "docker"], default="local")
    p.set_defaults(fn=cmd_gold)
    p = sp.add_parser("blob", help="test blobs")
    p.add_argument("action", choices=["list"])
    p.set_defaults(fn=cmd_blob)
    p = sp.add_parser("images", help="docker images")
    p.add_argument("action", choices=["build"])
    p.set_defaults(fn=cmd_images)
    a = ap.parse_args(argv)
    return a.fn(a)


app = main
