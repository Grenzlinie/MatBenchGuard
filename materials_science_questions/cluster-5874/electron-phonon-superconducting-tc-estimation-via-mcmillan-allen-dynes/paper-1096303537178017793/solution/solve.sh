#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: tc_vs_b0.csv ===
python3 /solution/helper.py --output tc_vs_b0.csv
