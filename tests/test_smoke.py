import json
import tarfile

from programbench.cli.main import main
from programbench.constants import BLOB_DIR, IMAGES_DIR
from programbench.utils.anti_cheat import sha256
from programbench.utils.load_data import load_all_instances


def test_cli_help(capsys):
    try:
        main(["--help"])
    except SystemExit as e:
        assert e.code == 0
    assert "eval" in capsys.readouterr().out


def test_instances_load():
    insts = load_all_instances()
    assert "gnuplot__gnuplot.a1bafa4" in insts
    for inst in insts.values():
        assert {"repository", "commit", "language", "eval_clean_hashes"} <= set(inst)
        assert inst["branches"]


def test_blobs_match_tests_json():
    for iid, inst in load_all_instances().items():
        for branch, info in inst["branches"].items():
            tar = BLOB_DIR / iid / "tests" / f"{branch}.tar.gz"
            assert tar.exists(), tar
            with tarfile.open(tar) as t:
                names = t.getnames()
            assert "eval/run.sh" in names
            modules = {n.split("/")[-1][:-3] for n in names if n.startswith("eval/tests/test_") and n.endswith(".py")}
            assert {t.split(".")[2] for t in info["tests"]} == modules
            assert len(info["tests"]) == len(set(info["tests"]))


def test_clean_hash_is_reference_binary():
    for iid, inst in load_all_instances().items():
        ref = IMAGES_DIR / iid / "task_cleanroom" / "workspace" / "gnuplot"
        assert sha256(ref) in inst["eval_clean_hashes"]


def test_test_runs_have_eval_json():
    from programbench.constants import TEST_RUNS_DIR

    for kind in ("correct", "incorrect"):
        for d in (TEST_RUNS_DIR / kind).iterdir():
            res = json.loads((d / f"{d.name}.eval.json").read_text())
            passed = sum(t["status"] == "passed" for t in res["test_results"])
            assert (passed == len(res["test_results"])) == (kind == "correct")


def test_verifier_pytest_is_pinned_everywhere():
    from programbench.constants import REPO_ROOT

    pinned = next(l.split("==")[1].strip() for l in (REPO_ROOT / "requirements-eval.txt").read_text().splitlines()
                  if l.startswith("pytest=="))
    for iid, inst in load_all_instances().items():
        for branch in inst["branches"]:
            with tarfile.open(BLOB_DIR / iid / "tests" / f"{branch}.tar.gz") as t:
                run_sh = t.extractfile("eval/run.sh").read().decode()
            assert f"PINNED={pinned}" in run_sh
        assert "requirements-eval.txt" in (IMAGES_DIR / iid / "task_cleanroom" / "Dockerfile").read_text()
