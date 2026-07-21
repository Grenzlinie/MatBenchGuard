#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: best_ann_results.csv ===
python3 /solution/generate_best_ann.py /app/outputs/best_ann_results.csv
