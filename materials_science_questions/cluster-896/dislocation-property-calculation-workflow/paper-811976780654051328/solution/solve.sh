#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: honeycomb_f_of_x.csv ===
python3 /solution/compute.py --csv /app/outputs/honeycomb_f_of_x.csv

# === solve block: critical_angle.txt ===
python3 /solution/compute.py --txt /app/outputs/critical_angle.txt
