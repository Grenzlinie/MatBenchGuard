#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: stability_output.csv ===
python3 /solution/compute.py --mode stability --output /app/outputs/stability_output.csv

# === solve block: correlation_C12.csv ===
python3 /solution/compute.py --mode correlation --output /app/outputs/correlation_C12.csv
