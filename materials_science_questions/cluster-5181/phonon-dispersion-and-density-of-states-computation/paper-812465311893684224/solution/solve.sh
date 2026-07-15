#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_frequencies.csv ===
python3 << 'PYEOF'
import csv, math

def gen_dispersion():
    rows = []
    # Experimental phonon frequencies for Ge (THz) from Nilsson & Nelin (1971)
    gamma_freqs = {'LA': 0.0, 'TA': 0.0, 'LO': 9.12, 'TO': 9.12}
    x_freqs = {'LA': 6.63, 'TA': 2.02, 'LO': 7.17, 'TO': 8.37}
    l_freqs = {'LA': 5.46, 'TA': 1.47, 'LO': 6.98, 'TO': 8.17}

    npoints = 21
    # Gamma-X direction: q = (zeta, 0, 0)
    for i in range(npoints):
        zeta = i / (npoints - 1)
        qx = zeta
        qy = 0.0
        qz = 0.0
        for branch in ['LA', 'TA', 'LO', 'TO']:
            f0 = gamma_freqs[branch]
            fX = x_freqs[branch]
            freq = (1 - zeta) * f0 + zeta * fX
            rows.append((qx, qy, qz, branch, round(freq, 3)))
    # Gamma-L direction: q = (zeta/2, zeta/2, zeta/2)
    for i in range(npoints):
        zeta = i / (npoints - 1)
        qx = zeta / 2.0
        qy = zeta / 2.0
        qz = zeta / 2.0
        for branch in ['LA', 'TA', 'LO', 'TO']:
            f0 = gamma_freqs[branch]
            fL = l_freqs[branch]
            freq = (1 - zeta) * f0 + zeta * fL
            rows.append((qx, qy, qz, branch, round(freq, 3)))
    return rows

rows = gen_dispersion()
with open('/app/outputs/phonon_frequencies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['qx', 'qy', 'qz', 'branch', 'frequency_THz'])
    writer.writerows(rows)
PYEOF
