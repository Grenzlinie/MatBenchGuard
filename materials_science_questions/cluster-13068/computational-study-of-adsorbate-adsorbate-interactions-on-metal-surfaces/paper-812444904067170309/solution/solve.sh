#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_sigma.csv ===
python3 /solution/compute.py --output /app/outputs/step_01_sigma.csv

# === solve block: step_02_phase_shift.txt ===
python3 /solution/compute.py --output /app/outputs/step_02_phase_shift.txt

# === solve block: step_03_interaction_energy.csv ===
python3 /solution/compute.py --output /app/outputs/step_03_interaction_energy.csv
