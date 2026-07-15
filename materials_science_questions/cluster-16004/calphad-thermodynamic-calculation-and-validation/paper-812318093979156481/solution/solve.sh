#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: temperature_shifts.csv ===
#!/bin/bash
set -euo pipefail
python3 <<'PYEOF'
import csv
import math

# ΔP = 690 MPa (the effective pressure used in the paper's calculations)
DP = 689.0

# Define data rows
# Line 1: ΔH = 60000 J/mol
rows_line1 = [
    (673, -1.778),
    (758, -1.719),
    (795, -1.679),
    (813, -1.647),
    (850, -1.598),
]
# Line 2: ΔH = -10550 J/mol
rows_line2 = [
    (920, -0.79),
    (898, -0.84),
    (886, -0.86),
    (873, -0.86),
    (850, -0.89),
]

# Pure Al control: line=0
pure_al = [(933, 0.77, 10500, 0)]

output = []

for line_id, dh, rows in [
    (1, 60000.0, rows_line1),
    (2, -10550.0, rows_line2),
]:
    for t1, dv in rows:
        exponent = (dv * DP) / dh
        t2 = t1 * math.exp(exponent)
        dt = t2 - t1
        output.append({
            'line': line_id,
            'T1_K': t1,
            'delta_V_ml_per_mol': dv,
            'T2_K': round(t2, 1),
            'delta_T_K': round(dt, 1),
        })

# Pure Al row
t1, dv, dh, line_id = pure_al[0]
exponent = (dv * DP) / dh
t2 = t1 * math.exp(exponent)
dt = t2 - t1
output.append({
    'line': line_id,
    'T1_K': t1,
    'delta_V_ml_per_mol': dv,
    'T2_K': round(t2, 1),
    'delta_T_K': round(dt, 1),
})

with open('/app/outputs/temperature_shifts.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['line', 'T1_K', 'delta_V_ml_per_mol', 'T2_K', 'delta_T_K'])
    writer.writeheader()
    writer.writerows(output)
PYEOF
