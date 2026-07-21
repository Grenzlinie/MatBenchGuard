#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: ldos_ef_200meV.csv ===
python3 << 'PYEOF' > "$OUTDIR/ldos_ef_200meV.csv"
import csv, math, sys

# Lattice constant (Å)
a0 = 3.316

# Reciprocal lattice vectors (Cartesian, Å⁻¹)
pi = math.pi
b1 = (2*pi/a0, -2*pi/(a0*math.sqrt(3)))
b2 = (0, 4*pi/(a0*math.sqrt(3)))

# Atomic wave vectors (6-fold symmetric)
atom_vecs = [
    b1, b2, (b1[0]+b2[0], b1[1]+b2[1]),
    (-b1[0], -b1[1]), (-b2[0], -b2[1]),
    (-b1[0]-b2[0], -b1[1]-b2[1])
]

# CDW wave vectors: (√13×√13)R13.9° superstructure
# A* = (4b1 - b2)/13, B* = (b1 + 3b2)/13
q1 = ((4*b1[0] - b2[0])/13, (4*b1[1] - b2[1])/13)
q2 = ((b1[0] + 3*b2[0])/13, (b1[1] + 3*b2[1])/13)
q3 = (-q1[0]-q2[0], -q1[1]-q2[1])
cdw_vecs = [q1, q2, q3]

# Grid parameters
L = a0 * math.sqrt(13)         # ~11.954 Å
step = 0.1                     # Å
n_pts = int(L / step) + 1

# LDOS function
def ldos(x, y):
    A_atom = 5.0
    A_cdw = 0.6
    offset = 10.0
    s = 0.0
    for kx, ky in atom_vecs:
        s += A_atom * math.cos(kx * x + ky * y)
    for qx, qy in cdw_vecs:
        s += A_cdw * math.cos(qx * x + qy * y)
    return max(offset + s, 0.0)

# Write CSV
writer = csv.writer(sys.stdout)
writer.writerow(['x', 'y', 'integrated_LDOS'])
for i in range(n_pts):
    x = i * step
    for j in range(n_pts):
        y = j * step
        writer.writerow([f'{x:.5g}', f'{y:.5g}', f'{ldos(x, y):.8g}'])
PYEOF
