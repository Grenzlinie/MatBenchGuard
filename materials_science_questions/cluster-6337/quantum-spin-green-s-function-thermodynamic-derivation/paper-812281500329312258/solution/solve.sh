#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"

# === solve block: L_functions.csv ===
python3 /solution/compute.py L_functions

# === solve block: critical_point.txt ===
python3 /solution/compute.py critical_point
