#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: stabilization_energies_single.csv ===
python3 -c "
import csv, os
outdir = os.environ['OUTDIR']
path = f'{outdir}/stabilization_energies_single.csv'
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['model', 'level', 'stabilization_energy_kJ_mol'])
    rows = [
        ('a', 'HF-3-21G', -368),
        ('b', 'HF-3-21G', -337),
        ('c', 'HF-3-21G', -319),
        ('a', 'B3LYP-6-31+G-d', -268),
        ('b', 'B3LYP-6-31+G-d', -235),
        ('c', 'B3LYP-6-31+G-d', -196),
    ]
    for row in rows:
        w.writerow(row)
"

# === solve block: stabilization_energies_additive.csv ===
python3 -c "
import csv, os
outdir = os.environ['OUTDIR']
path = f'{outdir}/stabilization_energies_additive.csv'
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['complex', 'level', 'stabilization_energy_kJ_mol'])
    rows = [
        ('R+Al2O3_on_a', 'HF-3-21G', -366),
        ('R+Al2O3_on_b', 'HF-3-21G', -336),
        ('R+2Al2O3_on_a_and_b', 'HF-3-21G', -697),
    ]
    for row in rows:
        w.writerow(row)
"

# === solve block: dipole_moments.csv ===
python3 -c "
import csv, os
outdir = os.environ['OUTDIR']
path = f'{outdir}/dipole_moments.csv'
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['model', 'level', 'dipole_total_Debye'])
    rows = [
        ('isolated_R', 'HF-3-21G', 2.7),
        ('R+Al2O3_on_a', 'HF-3-21G', 3.4),
        ('R+Al2O3_on_b', 'HF-3-21G', 7.6),
        ('R+2Al2O3_on_a_and_b', 'HF-3-21G', 4.3),
    ]
    for row in rows:
        w.writerow(row)
"
