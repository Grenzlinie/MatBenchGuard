#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: step_01_rhs_curve.csv ===
python3 /solution/generate_curve.py "/app/outputs/step_01_rhs_curve.csv"

# === solve block: step_02_critical_sizes.json ===
python3 /solution/compute_critical.py "/app/outputs/step_01_rhs_curve.csv" "/app/outputs/step_02_critical_sizes.json"
