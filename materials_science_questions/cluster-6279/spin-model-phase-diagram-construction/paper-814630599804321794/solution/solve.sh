#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: order_parameters.csv ===
python3 /solution/generate_order_parameters.py

# === solve block: phase_boundary.csv ===
python3 /solution/generate_phase_boundary.py

# === solve block: critical_temp_anisotropy.csv ===
python3 /solution/generate_critical_temp.py
