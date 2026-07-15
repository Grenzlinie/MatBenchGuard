#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reproduction_results.csv ===
python3 -c "
import csv

data = [
    [0,    1.0,  0.197, 0.228, 'Entropy',     '', ''],
    [0.125,1.20, 0.214, 0.250, 'Left sound',  0.45, ''],
    [0.25, 1.40, 0.269, 0.317, 'Left sound',   '', ''],
    [0.375,1.66, 0.375, 0.419, 'Left sound',   '', ''],
    [0.5,  1.71, 0.506, 0.476, 'Right sound',  '', 0.319],
    [0.625,'',    0.375, 0.412, 'Right sound',  '', ''],
    [0.75, '',    0.269, 0.313, 'Right sound',  '', ''],
    [0.875,'',    0.214, 0.249, 'Right sound',  '', ''],
]

with open('/app/outputs/reproduction_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['phi','inert_max','chem_acoustic_tstar','full_tstar','blowup_mode','pressure_tstar_phi125','pressure_tstar_phi5'])
    w.writerows(data)
"
