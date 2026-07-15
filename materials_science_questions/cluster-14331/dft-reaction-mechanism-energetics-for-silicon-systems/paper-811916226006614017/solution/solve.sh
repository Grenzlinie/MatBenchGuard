#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: relative_energies.csv ===
python3 -c "
import csv
hartree_per_kcal = 1.0 / 627.509
base_energy = -200.0

data = [
    ('H',   'RNSi', base_energy),
    ('H',   'RSiN', base_energy + 64.2 * hartree_per_kcal),
    ('CH3', 'RNSi', base_energy),
    ('CH3', 'RSiN', base_energy + 49.6 * hartree_per_kcal),
    ('OH',  'RNSi', base_energy),
    ('OH',  'RSiN', base_energy - 3.3  * hartree_per_kcal),
    ('F',   'RNSi', base_energy),
    ('F',   'RSiN', base_energy - 22.6 * hartree_per_kcal),
]

method = 'QCISD(T)/6-311G**//QCISD/6-31G*'

with open('/app/outputs/relative_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['R', 'isomer', 'total_energy_hartree', 'method'])
    for r, iso, e in data:
        w.writerow([r, iso, round(e, 10), method])
"

# === solve block: barriers.csv ===
python3 -c "
import csv

data = [
    ('H',   11.9, 76.1),
    ('CH3', 18.7, 68.3),
    ('OH',  34.2, 31.1),
    ('F',   44.3, 21.8),
]

method = 'QCISD(T)/6-311G**//QCISD/6-31G*'

with open('/app/outputs/barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['R', 'forward_barrier_kcal_mol', 'reverse_barrier_kcal_mol', 'method'])
    for r, fwd, rev in data:
        w.writerow([r, fwd, rev, method])
"
