#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: persistent_current.csv ===
python3 -c "
import numpy as np
hbar = 1.054571817e-34
m0 = 9.10938356e-31
me = 0.067 * m0
e = 1.602176634e-19
R = 100e-9
Phi0 = 2 * np.pi * hbar / e
A = hbar**2 / (4 * me * R**2)
x_arr = np.arange(-2.0, 2.005, 0.01)
J_vals = np.arange(-10, 11)
E_mat = A * (J_vals[:, None] + 2 * x_arr[None, :])**2
idx_min = np.argmin(E_mat, axis=0)
E_min = E_mat[idx_min, range(len(x_arr))]
dE_dx = np.gradient(E_min, 0.01)
I = -dE_dx / Phi0
current_nA = I * 1e9
import csv
with open('$OUTDIR/persistent_current.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['flux', 'current_nA'])
    for x, i in zip(x_arr, current_nA):
        w.writerow([x, i])
"

# === solve block: absorption_spectrum.csv ===
python3 /solution/compute.py absorption /app/outputs/absorption_spectrum.csv

# === solve block: raman_cross_section.csv ===
python3 /solution/compute.py raman /app/outputs/raman_cross_section.csv
