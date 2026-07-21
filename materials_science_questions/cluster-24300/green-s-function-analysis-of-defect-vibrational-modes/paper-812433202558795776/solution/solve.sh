#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: localized_frequencies.csv ===
python3 << 'EOF_SCRIPT' 2>/dev/null
import csv, math, os, numpy as np

outdir = os.environ.get('OUTDIR', '/app/outputs')

# Physical constants (CGS)
r0_cm = 2.282e-8
e_esu = 4.803e-10
alpha = 1.7627
K_bulk = 1.441e11
amu_to_g = 1.660539e-24

# Host short-range parameters A and B
A = 3.0 * r0_cm * K_bulk * (8.0 * r0_cm**3 / e_esu**2) + 2.0 * alpha / (3.0 * math.sqrt(3.0))
B = -alpha / (3.0 * math.sqrt(3.0))

e2 = e_esu * e_esu
pref_short = e2 / (8.0 * r0_cm**3)

# Masses
m_Cs = 132.9 * amu_to_g

# Position vectors (unit cell direction cosines)
sigs = [
    ( 0,  0,  0),       # 0 central impurity
    ( 1,  1,  1),       # 1
    (-1, -1, -1),       # 2
    (-1,  1,  1),       # 3
    ( 1, -1, -1),       # 4
    ( 1, -1,  1),       # 5
    (-1,  1, -1),       # 6
    ( 1,  1, -1),       # 7
    (-1, -1,  1),       # 8
]
pos = [[x * r0_cm for x in s] for s in sigs]

# Charges: -1 for central impurity, +1 for neighbours
q = [-1, 1, 1, 1, 1, 1, 1, 1, 1]

# A' sweep and impurities
A_primes = [4.7452, 4.0, 3.0, 2.0, 1.0, 0.5]
impurities = [('H', 1.0), ('D', 2.0)]   # name, mass in amu

rows = []
for A_prime in A_primes:
    for imp_name, mass_amu in impurities:
        M0 = mass_amu * amu_to_g
        masses = [M0] + [m_Cs] * 8
        D = np.zeros((27, 27))

        # Coulomb contributions for all distinct pairs
        for i in range(9):
            for j in range(i+1, 9):
                inv_sqrt_m = 1.0 / math.sqrt(masses[i] * masses[j])
                rvec = [pos[j][k] - pos[i][k] for k in range(3)]
                dist2 = sum(x*x for x in rvec)
                dist = math.sqrt(dist2)
                dist3 = dist**3
                dist5 = dist**5
                fact = q[i] * q[j] * e2
                for a in range(3):
                    for b in range(3):
                        val = -inv_sqrt_m * (fact * rvec[a]*rvec[b] / dist5 - fact * (1 if a==b else 0) / dist3)
                        D[i*3 + a, j*3 + b] += val
                        D[j*3 + b, i*3 + a] += val

        # Short-range on-site diagonals
        diag0 = (1.0 / M0) * pref_short * (8.0 / 3.0) * (A_prime + 2.0*B)
        for a in range(3):
            D[a, a] += diag0

        for l in range(1, 9):
            Ml = masses[l]
            diag_l = (1.0 / Ml) * pref_short * (1.0 / 3.0) * (A_prime + 7.0*A + 16.0*B)
            idx = l * 3
            for a in range(3):
                D[idx + a, idx + a] += diag_l

        # Short-range off-diagonal central-neighbour blocks
        for l in range(1, 9):
            Ml = masses[l]
            inv_sqrt_m = 1.0 / math.sqrt(M0 * Ml)
            s_vec = sigs[l]
            for a in range(3):
                for b in range(3):
                    val = -inv_sqrt_m * pref_short * ((A_prime - B) * s_vec[a]*s_vec[b] / 3.0 + B * (1 if a==b else 0))
                    D[a, l*3 + b] += val
                    D[l*3 + b, a] += val

        # Diagonalise (real symmetric)
        eigvals = np.linalg.eigh(D)[0]
        omega2 = eigvals[-1]
        omega = math.sqrt(max(omega2, 0.0))
        freq = omega / 1e13
        rows.append((A_prime, imp_name, freq))

# Write scored CSV
with open(os.path.join(outdir, 'localized_frequencies.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['A_prime', 'impurity', 'frequency'])
    for row in rows:
        writer.writerow(row)
EOF_SCRIPT
