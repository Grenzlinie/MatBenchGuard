#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy
python3 /solution/compute.py

# === solve block: gq_vs_energy.csv ===
cp /tmp/gq_vs_energy.csv /app/outputs/gq_vs_energy.csv

# === solve block: line_shapes.csv ===
cp /tmp/line_shapes.csv /app/outputs/line_shapes.csv
