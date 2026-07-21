#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: testing_predictions.csv ===
python3 /solution/generate.py --csv --out /app/outputs/testing_predictions.csv

# === solve block: final_metrics.json ===
python3 /solution/generate.py --json --out /app/outputs/final_metrics.json
