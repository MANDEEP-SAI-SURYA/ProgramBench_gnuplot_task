#!/usr/bin/env bash
# Reproduce one calibration run with the Claude Code CLI (headless) in the cleanroom image.
#   usage: ./run_claude_code.sh RUN_NAME            (needs docker + an Anthropic API key / Claude login)
# Produces runs/RUN_NAME/{trajectory.jsonl, meta.json, gnuplot__gnuplot.a1bafa4/submission.tar.gz}; score it with
#   cd ../../src && python3 -m programbench eval ../calibration/gnuplot__gnuplot.a1bafa4/runs/RUN_NAME
# Budget (same as the recorded batch): one session, ~90 min wall clock, max 400 turns.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
RUN="$1"; OUT="$HERE/runs/$RUN"; mkdir -p "$OUT/gnuplot__gnuplot.a1bafa4"
IMAGE=programbench/gnuplot_1776_gnuplot.a1bafa4:task_cleanroom_v6
MODEL="${MODEL:-claude-opus-5-5}"
PROMPT="$(sed 's|{WS}|/workspace|g' "$HERE/PROMPT.md")"
START=$(date -u +%FT%TZ)
# The container has no network except the Anthropic API (allow-list it in your proxy/firewall).
docker run --rm -e ANTHROPIC_API_KEY -v "$OUT:/out" "$IMAGE" bash -c "
  npm i -g @anthropic-ai/claude-code >/dev/null 2>&1 || true
  cd /workspace && timeout 5400 claude -p \"\$0\" --model $MODEL --max-turns 400 \
     --dangerously-skip-permissions --output-format stream-json --verbose > /out/trajectory.jsonl
  tar -C /workspace/solution --exclude=executable -czf /out/gnuplot__gnuplot.a1bafa4/submission.tar.gz ." "$PROMPT"
printf '{"run": "%s", "model": "%s", "agent": "claude-code (headless)", "start": "%s", "end": "%s", "wall_clock_budget_s": 5400, "max_turns": 400}\n' \
  "$RUN" "$MODEL" "$START" "$(date -u +%FT%TZ)" > "$OUT/meta.json"
