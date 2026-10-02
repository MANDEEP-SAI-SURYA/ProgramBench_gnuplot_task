#!/usr/bin/env bash
# Run from /workspace (the directory that contains ./executable).
set -u
cd "$(dirname "$0")/.."
TIMEOUT_ARGS=""
if python3 -c "import pytest_timeout" 2>/dev/null; then TIMEOUT_ARGS="--timeout=60 --timeout-method=thread"; fi
XDIST_ARGS=""
if python3 -c "import xdist" 2>/dev/null; then XDIST_ARGS="-n auto"; fi
python3 -m pytest eval/tests -v -p no:cacheprovider --rootdir="$PWD" \
  --junitxml=eval/results.xml -o junit_family=xunit1 $TIMEOUT_ARGS $XDIST_ARGS
exit 0
