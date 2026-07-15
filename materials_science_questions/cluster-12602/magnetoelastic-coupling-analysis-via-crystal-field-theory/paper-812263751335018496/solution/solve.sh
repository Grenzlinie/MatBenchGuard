#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/compute.py

# === solve block: cef_levels.json ===
echo "cef_levels.json written by compute.py"

# === solve block: c55_curve.csv ===
echo "c55_curve.csv written by compute.py"
