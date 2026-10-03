# Task card — `gnuplot__gnuplot.a1bafa4`

| Field | Value |
|---|---|
| Program | gnuplot 5.4 patchlevel 9 |
| Upstream | gnuplot (SourceForge; GitHub mirror `gnuplot/gnuplot`), tag `5.4.9`, commit `a1bafa410d3c07d832f81884c5af61dee73fb1c5` |
| License | gnuplot license (permissive) |
| Reference | C, ~165k non-blank LOC (src/ + term/); static, stripped linux/amd64 binary |
| Build | `sources/<iid>/build.sh`: offline, reproducible (identical sha256 across builds); no X11/Qt/wx/cairo/libgd/lua/readline; one 2-line build-only patch |
| Agent inputs | binary, full reference manual (`gnuplot.gih`), man page, `TASK.md`, examples |
| Tests | 510 behavioural tests in 7 branches |
| Scoring | flat % of tests passed; stdout + stderr + exit status (+ checked files) byte-exact |
| Quality checks | reference 100%; gold submission built from source 100%; do-nothing stub 0%; every case run twice at generation (deterministic) |
| Verifier | pytest 9.1.1, pinned (`requirements-eval.txt`, Dockerfile, every `eval/run.sh`) |
| Calibration | 8 × Claude Opus 5.5 on the frozen revision: mean 49.53% |

## What is tested

| Area | Tests | Notes |
|---|---|---|
| CLI and program structure | 42 | options, `-e`, `-c` + ARGs, stdin, exit codes, `load`/`call`/`eval`/macros, `set print` files, datablocks |
| Expressions and formatting | 65 | int/float/complex/string semantics, overflow, special functions, `sprintf`, `gprintf` |
| Errors and `show` | 104 | error text with caret lines and file/line prefixes; `show` output for ~60 settings |
| Table output | 71 | `set table` for functions, data (`using`, `every`, `index`, missing values, time data, headers), 3D grids, contours, dgrid3d |
| Smoothing, stats, fit | 90 | all `smooth` algorithms and `bins`; `stats` reports and variables; `fit` iteration logs, reports, variables |
| Dumb terminal | 125 | 2D styles, keys, tics, labels, log scales, 3D (`splot`, hidden3d, contours), multiplot |
| Vector terminals | 13 | svg, canvas, terminal options |

## Difficulty calibration

**Final batch (the evidence):** 8 independent Claude Opus 5.5 runs on frozen revision
`b62a6b5b47e08edc2d67460a9498457d44a83f7b`. Mean **49.53%** (σ 6.04, min 39.22%, max 54.90%),
target < 70%. Complete trajectories, submissions, eval.json files, model settings and budgets are in
[`calibration/gnuplot__gnuplot.a1bafa4/`](../../calibration/gnuplot__gnuplot.a1bafa4/README.md).

Strongest areas for the agents: CLI, expressions and formatting (72–100%). Weakest: 3D,
multiplot, svg/canvas (0%), fit (15–29%), stats (15–33%), dumb-terminal plots (20–51%).

**History (candidate selection, before the freeze):**

| Candidate | Result | Decision |
|---|---|---|
| Author-written 4.5k-LOC scripting-language interpreter | one run, 99.7% | rejected: too easy |
| shfmt v3.12.0 (mvdan/sh) | one unfinished run, 80.7% | rejected: too easy |
| gnuplot 5.4.9, first suite (441 tests) | one run, 63.3% | suite deepened to 510 tests |

`src/programbench/data/test_runs/incorrect/` keeps the solution from that pre-freeze run as an
example of a partial submission (281/510 on the final suite). It is not part of the calibration.

## Fairness notes

* Every tested behaviour is deterministic and observable by running the binary; most is
  described in the manual. Where the manual and the binary disagree, the binary is authoritative
  (stated in TASK.md).
* Excluded at authoring time: outputs containing dates (fit.log header, EPS CreationDate),
  cases where the reference crashes, and cases a do-nothing executable would pass.
* Risk: a few tests print floating-point results to 15–17 significant digits; an implementation
  using a different libm might differ in the last digit. Most numeric tests print ≤ 6 digits.
* Source lookup is prevented by the cleanroom image (no sources) and an offline sandbox; the
  harness also deletes copies of the reference (`eval_clean_hashes`) and rejects wrappers.
