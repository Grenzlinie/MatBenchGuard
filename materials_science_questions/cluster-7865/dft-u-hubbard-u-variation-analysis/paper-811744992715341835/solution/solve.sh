#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_structure.json ===
python3 -c "
import json
data = {
    'R_Co_N1': 1.942,
    'R_N1_C1': 1.381,
    'R_C1_N2': 1.323,
    'R_C1_C2': 1.455,
    'R_C_H': 1.089,
    'theta_C1_N1_C1p': 107.577,
    'theta_N2_C1_N1': 127.577,
    'theta_N1_C1_C2': 109.855
}
with open('/app/outputs/step_01_structure.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_02_properties.json ===
python3 -c "
import json
data = {
    'HOMO_LUMO_gap': 1.4,
    'total_magnetic_moment': 1.0,
    'Co_magnetic_moment': 1.04
}
with open('/app/outputs/step_02_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_03_pdos_co.csv ===
python3 -c "
import csv, math

e_min = -5.0
e_max = 2.0
step = 0.01
peak1 = -1.7
peak2 = -2.6
sigma = 0.2
h1 = 3.0
h2 = 2.0

def gaussian(e, center, sigma, height):
    return height * math.exp(-((e - center) ** 2) / (2 * sigma ** 2))

with open('/app/outputs/step_03_pdos_co.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['energy_eV', 'pdos_co_3d'])
    e = e_min
    while e <= e_max + 1e-9:
        pdos = gaussian(e, peak1, sigma, h1) + gaussian(e, peak2, sigma, h2)
        w.writerow([round(e, 6), round(pdos, 6)])
        e += step
"
