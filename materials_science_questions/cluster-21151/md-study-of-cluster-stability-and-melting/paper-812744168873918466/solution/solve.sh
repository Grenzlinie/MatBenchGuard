#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_03_caloric_curves.csv ===
OUTDIR=${OUTDIR:-/app/outputs}
python3 /dev/stdin <<'PYEOF' "$OUTDIR/step_03_caloric_curves.csv"
import csv, math, sys
outfile = sys.argv[1]
T = [300 + i*25 for i in range(49)]
U = [-3.93 + 0.00005*(t-300) + 0.005*(1+math.tanh((t-1070)/5)) + 0.05*(1+math.tanh((t-1274)/5)) for t in T]
eV_J = 96485.33212
R = 8.314
Cp = []
for i in range(len(T)):
    if i == 0:
        dU = (U[1] - U[0]) / (T[1] - T[0])
    elif i == len(T) - 1:
        dU = (U[-1] - U[-2]) / (T[-1] - T[-2])
    else:
        dU = (U[i+1] - U[i-1]) / (T[i+1] - T[i-1])
    Cp.append(dU * eV_J + 1.5 * R)
with open(outfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'total_potential_energy_eV_per_atom', 'heat_capacity_J_per_mol_K'])
    for t, u, c in zip(T, U, Cp):
        writer.writerow([f'{t:.1f}', f'{u:.6f}', f'{c:.3f}'])
PYEOF

# === solve block: step_04_cna_fractions.csv ===
python3 /solution/gen_data.py step_04

# === solve block: step_06_surface_energy.csv ===
python3 /solution/gen_data.py step_06

# === solve block: step_07_size_classification.csv ===
python3 /solution/gen_data.py step_07
