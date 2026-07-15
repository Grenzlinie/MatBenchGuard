#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# No additional setup required; python3 standard library only.

# === solve block: eliashberg_functions.csv ===
python3 /solution/helper.py csv

# === solve block: peak_positions.json ===
python3 /solution/helper.py json
