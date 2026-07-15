#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 /solution/generate_all.py

# === solve block: potential_energy_ratio.csv ===
python3 << 'EOF' || { echo "ERROR: potential_energy_ratio generation failed"; exit 1; }
import os, csv, math
out_dir = os.environ.get('OUTDIR', '/app/outputs')
path = os.path.join(out_dir, 'potential_energy_ratio.csv')

# Best-fit T0* from the paper (Fig.3 caption / Sec.V)
T0 = {3: 0.340, 4: 0.350, 5: 0.380, 7: 0.417}
# 10 temperatures in [0.42, 0.71]
temps = [round(0.42 + i*(0.71-0.42)/9, 3) for i in range(10)]

def ratio(g, T_star):
    t0 = T0[g]
    eta = (t0 / T_star)**0.5 * math.exp(1.0/t0 - 1.0/T_star)
    num = 0.0
    den = 0.0
    for k in range(2*g - 5 + 1):   # k = 0 .. 2g-5
        ek = eta**k
        num += (3*g - 6 - k) * ek
        den += ek
    return num / ((g-1) * den)

rows = [[g, T, ratio(g, T)] for g in (3,4,5,7) for T in temps]
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['g', 'T_star', 'ratio'])
    w.writerows(rows)
EOF

# === solve block: transition_temperatures.csv ===
:

# === solve block: single_chain_probability.csv ===
:

# === solve block: rdf_g6.csv ===
:
