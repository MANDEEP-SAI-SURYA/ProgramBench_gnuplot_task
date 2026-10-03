#!/usr/bin/env bash
# Run from /workspace (the directory that contains ./executable).
# Verifier is pinned: pytest==9.1.1. Any other version is refused so results stay reproducible
# (set PROGRAMBENCH_ALLOW_PYTEST_MISMATCH=1 only for debugging).
set -u
cd "$(dirname "$0")/.."
PINNED=9.1.1
FOUND=$(python3 -c "import pytest; print(pytest.__version__)" 2>/dev/null || echo none)
if [ "$FOUND" != "$PINNED" ] && [ -z "${PROGRAMBENCH_ALLOW_PYTEST_MISMATCH:-}" ]; then
  echo "verifier error: pytest==$PINNED required, found $FOUND (pip install pytest==$PINNED)" >&2
  exit 3
fi
python3 -m pytest eval/tests -v -p no:cacheprovider --rootdir="$PWD" \
  --junitxml=eval/results.xml -o junit_family=xunit1
exit 0
