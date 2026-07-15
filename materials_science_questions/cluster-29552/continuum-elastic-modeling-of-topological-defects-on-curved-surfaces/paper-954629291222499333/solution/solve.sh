#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
chmod +x /solution/generate.py

# === solve block: defect_analysis.csv ===
python3 /solution/generate.py --basename defect_analysis.csv > /app/outputs/defect_analysis.csv

# === solve block: stress_drop_predictions.csv ===
python3 /solution/generate.py --basename stress_drop_predictions.csv > /app/outputs/stress_drop_predictions.csv

# === solve block: summary_metrics.json ===
python3 /solution/generate.py --basename summary_metrics.json > /app/outputs/summary_metrics.json
