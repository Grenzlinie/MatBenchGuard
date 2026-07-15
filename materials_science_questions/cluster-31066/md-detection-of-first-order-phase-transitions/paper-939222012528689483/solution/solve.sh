#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: mu_1_0_K.csv ===
python3 /solution/dh_solver_and_classify.py 1.0 /app/outputs/mu_1_0_K.csv

# === solve block: mu_1_5_K.csv ===
python3 /solution/dh_solver_and_classify.py 1.5 /app/outputs/mu_1_5_K.csv

# === solve block: mu_1_8_K.csv ===
python3 /solution/dh_solver_and_classify.py 1.8 /app/outputs/mu_1_8_K.csv

# === solve block: classification.json ===
python3 /solution/dh_solver_and_classify.py classify /app/outputs
