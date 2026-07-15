#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: results_maxdeltaT.csv ===
python3 /solution/compute.py maxdeltaT /app/outputs/results_maxdeltaT.csv

# === solve block: results_maxheatload.csv ===
python3 /solution/compute.py maxheatload /app/outputs/results_maxheatload.csv

# === solve block: example_F7_curve.csv ===
python3 /solution/compute.py example_curve /app/outputs/example_F7_curve.csv

# === solve block: example_max_delta_T.json ===
python3 /solution/compute.py example_max /app/outputs/example_max_delta_T.json
