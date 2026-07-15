#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: stress_relaxation_force.csv ===
python3 /solution/simulate.py --mode stress_relaxation --output /app/outputs/stress_relaxation_force.csv

# === solve block: cyclic_loading_force.csv ===
python3 /solution/simulate.py --mode cyclic --output /app/outputs/cyclic_loading_force.csv
