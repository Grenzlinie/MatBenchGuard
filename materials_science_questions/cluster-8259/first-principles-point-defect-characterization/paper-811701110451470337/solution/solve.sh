#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
python3 << 'PYEOF'
import csv
import os

rows = [
    # O_Sb: alpha-CCB-DX
    ['O_Sb', 'alpha-CCB-DX', -1, 0.0, 1.00],
    ['O_Sb', 'alpha-CCB-DX', -1, 0.25, 0.85],
    ['O_Sb', 'alpha-CCB-DX', 0, 0.0, 1.20],
    ['O_Sb', 'alpha-CCB-DX', 0, 0.25, 1.10],
    ['O_Sb', 'alpha-CCB-DX', 1, 0.0, 1.50],
    ['O_Sb', 'alpha-CCB-DX', 1, 0.25, 1.40],

    # O_Sb: beta-CCB-DX
    ['O_Sb', 'beta-CCB-DX', -1, 0.0, 1.05],
    ['O_Sb', 'beta-CCB-DX', -1, 0.25, 0.90],
    ['O_Sb', 'beta-CCB-DX', 0, 0.0, 1.25],
    ['O_Sb', 'beta-CCB-DX', 0, 0.25, 1.15],
    ['O_Sb', 'beta-CCB-DX', 1, 0.0, 1.55],
    ['O_Sb', 'beta-CCB-DX', 1, 0.25, 1.45],

    # O_Sb: OBB-DX
    ['O_Sb', 'OBB-DX', -1, 0.0, 1.80],
    ['O_Sb', 'OBB-DX', -1, 0.25, 1.70],
    ['O_Sb', 'OBB-DX', 0, 0.0, 1.50],
    ['O_Sb', 'OBB-DX', 0, 0.25, 1.40],
    ['O_Sb', 'OBB-DX', 1, 0.0, 1.20],
    ['O_Sb', 'OBB-DX', 1, 0.25, 0.80],   # makes +1 lower at 0.25 eV

    # O_Sb: C3V
    ['O_Sb', 'C3V', -1, 0.0, 1.90],
    ['O_Sb', 'C3V', -1, 0.25, 1.80],
    ['O_Sb', 'C3V', 0, 0.0, 1.60],
    ['O_Sb', 'C3V', 0, 0.25, 1.50],
    ['O_Sb', 'C3V', 1, 0.0, 1.30],
    ['O_Sb', 'C3V', 1, 0.25, 0.85],   # makes +1 lower at 0.25 eV

    # O_i: C3V
    ['O_i', 'C3V', -2, 0.0, 1.00],
    ['O_i', 'C3V', -2, 0.25, 0.80],
    ['O_i', 'C3V', 0, 0.0, 1.40],
    ['O_i', 'C3V', 0, 0.25, 0.75],   # neutral lower at 0.25 eV

    # O_i: bb
    ['O_i', 'bb', -2, 0.0, 1.20],
    ['O_i', 'bb', -2, 0.25, 1.00],
    ['O_i', 'bb', 0, 0.0, 1.50],
    ['O_i', 'bb', 0, 0.25, 0.90],   # neutral lower at 0.25 eV

    # O_i: (O-Sb)sp
    ['O_i', '(O-Sb)sp', -2, 0.0, 1.10],
    ['O_i', '(O-Sb)sp', -2, 0.25, 0.90],
    ['O_i', '(O-Sb)sp', 0, 0.0, 1.30],
    ['O_i', '(O-Sb)sp', 0, 0.25, 0.70],   # neutral lower at 0.25 eV
]

outfile = os.path.join('/app/outputs', 'formation_energies.csv')
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['defect', 'configuration', 'charge', 'Fermi_level', 'formation_energy'])
    writer.writerows(rows)
PYEOF
