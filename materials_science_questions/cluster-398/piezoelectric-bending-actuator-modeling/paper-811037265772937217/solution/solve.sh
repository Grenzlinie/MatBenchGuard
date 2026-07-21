#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bimorph_deflections.csv ===
python3 << 'PYEOF'
import csv
import math
import os

E1 = 0.2e10
# N/m²
e31 = 0.046
# C/m²
t = 0.5e-3
# m total thickness

voltages = [1, 50, 100, 150, 200]
positions = [0.02, 0.04, 0.06, 0.08, 0.10]

def deflection(V, x):
    return 0.375 * e31 * V / E1 * (x / t) ** 2

# Compute all values into a dict keyed by x then V
rows = []
for x in positions:
    row = {
        'distance_m': f'{x:.2f}',
        'deflection_unit_voltage_m': f'{deflection(1, x):.4e}',
        'deflection_50V_m': f'{deflection(50, x):.4e}',
        'deflection_100V_m': f'{deflection(100, x):.4e}',
        'deflection_150V_m': f'{deflection(150, x):.4e}',
        'deflection_200V_m': f'{deflection(200, x):.4e}'
    }
    rows.append(row)

fieldnames = ['distance_m', 'deflection_unit_voltage_m', 'deflection_50V_m',
              'deflection_100V_m', 'deflection_150V_m', 'deflection_200V_m']

out_file = '/app/outputs/bimorph_deflections.csv'
with open(out_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
PYEOF
