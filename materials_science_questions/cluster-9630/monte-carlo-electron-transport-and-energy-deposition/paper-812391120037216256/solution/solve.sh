#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: absolute_values.json ===
python3 -c "
import json
data = {
    'H+': {'gamma_B': 0.12, 'dE_dx': 0.00866},
    'C6+': {'gamma_B': 3.6, 'dE_dx': 0.307},
    'Ca20+': {'gamma_B': 32.1, 'dE_dx': 2.88},
    'Ni27+': {'gamma_B': 45.0, 'dE_dx': 5.13},
    'Mo39+': {'gamma_B': 82.3, 'dE_dx': 9.91}
}
with open('/app/outputs/absolute_values.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: normalized_ratios.csv ===
python3 -c "
import csv
gamma_C = 3.6
dedx_C = 0.307
data = {
    'H+':  {'Q':1, 'gamma':0.12, 'dedx':0.00866},
    'C6+': {'Q':6, 'gamma':3.6, 'dedx':0.307},
    'Ca20+': {'Q':20, 'gamma':32.1, 'dedx':2.88},
    'Ni27+': {'Q':27, 'gamma':45.0, 'dedx':5.13},
    'Mo39+': {'Q':39, 'gamma':82.3, 'dedx':9.91}
}
rows = []
for ion, vals in data.items():
    Q_P = vals['Q']
    R_gamma = 36 * vals['gamma'] / (Q_P**2 * gamma_C)
    R_dE_dx = 36 * vals['dedx'] / (Q_P**2 * dedx_C)
    rows.append([Q_P, round(R_gamma, 6), round(R_dE_dx, 6)])
with open('/app/outputs/normalized_ratios.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Q_P', 'R_gamma', 'R_dE_dx'])
    writer.writerows(rows)
"
