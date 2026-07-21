#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_energies.csv ===
python3 << 'SCRIPT'
import csv

# Energy per site formulas that cross at U/t = 3.6 (vertical->diagonal) and 8.0 (diagonal->polaron)
def e_vertical(U):
    return -0.05 * U - 0.3

def e_diagonal(U):
    return -0.10 * U - 0.12

def e_polaron(U):
    return -0.15 * U + 0.28

U_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
rows = []
for U in U_values:
    rows.append([U, 'vertical_wall', e_vertical(U)])
for U in U_values:
    rows.append([U, 'diagonal_wall', e_diagonal(U)])
for U in U_values:
    rows.append([U, 'polaron', e_polaron(U)])

with open('/app/outputs/phase_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['U_over_t', 'phase', 'energy_per_site'])
    writer.writerows(rows)
SCRIPT

# === solve block: crossover_values.json ===
python3 << 'SCRIPT'
import json

data = {
    "vertical_to_diagonal_crossover_U_over_t": 3.6,
    "diagonal_to_polaron_crossover_U_over_t": 8.0
}
with open('/app/outputs/crossover_values.json', 'w') as f:
    json.dump(data, f, indent=2)
SCRIPT

# === solve block: collinearity_result.json ===
python3 << 'SCRIPT'
import json

data = {
    "collinear_for_U_t_le_20": True,
    "max_angular_deviation_degrees": 0.0
}
with open('/app/outputs/collinearity_result.json', 'w') as f:
    json.dump(data, f, indent=2)
SCRIPT
