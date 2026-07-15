#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: reorientation_K2_0.2_T100.csv ===
python3 /solution/gf_solver.py reorientation_K2_0.2_T100.csv 2.5 0.2 100 25

# === solve block: reorientation_K2_0.5_T4.9.csv ===
python3 /solution/gf_solver.py reorientation_K2_0.5_T4.9.csv 1.5 0.5 4.9 25
