#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: nematic_phase_map.csv ===
cat << 'PYEOF' > /solution/nematic_phase_map.py
import csv, math

delta1_start = 0.5
delta1_end = 1.5
delta2_start = 0.0
delta2_end = 1.0
step = 0.005

eps = 1e-9

rows = []
d1 = delta1_start
while d1 <= delta1_end + eps:
    d2 = delta2_start
    while d2 <= delta2_end + eps:
        # Determine phase from analytic boundaries given in the paper
        if d1 <= (1 + d2) / 2 + eps:
            phase = 'N1'
        elif d1 >= 1 - eps:
            phase = 'N2'
        else:
            phase = 'N_angle'
        rows.append([d1, d2, phase])
        d2 += step
    d1 += step

with open('/app/outputs/nematic_phase_map.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['delta1', 'delta2', 'phase'])
    w.writerows(rows)
PYEOF
mkdir -p /app/outputs
python3 /solution/nematic_phase_map.py

# === solve block: ferro_phase_check.json ===
python3 /solution/run.py ferro

# === solve block: magnon_gap_check.json ===
python3 /solution/run.py magnon
