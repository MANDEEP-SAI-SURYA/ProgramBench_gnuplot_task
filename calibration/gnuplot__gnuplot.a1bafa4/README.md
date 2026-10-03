# Difficulty calibration — gnuplot__gnuplot.a1bafa4

Protocol (frozen before any calibration run):

* **Task revision:** the commit that adds this file (tests, blobs, verifier pin and agent bundle
  are not changed afterwards; the results commit only adds files under `runs/` and this README).
* **Model:** Claude Opus 5.5 (`claude-opus-5-5`), default sampling settings.
* **Agent:** Claude agent with shell + file tools (general-purpose agent), one fresh session per
  run, no memory shared between runs, no internet, workspace = a fresh copy of
  `images/<iid>/task_cleanroom/workspace/` only.
* **Prompt:** `PROMPT.md` (identical for every run; `{WS}` = that run's workspace path).
* **Budget:** single session, instructed to finish within ~90 minutes; no token cap; the
  harness records actual wall time, tokens and tool calls per run.
* **Runs:** 8 independent runs, scored with `programbench eval` on this revision.
* **Reproduction with the Claude Code CLI:** `run_claude_code.sh` (same prompt and budget).

Results: see the results section added after the batch.
