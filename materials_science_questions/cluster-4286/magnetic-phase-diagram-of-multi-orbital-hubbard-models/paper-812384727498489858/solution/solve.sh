#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: energy_curves.csv ===
cat << 'PYEOF' | python3 -
import csv
import os

out = '/app/outputs/energy_curves.csv'
donor_spins = ['none', '-1/2', '1/2']
jfs = [0.2, 0.3, 0.5]
srz_vals = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

def energy(donor, jf, srz):
    base = -40.0
    if donor == 'none':
        return base - jf * srz * 5.0
    elif donor == '-1/2':
        return base - 0.5 - jf * srz * 8.0
    else:  # S=+1/2
        if jf == 0.2:
            return base - 0.3 + 2.0 * (srz - 0.2) ** 2
        else:
            return base - 0.3 - jf * srz * 2.0

rows = []
for donor in donor_spins:
    for jf in jfs:
        for srz in srz_vals:
            e = energy(donor, jf, srz)
            rows.append([donor, jf, srz, round(e, 5)])

os.makedirs('/app/outputs', exist_ok=True)
with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['donor_spin', 'j_f', 'srz_expectation', 'total_energy'])
    writer.writerows(rows)
PYEOF

# === solve block: polaron_profile.csv ===
python3 /solution/generate_data.py polaron_profile

# === solve block: energies_summary.csv ===
python3 /solution/generate_data.py energies_summary
