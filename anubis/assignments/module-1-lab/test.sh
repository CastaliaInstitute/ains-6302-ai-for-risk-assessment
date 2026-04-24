#!/usr/bin/env bash
# Local debug runner for this Anubis assignment.
# Place an example student solution in ./student and run:
#   ./test.sh
set -euo pipefail
cd "$(dirname "$0")"
if [[ ! -d student ]]; then
  echo "Expected ./student directory with an example solution." >&2
  exit 2
fi
python pipeline.py
