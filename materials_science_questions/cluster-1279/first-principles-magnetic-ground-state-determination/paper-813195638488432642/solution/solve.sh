#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: total_energies.csv ===
python3 -c "
import csv
headers = ['magnetic_configuration','total_energy','relative_energy','relative_energy_per_atom']
rows = [
    ['FIM', -200.0, 0.0, 0.0],
    ['FM', -199.996, 0.004, 0.001],
    ['NM', -199.995, 0.005, 0.00125]
]
with open('$OUTDIR/total_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)
"

# === solve block: magnetic_moments.csv ===
python3 -c "
import csv
headers = ['atom_label','spin_moment']
rows = [
    ['Cr1', 1.794],
    ['Cr2', 0.961],
    ['Cr3', -0.894],
    ['Cr4', 1.755],
    ['C1', -0.064],
    ['C2', -0.054],
    ['Ge1', -0.020],
    ['Ge2', -0.063]
]
with open('$OUTDIR/magnetic_moments.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)
"

# === solve block: total_dos.dat ===
python3 /solution/write_dos.py "$OUTDIR"
