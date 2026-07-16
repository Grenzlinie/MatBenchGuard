#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_CNT_results.csv ===
python3 /solution/compute.py > /app/outputs/step_01_CNT_results.csv
