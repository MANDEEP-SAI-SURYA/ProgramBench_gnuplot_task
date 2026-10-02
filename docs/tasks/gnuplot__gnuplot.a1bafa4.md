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

Candidates were calibrated with blind, offline runs of a Claude Opus 5.5 agent that saw only
the agent bundle:

| Candidate | Result | Decision |
|---|---|---|
| Author-written 4.5k-LOC scripting-language interpreter | 99.7% (37 min) | rejected: too easy |
| shfmt v3.12.0 (mvdan/sh) | 80.7% with the run unfinished (61 min, rate-limited) | rejected: too easy |
| gnuplot 5.4.9, first suite (441 tests) | 63.3% (33 min, 9.7k LOC Go) | suite deepened |
| **gnuplot 5.4.9, final suite (510 tests)** | **55.1%** (same solution) | accepted |

The calibration solution is kept as `src/programbench/data/test_runs/incorrect/<iid>/`
(score 281/510). Per area it reached: CLI 80%, expressions 78–100%, errors 62%, show 68%,
tables 51–96%, smoothing 32–38%, stats 0–31%, fit 23–33%, dumb plots 0–66%, svg/canvas 0%.

The JD target is < 70% averaged over about 8 runs. A single 33-minute run is only an estimate:
longer runs will close some gaps (3D, multiplot, svg). The suite was deepened to leave margin.

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
