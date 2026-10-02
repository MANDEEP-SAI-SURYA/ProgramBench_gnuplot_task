# Usage guide

## Inference (running a solving agent)

The agent must see **only** `images/gnuplot__gnuplot.a1bafa4/task_cleanroom/workspace/`:

```
workspace/
├── gnuplot          reference binary (static, stripped, linux/amd64)
├── TASK.md          task statement, rules and how scoring works
├── docs/            gnuplot.gih (full reference manual), gnuplot.1 (man page)
└── examples/        a few scripts with captured stdout/stderr/exit code
```

> [!IMPORTANT]
> The agent MUST NOT have internet access during inference.

Preferred: the Docker image (same naming as upstream, `__` → `_1776_`).

```bash
cd src && python3 -m programbench images build      # builds :task_cleanroom_v6 and :task_v6
docker run -it --network none programbench/gnuplot_1776_gnuplot.a1bafa4:task_cleanroom_v6 bash
```

Without Docker, copy `workspace/` to an empty directory on a machine without gnuplot sources and
start the agent there with networking disabled. Tell the agent to read `TASK.md` first. For
Claude Code / Codex style agents a good prompt is: *"Read TASK.md and complete the task in this
directory. Work offline. Your deliverable is compile.sh that produces ./executable."*

The submission is the complete codebase the agent produced (with `compile.sh` at its root).

## Evaluation

Put submissions in the upstream run layout:

```
my-run/
└── gnuplot__gnuplot.a1bafa4/
    └── submission.tar.gz        (submission.zip or an unpacked submission/ directory also work)
```

`programbench pack CODEBASE my-run --instance gnuplot__gnuplot.a1bafa4` creates it from a directory.

```bash
cd src
python3 -m programbench eval ../my-run                   # local backend (default)
python3 -m programbench eval ../my-run --backend docker  # every step inside :task_cleanroom_v6
python3 -m programbench info ../my-run                   # summary again later
```

Pipeline (step names as upstream): wipe workspace → extract submission → remove files whose
sha256 is in `eval_clean_hashes` → remove any shipped `./executable` → `compile.sh` with the
network blocked → hash `./executable` → reject the reference binary or wrappers that point to
it → for every test branch, in a fresh copy of the compiled workspace: extract
`blobs/<iid>/tests/<branch>.tar.gz`, restore and verify `./executable`, run `eval/run.sh`, read
`eval/results.xml`.

Requirements, local backend: Linux x86-64, `bash`, `python3` ≥ 3.10 with `pytest`, plus the
toolchain the submission's `compile.sh` needs. Network blocking uses `unshare -rn` when allowed.

### Output

`<run>/<iid>/<iid>.eval.json`, upstream schema:

```json
{
  "test_results": [{"name": "eval.tests.test_dumb.test_sin_default", "branch": "8f4b382f07f4",
                    "status": "passed", "extra": {"time": 0.01}}, ...],
  "error_code": null, "error_details": null,
  "log": [{"step": "compile", "command": "...", "wall_time": 1.2, "output": "...", "returncode": 0}, ...],
  "solution_branch": "submission",
  "test_branches": ["d909783f33c7", ...],
  "test_branch_errors": {},
  "executable_hash": "…",
  "warnings": [],
  "structure": {"files": 21, "nonblank_loc": 9372, "languages": {...}}
}
```

`structure` is an addition: a size/language report of the submission for reviewers.

### Scoring

Flat, unweighted percentage of non-ignored tests with status `passed`. A test passes only if
stdout, stderr and the exit status match the reference byte for byte (plus the content of files
the test checks, e.g. `set print 'out.txt'`). Each test runs in a fresh temporary directory with
`LC_ALL=C.UTF-8` and `HOME` set to that directory.

### Test branches

| Branch | Name | Tests | Modules |
|---|---|---|---|
| d909783f33c7 | cli_and_programs | 42 | test_cli, test_program |
| e25ad822d6e3 | expressions_and_formatting | 65 | test_expr, test_expr_print, test_format |
| 26b37877411a | errors_and_show | 104 | test_errors, test_show |
| edd4682a61c3 | table_output | 71 | test_table, test_table_matrix, test_table3d |
| 1fe6fa7ee706 | smoothing_stats_fit | 90 | test_smooth, test_smooth_matrix, test_stats, test_stats_matrix, test_fit, test_fit_matrix |
| 8f4b382f07f4 | dumb_terminal | 125 | test_dumb, test_dumb_matrix, test_dumb3d, test_multiplot |
| 743807875866 | vector_terminals | 13 | test_terminals, test_svg |

A branch can also be run by hand, exactly as the harness does:

```bash
mkdir ws && cp /path/to/executable ws/executable
tar -xzf blobs/gnuplot__gnuplot.a1bafa4/tests/8f4b382f07f4.tar.gz -C ws
cd ws && ./eval/run.sh          # JUnit XML in eval/results.xml
```

## Self-checks

```bash
python3 -m pytest tests                      # reference 100%, stub 0%, copy/wrapper rejected
cd src && python3 -m programbench gold       # + gold submission built from source = 100% (~1 min)
```
