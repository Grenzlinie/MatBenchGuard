#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: geometry_report.json ===
python3 << 'PYEOF' > /app/outputs/geometry_report.json
import json
import sys
import numpy as np

# --- crystallographic data (paper Table 1, Table 2) ---
a = 6.105
b = 8.658
c = 11.072
alpha = np.deg2rad(71.35)
beta  = np.deg2rad(77.58)
gamma = np.deg2rad(71.09)

# fractional coordinates (Table 2)
Br1 = np.array([0.5,      0.5,      0.0   ])
Br2 = np.array([0.4894,   0.7294,   0.0982])
O4  = np.array([0.0,      0.0,      0.5   ])   # oxonium oxygen

O1 = np.array([0.804,    0.7706,   0.4596])
O2 = np.array([0.854,    1.0563,   0.2714])
O3 = np.array([1.119,    1.2499,   0.2988])

# Inversion symmetry equivalents (centre at O4: 0,0,0.5)
O1_sym = np.array([-O1[0], -O1[1], 1.0 - O1[2]])
O2_sym = np.array([-O2[0], -O2[1], 1.0 - O2[2]])
O3_sym = np.array([-O3[0], -O3[1], 1.0 - O3[2]])

# --- Cartesian orthogonalisation matrix ---
cos_a = np.cos(alpha)
cos_b = np.cos(beta )
cos_g = np.cos(gamma)
sin_g = np.sin(gamma)
v_star = np.sqrt(1.0 - cos_a**2 - cos_b**2 - cos_g**2 + 2.0*cos_a*cos_b*cos_g)

cell = np.array([
    [a,                         0.0,                       0.0],
    [b*cos_g,                   b*sin_g,                   0.0],
    [c*cos_b,  c*(cos_a - cos_b*cos_g)/sin_g, c*v_star/sin_g]
])

frac_to_cart = lambda frac: frac @ cell

# --- 1. Br–Br bond length ---
Br1_cart = frac_to_cart(Br1)
Br2_cart = frac_to_cart(Br2)
br_br = np.linalg.norm(Br2_cart - Br1_cart)

# --- 2. Out-of-plane displacement of oxonium oxygen ---
# the six crown ether oxygens
crown_O = np.array([O1, O2, O3, O1_sym, O2_sym, O3_sym])
crown_O_cart = frac_to_cart(crown_O)

centroid = crown_O_cart.mean(axis=0)
centered = crown_O_cart - centroid

# least-squares plane via SVD
_, _, vh = np.linalg.svd(centered, full_matrices=False)
normal = vh[-1]   # plane normal

O4_cart = frac_to_cart(O4)
displacement = abs(np.dot(O4_cart - centroid, normal))

# --- 3. O(oxonium)···O(crown) distances ---
O_crown_dist = np.linalg.norm(crown_O_cart - O4_cart, axis=1)
min_dist = O_crown_dist.min()
max_dist = O_crown_dist.max()

result = {
    "br_br_bond_length_angstrom": round(float(br_br), 6),
    "oxonium_out_of_plane_displacement_angstrom": round(float(displacement), 6),
    "o_ox_crown_min_dist_angstrom": round(float(min_dist), 6),
    "o_ox_crown_max_dist_angstrom": round(float(max_dist), 6)
}

json.dump(result, sys.stdout, indent=2)
PYEOF
