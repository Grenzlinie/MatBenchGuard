#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
pip install numpy scipy -i https://pypi.tuna.tsinghua.edu.cn/simple

# === solve block: g_c_values.csv ===
python3 /solution/compute.py > /app/outputs/g_c_values.csv
