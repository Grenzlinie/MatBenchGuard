#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: step_01_order_parameters.csv ===
python3 /solution/solve_equations.py /app/outputs/step_01_order_parameters.csv

# === solve block: step_02_transition_temperatures.csv ===
python3 /solution/find_transitions.py /app/outputs/step_01_order_parameters.csv /app/outputs/step_02_transition_temperatures.csv
