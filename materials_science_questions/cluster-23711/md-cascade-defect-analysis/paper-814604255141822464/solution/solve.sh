#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: excess_energy_profile.csv ===
python3 <<'PYEOF'
import math

L = 1000.0              # grain size in nm
A = 0.7778              # peak amplitude
lam = 23.074            # decay length (nm)

def deltaE(x):
    """Excess energy at position x (nm) from left GB."""
    if x < 0 or x > L:
        return 0.0
    return A * (math.exp(-x / lam) + math.exp(-(L - x) / lam))

with open('/app/outputs/excess_energy_profile.csv', 'w') as f:
    f.write('x_nm,DeltaE_eV_per_atom\n')
    for i in range(0, int(L) + 1):   # 0 to 1000 nm inclusive
        x = float(i)
        val = deltaE(x)
        f.write(f'{x},{val:.8f}\n')
PYEOF

# === solve block: distances.json ===
python3 <<'PYEOF'
import csv

xs = []
ys = []
with open('/app/outputs/excess_energy_profile.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        xs.append(float(row[0]))
        ys.append(float(row[1]))

def find_first_below(xs, ys, thresh):
    for x, y in zip(xs, ys):
        if y < thresh:
            return x
    return None

d_amorph = find_first_below(xs, ys, 0.6)
d_half   = find_first_below(xs, ys, 0.3)

import json
with open('/app/outputs/distances.json', 'w') as f:
    json.dump({
        'distance_to_amorphization_nm': d_amorph,
        'distance_to_half_amorphization_nm': d_half
    }, f)
PYEOF
