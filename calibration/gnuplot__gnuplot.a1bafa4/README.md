# Difficulty calibration — gnuplot__gnuplot.a1bafa4

**Result: 8 independent Claude Opus 5.5 runs on the frozen revision, mean score 49.53%
(σ 6.04, min 39.22%, max 54.90%). Target: mean < 70%. No difficulty change was needed.**

## Frozen revision

`b62a6b5b47e08edc2d67460a9498457d44a83f7b` ("Pin verifier (pytest==9.1.1) and freeze revision for
calibration"). It contains the final 510 tests (7 branches), the pinned verifier and this
protocol. All runs were started after that commit and scored against it. The commit adding these
results changes only `calibration/` (plus documentation pointing to it): no test, blob, golden
output, harness file or agent-bundle file changed.

## Protocol and settings

| Setting | Value |
|---|---|
| Model | Claude Opus 5.5, model id `claude-opus-5-5` (recorded per message in every trajectory); provider default sampling settings, nothing overridden |
| Agent | Claude Code agent SDK, general-purpose agent, version `2.1.288` (recorded in trajectories); tools available: Bash, Read, Write, Edit, Glob, Grep, web tools. Tools actually used (from trajectories): Bash and Write only. No web tool was ever called |
| Sessions | 8 independent fresh sessions (no shared memory, no previous solution); each in its own fresh copy of `images/<iid>/task_cleanroom/workspace/` (binary + docs + TASK.md + examples only) |
| Prompt | `PROMPT.md`, identical for every run (`{WS}` replaced by that run's workspace path) |
| Isolation | task sources, tests, goldens, earlier solutions and packaged outputs were moved to a stash directory under `/root` for the duration of the runs (the orchestrating session's own transcript also stayed under `/root`). The prompt forbids reading outside the workspace, disassembling the binary, using the internet or wrapping the binary. The audit below confirms no shell command touched `/root`, `/home/claude`, another run, or the network, and every `Write` targeted the run's own workspace (run_02 also kept shell-created scratch files one level above its workspace, see integrity notes) |
| Budget | one session per run, prompt asks to finish within ~90 min; no token or turn cap. Actual: 25–39 min, 64–127 tool calls, 44k–112k output tokens (table below) |
| Scoring | `cd src && python3 -m programbench eval ../calibration/gnuplot__gnuplot.a1bafa4/runs/run_NN` at the frozen revision, verifier pytest 9.1.1 (recorded in each eval.json under `verifier`) |
| Concurrency | runs 01–04 in parallel (2026-10-03 04:37 UTC), 05–06 in parallel (09:30 UTC), 07–08 in parallel (09:59 UTC) |

## Results

| Run | Passed | Score | Wall time (min) | Tool calls | Output tokens | Input tokens (incl. cache) | Solution LOC | Language |
|---|---|---|---|---|---|---|---|---|
| run_01 | 267/510 | **52.35%** | 33.8 | 95 | 79,735 | 36,163,077 | 8873 | Go |
| run_02 | 200/510 | **39.22%** | 25.1 | 64 | 44,034 | 18,908,396 | 7474 | Go |
| run_03 | 235/510 | **46.08%** | 25.4 | 68 | 52,855 | 19,714,564 | 8124 | Go |
| run_04 | 218/510 | **42.75%** | 29.1 | 83 | 48,264 | 27,016,218 | 8376 | Go |
| run_05 | 280/510 | **54.90%** | 29.0 | 93 | 95,918 | 35,952,177 | 8684 | Go |
| run_06 | 277/510 | **54.31%** | 28.2 | 77 | 96,630 | 27,098,292 | 9338 | Go |
| run_07 | 278/510 | **54.51%** | 39.2 | 127 | 112,102 | 56,603,544 | 9555 | Go |
| run_08 | 266/510 | **52.16%** | 29.7 | 71 | 106,314 | 23,629,091 | 8225 | Go |
| **mean** | 252.6/510 | **49.53%** | 30.0 | 84.8 | | | | |

Mean pass rate per test module over the 8 runs:

| Module | Mean | Module | Mean |
|---|---|---|---|
| test_cli | 85.6% | test_show | 54.8% |
| test_program | 78.4% | test_table | 51.4% |
| test_expr | 72.6% | test_table_matrix | 81.2% |
| test_expr_print | 100.0% | test_table3d | 12.5% |
| test_format | 79.5% | test_smooth | 33.9% |
| test_errors | 59.6% | test_smooth_matrix | 55.1% |
| test_dumb | 20.3% | test_stats | 32.7% |
| test_dumb_matrix | 50.9% | test_stats_matrix | 14.6% |
| test_dumb3d | 0.0% | test_fit | 15.4% |
| test_multiplot | 0.0% | test_fit_matrix | 29.2% |
| test_svg | 0.0% | test_terminals | 0.0% |

## Files

```
PROMPT.md                     exact prompt
run_claude_code.sh            reproduce one run with the Claude Code CLI (headless) in the cleanroom image
summary.json                  machine-readable table above (regenerate: python3 tools/summarize.py)
tools/package_runs.py         how trajectories/submissions/meta were collected (incl. the shell-command audit)
tools/summarize.py
runs/run_NN/
  trajectory.jsonl.gz         complete agent trajectory: every message, tool call and tool result, with timestamps,
                              model id and token usage (Claude Code JSONL transcript)
  meta.json                   model, agent version, start/end, tool calls, token usage, budget, audit flags
  gnuplot__gnuplot.a1bafa4/
    submission.tar.gz         the agent's codebase (compile.sh at root; build caches excluded)
    gnuplot__gnuplot.a1bafa4.eval.json   full evaluation output (per-test status, logs, verifier versions)
runs/_aborted_rate_limited/   4 attempts of runs 05–08 started at 05:11 UTC and killed after ~5 min by an
                              API rate limit; never scored; repeated from scratch in fresh workspaces
```

## Integrity notes

* **Audit:** `tools/package_runs.py` scans every shell command in each trajectory for access to
  other runs or task material (`/home/claude`, `/root/`, other `/tmp/cal/run_NN`), disassembly
  (`strings`, `objdump`) and downloads (`curl`, `wget`, `pip install`, `go get`). There are no
  flags in any run (`meta.json` → `audit_flags`).
* **run_02** said in its final message that it kept scratch probe files in its own run directory
  (`/tmp/cal/run_02/`, one level above its workspace) and deleted them at the end. That directory
  held only its own files, so the run is kept; it is also the lowest score (39.22%).
* **Anti-cheat:** each submission passed the harness checks: no copy of the reference
  (`eval_clean_hashes`), no wrapper around it.
* **Interruption:** the 4 rate-limited attempts were discarded before scoring. Their trajectories
  are kept for transparency. Each counted run is a complete, uninterrupted session.
