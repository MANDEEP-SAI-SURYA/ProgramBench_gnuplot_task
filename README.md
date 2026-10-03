<h1 align="center">ProgramBench — task contribution: <code>gnuplot__gnuplot.a1bafa4</code></h1>

<p align="center"><em>Can a language model rebuild gnuplot 5.4.9 from only its binary and documentation?</em></p>

This repository follows the layout of
[facebookresearch/ProgramBench](https://github.com/facebookresearch/ProgramBench) and adds one
new instance. An agent receives only the compiled `gnuplot` binary and its manual, and has to
write a complete codebase whose `compile.sh` produces `./executable`. 510 hidden behavioural
tests, organised in 7 test branches, compare it against the original.

| | |
|---|---|
| Instance | `gnuplot__gnuplot.a1bafa4` (gnuplot 5.4 patchlevel 9, tag `5.4.9`) |
| Reference | C, ~165k LOC, static stripped x86-64 binary |
| Tests | 510 in 7 branches, flat unweighted score; reference 100%, do-nothing stub 0% |
| Calibration | blind Claude Opus 5.5 run, offline: **55.1%** (target: < 70% on average) |

## Quickstart

```bash
pip install -r requirements-eval.txt                  # pinned verifier: pytest==9.1.1
cd src
python3 -m programbench gold --skip-source              # reference binary must score 100%

# score an agent's codebase (directory with compile.sh)
python3 -m programbench pack /path/to/agent/codebase ../runs/my-run --instance gnuplot__gnuplot.a1bafa4
python3 -m programbench eval ../runs/my-run              # writes <instance>.eval.json, prints the score
python3 -m programbench info ../runs/my-run
```

See [docs/README.md](docs/README.md) for the full usage guide (inference setup, Docker images,
evaluation, output format) and [docs/tasks/gnuplot__gnuplot.a1bafa4.md](docs/tasks/gnuplot__gnuplot.a1bafa4.md)
for the task card (design, difficulty calibration, fairness notes).

## Layout

```
.
├── README.md  CLAUDE.md  CONTRIBUTING.md  LICENSE  pyproject.toml  .python-version
├── requirements-eval.txt               pinned verifier (pytest==9.1.1)
├── .github/workflows/test.yml          CI: harness self-tests + gold check
├── calibration/<instance_id>/          difficulty evidence: prompt, settings, 8 runs (trajectories, submissions, scores)
├── docs/
│   ├── README.md                       usage guide (inference + evaluation)
│   └── tasks/<instance_id>.md          task card: design, calibration, fairness notes
├── src/programbench/                   harness (same package layout as upstream)
│   ├── cli/main.py                     `programbench eval | info | pack | check-executable | gold | blob | images`
│   ├── eval/eval.py                    compile → per-branch test run → JUnit → <iid>.eval.json
│   ├── utils/                          load_data, blob_store, internet_control, instance_filters, anti_cheat
│   ├── constants.py  exceptions.py
│   └── data/
│       ├── tasks/<instance_id>/        task.yaml + tests.json   (the instance registry entry)
│       └── test_runs/{correct,incorrect}/<instance_id>/  submission.zip + <iid>.eval.json
├── tests/                              harness self-tests (pytest)
│
│   ── material that upstream keeps outside the git repo ──
├── blobs/<instance_id>/tests/<branch>.tar.gz   = HF dataset programbench/ProgramBench-Tests
├── images/<instance_id>/
│   ├── task_cleanroom/                 = Docker image :task_cleanroom_v6 (agent sees only this)
│   │   ├── Dockerfile
│   │   └── workspace/                  gnuplot binary, TASK.md, docs/, examples/
│   └── task/Dockerfile                 = Docker image :task_v6 (full build env, maintainers)
├── sources/<instance_id>/              = upstream repo at the pinned commit + build-only patch + build.sh
└── test_authoring/<instance_id>/       how the hidden tests were produced (cases, goldens, branch builder)
```
