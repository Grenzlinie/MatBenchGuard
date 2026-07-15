#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: enthalpy_entropy_Y04Bi06VO4.csv ===
python3 /solution/calc.py Y04Bi06VO4 /tmp/temp_Y04.csv && python3 -c "
import csv
with open('/tmp/temp_Y04.csv') as f, open('$OUTDIR/enthalpy_entropy_Y04Bi06VO4.csv', 'w', newline='') as out:
    reader = csv.DictReader(f)
    writer = csv.DictWriter(out, fieldnames=['T (K)', 'Cp (J/(mol·K))', 'delta_H (kJ/mol)', 'delta_S (J/(mol·K))', 'Phi (J/(mol·K))'])
    writer.writeheader()
    for row in reader:
        T = float(row['T (K)'])
        dH = float(row['delta_H (kJ/mol)'])
        dS = float(row['delta_S (J/(mol·K))'])
        dH_J = dH * 1000
        Phi = dS - dH_J / T
        row['Phi (J/(mol·K))'] = round(Phi, 2)
        writer.writerow(row)
"

# === solve block: enthalpy_entropy_Y06Bi04VO4.csv ===
python3 /solution/calc.py Y06Bi04VO4 /app/outputs/enthalpy_entropy_Y06Bi04VO4.csv
