import os
from pathlib import Path

import pytest

from programbench.constants import IMAGES_DIR, TEST_RUNS_DIR
from programbench.eval.eval import Evaluator, score
from programbench.utils.load_data import load_all_instances

IID = "gnuplot__gnuplot.a1bafa4"
REF = IMAGES_DIR / IID / "task_cleanroom" / "workspace" / "gnuplot"


@pytest.fixture(scope="module")
def inst():
    return load_all_instances()[IID]


def _submission(tmp_path: Path, compile_sh: str) -> Path:
    d = tmp_path / "sub"
    d.mkdir()
    (d / "compile.sh").write_text("#!/bin/bash\nset -e\n" + compile_sh)
    (d / "compile.sh").chmod(0o755)
    return d


def test_reference_binary_scores_100(inst):
    res = Evaluator(inst, REF, prebuilt=REF).run()
    assert score(res, inst)[0] == score(res, inst)[1] > 0


def test_dummy_scores_0(inst, tmp_path):
    sub = _submission(tmp_path, 'printf "#!/bin/sh\\nexit 0\\n" > executable; chmod +x executable\n')
    res = Evaluator(inst, sub).run()
    assert res["error_code"] is None
    assert score(res, inst)[0] == 0


def test_copy_of_reference_is_removed(inst, tmp_path):
    sub = _submission(tmp_path, "cp ref.bin executable\n")
    (sub / "ref.bin").write_bytes(REF.read_bytes())
    res = Evaluator(inst, sub).run()
    assert res["error_code"] == "compile_failed"  # ref.bin was deleted before compiling


def test_wrapper_is_rejected(inst, tmp_path):
    sub = _submission(tmp_path, f'printf "#!/bin/sh\\nexec {REF} \\\\"\\$@\\\\"\\n" > executable; chmod +x executable\n')
    res = Evaluator(inst, sub).run()
    assert res["error_code"] == "reference_wrapper"


def test_missing_compile_script(inst, tmp_path):
    d = tmp_path / "empty"
    d.mkdir()
    assert Evaluator(inst, d).run()["error_code"] == "no_compile_script"


@pytest.mark.skipif(not os.environ.get("PROGRAMBENCH_SLOW"), reason="builds gnuplot from source (~1 min); set PROGRAMBENCH_SLOW=1")
def test_gold_submission_from_source(inst):
    res = Evaluator(inst, TEST_RUNS_DIR / "correct" / IID / "submission.zip").run()
    assert score(res, inst)[0] == score(res, inst)[1]
