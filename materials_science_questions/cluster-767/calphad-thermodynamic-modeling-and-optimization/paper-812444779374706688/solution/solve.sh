#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: step_01_binary_eutectic.csv ===
python3 -c "
import csv
with open('$OUTDIR/step_01_binary_eutectic.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['eutectic_temperature_K', 'eutectic_Zn_mole_fraction'])
    w.writerow([464.0, 0.16])
"

# === solve block: step_01_ternary_liquidus.csv ===
python3 /solution/helper.py ternary
