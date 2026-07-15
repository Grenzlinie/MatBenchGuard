#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# Install required packages (Tsinghua mirror)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_stress_strain.csv ===
sed -i 's/math\.log(1 - xi + math\.exp(-7))/math.log(max(1e-12, 1 - xi + math.exp(-7)))/g' /solution/simulate.py
python3 /solution/simulate.py
[ -f step_01_stress_strain.csv ] && mv step_01_stress_strain.csv "$OUTDIR/"

# === solve finalize ===
# No extra finalize steps
