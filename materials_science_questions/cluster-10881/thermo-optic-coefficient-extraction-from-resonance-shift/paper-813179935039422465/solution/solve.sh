#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"
python3 /solution/generate.py

# === solve block: steady_state_results.csv ===
# file already written by preamble
test -f "/app/outputs/steady_state_results.csv" || exit 1

# === solve block: cutoff_frequency.txt ===
# file already written by preamble
test -f "/app/outputs/cutoff_frequency.txt" || exit 1
