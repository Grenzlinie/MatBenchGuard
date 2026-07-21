#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: bulk_band_structure.json ===
python3 - "$OUTDIR" << 'PYEOF'
import numpy as np
import json, sys, os

OUTDIR = sys.argv[1]

# High-symmetry points in fractional coordinates
Gamma = np.array([0.0, 0.0, 0.0])
Z = np.array([0.0, 0.0, 0.5])
T = np.array([0.5, 0.0, 0.5])

npts_seg = 60

def linspace_path(start, end, n):
    return [start + (end-start)*t for t in np.linspace(0,1,n, endpoint=True)]

GZ = linspace_path(Gamma, Z, npts_seg)
ZT = linspace_path(Z, T, npts_seg)
kpts = GZ + ZT[1:]  # drop duplicate Z

# Label only the high-symmetry points
kpath_objs = []
for i, k in enumerate(kpts):
    if i == 0:
        lab = "Gamma"
    elif i == npts_seg-1:
        lab = "Z"
    elif i == 2*npts_seg-2:
        lab = "T"
    else:
        lab = ""
    kpath_objs.append({"label": lab, "k": k.tolist()})

# Tight-binding parameters
e = -1.1112
t1p = -1.3298
t2p = 4.2265
t3p = -0.3605
t4p = -0.1621
t1t = 0.5558
t2t = 0.2303

def H_k(kx, ky, kz):
    # k in fractional coords, phase factors involve 2π
    a1 = 2*np.pi*kx
    a2 = 2*np.pi*ky
    a3 = 2*np.pi*kz
    h12 = t1p*(1 + np.exp(-1j*a2)) + t3p*(np.exp(-1j*a1) + np.exp(-1j*(a1+a2)))
    h13 = t4p*(1 + np.exp(-1j*a2) + np.exp(-1j*a1) + np.exp(-1j*(a1+a2))) + t2t*(np.exp(-1j*a3) + np.exp(-1j*(a1+a3)))
    h14 = t2p*np.exp(-1j*(a1+a2)) + t1t*(np.exp(-1j*(a1+a3)) + np.exp(-1j*(a1+a2+a3)))
    h23 = t2p + t1t*(np.exp(-1j*a3) + np.exp(1j*(a2-a3)))
    h24 = h13
    h34 = h12
    H = np.zeros((4,4), dtype=complex)
    H[0,1] = h12
    H[0,2] = h13
    H[0,3] = h14
    H[1,2] = h23
    H[1,3] = h24
    H[2,3] = h34
    H += np.conj(H).T
    np.fill_diagonal(H, e + np.diag(H))
    return H

# Eigenvalues along path
eigenvalues = []
for kpt in kpts:
    evals = np.linalg.eigvalsh(H_k(kpt[0], kpt[1], kpt[2]))
    eigenvalues.append(evals.tolist())

# Node line in T-Z-Gamma plane (ky=0) around Z
num_angles = 101
theta_vals = np.linspace(0, 2*np.pi, num_angles, endpoint=True)
node_line_points = []

def gap_at_r(r, theta):
    kx = Z[0] + r*np.cos(theta)
    kz = Z[2] + r*np.sin(theta)
    ev = np.linalg.eigvalsh(H_k(kx, 0.0, kz))
    return ev[2] - ev[1]  # band2 - band1

for theta in theta_vals:
    r_low, r_high = 0.0, 0.5
    gap_low = gap_at_r(r_low, theta)
    gap_high = gap_at_r(r_high, theta)
    if gap_low * gap_high > 0:
        continue  # no crossing in this direction
    for _ in range(50):
        r_mid = (r_low + r_high)/2
        gap_mid = gap_at_r(r_mid, theta)
        if gap_mid == 0:
            break
        if np.sign(gap_mid) == np.sign(gap_low):
            r_low = r_mid
            gap_low = gap_mid
        else:
            r_high = r_mid
            gap_high = gap_mid
    kx_node = Z[0] + r_mid*np.cos(theta)
    kz_node = Z[2] + r_mid*np.sin(theta)
    node_line_points.append([kx_node, 0.0, kz_node])

# Close the loop
if node_line_points:
    node_line_points.append(node_line_points[0])

data = {
    "kpath": kpath_objs,
    "eigenvalues": eigenvalues,
    "node_line_points": node_line_points
}

os.makedirs(OUTDIR, exist_ok=True)
with open(os.path.join(OUTDIR, "bulk_band_structure.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: berry_phase_zigzag.json ===
cd /app/outputs && python3 /solution/solve.py berry_phase_zigzag.json

# === solve block: surface_band_beard.json ===
cd /app/outputs && python3 /solution/solve.py surface_band_beard.json
