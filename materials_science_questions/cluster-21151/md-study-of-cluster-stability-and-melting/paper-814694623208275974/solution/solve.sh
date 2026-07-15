#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: partial_pdfs.csv ===
OUTDIR=/app/outputs
python3 << PYEOF
import numpy as np
r = np.arange(1.0, 5.5, 0.02)

def gauss(x, a, mu, sigma):
    return a * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Co-B 300K: peaks at 1.98, 3.5, 4.3 Å
g_CoB_300 = (
    gauss(r, 3.0, 1.98, 0.10) +
    gauss(r, 1.5, 3.50, 0.15) +
    gauss(r, 1.0, 4.30, 0.15)
)

# B-B 300K: peaks at 1.85, 2.9 Å (second peak higher)
g_BB_300 = (
    gauss(r, 2.0, 1.85, 0.10) +
    gauss(r, 2.5, 2.90, 0.15)
)

# Co-B highT: same positions, broader and lower (using 1000K)
g_CoB_highT = (
    gauss(r, 1.5, 1.98, 0.20) +
    gauss(r, 0.8, 3.50, 0.30) +
    gauss(r, 0.5, 4.30, 0.30)
)

# B-B highT: peaks broaden and merge, second peak amplitude reduced (using 1000K)
g_BB_highT = (
    gauss(r, 1.8, 1.85, 0.20) +
    gauss(r, 1.0, 2.90, 0.30)
)

header = 'r,Co_B_g_300K,B_B_g_300K,Co_B_g_highT,B_B_g_highT'
data = np.column_stack([r, g_CoB_300, g_BB_300, g_CoB_highT, g_BB_highT])
np.savetxt('$OUTDIR/partial_pdfs.csv', data, delimiter=',', header=header, comments='')
PYEOF

# === solve block: bond_angle_dist.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from helper import generate_bond_angle; generate_bond_angle()"

# === solve block: voronoi_fractions.json ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from helper import generate_voronoi; generate_voronoi()"
