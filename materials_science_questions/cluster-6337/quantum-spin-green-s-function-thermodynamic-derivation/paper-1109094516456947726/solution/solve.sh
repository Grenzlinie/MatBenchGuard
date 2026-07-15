#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: results.csv ===
python3 -c '
import numpy as np
import csv, sys

N = 100
J_x = 1.0
J_y_ratios = [-2.0, -1.0, 0.0, 1.0, 2.0]
h_vals = np.arange(-3.0, 3.0001, 0.1)

eps = 1e-12

def compute_all(jyr):
    J_y = jyr
    k = np.pi * np.arange(1, N) / N
    A = -h_vals[:, None] + (J_x + J_y) * np.cos(2*k)
    B = (J_x - J_y) * np.sin(2*k)
    omega = np.sqrt(A**2 + B**2)
    # avoid division by zero near degeneracy points
    denom = omega + eps
    sin_half_sq = 0.5 * (1 - A/denom)
    sin_theta = -B/denom
    gamma0 = np.sum(sin_half_sq, axis=1) * 2/N
    gamma1 = np.sum(np.cos(k) * sin_half_sq, axis=1) * 2/N
    gamma2 = np.sum(np.cos(2*k) * sin_half_sq, axis=1) * 2/N
    xi1 = -np.sum(np.sin(k) * sin_theta, axis=1) / N
    xi2 = -np.sum(np.sin(2*k) * sin_theta, axis=1) / N
    n_l = gamma0
    # nearest neighbour (distance 1) correlations
    x12 = xi1
    z12 = gamma1
    # corrected fermion Wick: <n_l n_{l+1}> = n_l^2 + |z12|^2 - |x12|^2
    nn1 = n_l**2 + gamma1**2 - xi1**2
    Czz1 = 4*nn1 - 4*n_l + 1
    u12 = (1 + 2*(2*n_l-1) + Czz1)/4
    v12 = (1 - 2*(2*n_l-1) + Czz1)/4
    w12 = (1 - Czz1)/4
    C12 = 2 * np.maximum(0, np.maximum(np.abs(x12)-w12, np.abs(z12)-np.sqrt(np.maximum(u12*v12,0))))
    # next-nearest neighbour (distance 2) correlations
    x13 = xi2 * (1 - 2*n_l)
    z13 = gamma2*(1-2*n_l) + 2*gamma1**2
    # corrected fermion Wick: <n_l n_{l+2}> = n_l^2 + gamma2^2 - xi2^2
    nn2 = n_l**2 + gamma2**2 - xi2**2
    Czz2 = 4*nn2 - 4*n_l + 1
    u13 = (1 + 2*(2*n_l-1) + Czz2)/4
    v13 = (1 - 2*(2*n_l-1) + Czz2)/4
    w13 = (1 - Czz2)/4
    C13 = 2 * np.maximum(0, np.maximum(np.abs(x13)-w13, np.abs(z13)-np.sqrt(np.maximum(u13*v13,0))))
    def entropy(p):
        p = np.clip(p, 1e-12, 1-1e-12)
        return -p*np.log2(p) - (1-p)*np.log2(1-p)
    S_single = entropy(n_l)
    diff = np.sqrt(((u13-v13)/2)**2 + x13**2)
    lambda1 = (u13+v13)/2 + diff
    lambda2 = (u13+v13)/2 - diff
    lambda3 = w13 + np.abs(z13)
    lambda4 = w13 - np.abs(z13)
    evals = np.stack([lambda1, lambda2, lambda3, lambda4], axis=-1)
    evals = np.clip(evals, 0, 1)
    S_joint = -np.sum(evals * np.log2(evals + 1e-12), axis=-1)
    I13 = 2*S_single - S_joint
    zeta = 0.5 + np.sqrt(((u13-v13)/2)**2 + (np.abs(x13)+np.abs(z13))**2)
    H_zeta = entropy(zeta)
    D13 = H_zeta + S_single - S_joint
    E_global = 4*n_l*(1-n_l)
    Mz = 2*n_l - 1
    return Mz, C12, C13, I13, D13, E_global

C13_matrix = []
Mz_matrix = []
C12_matrix = []
I13_matrix = []
D13_matrix = []
E_global_matrix = []

for jyr in J_y_ratios:
    Mz, C12, C13, I13, D13, Eg = compute_all(jyr)
    Mz_matrix.append(Mz)
    C12_matrix.append(C12)
    C13_matrix.append(C13)
    I13_matrix.append(I13)
    D13_matrix.append(D13)
    E_global_matrix.append(Eg)

C13_arr = np.array(C13_matrix)
dC_dJ_y = np.gradient(C13_arr, axis=0)
dC_dh = np.gradient(C13_arr, h_vals, axis=1)

writer = csv.writer(sys.stdout)
writer.writerow(["J_y_over_J_x", "h_over_J_x", "magnetization", "C_12", "C_13", "dC_dJ_y", "dC_dh", "I_13", "D_13", "E_global"])
for i, jyr in enumerate(J_y_ratios):
    for j, h in enumerate(h_vals):
        writer.writerow([
            jyr, round(h, 10), Mz_matrix[i][j], C12_matrix[i][j], C13_arr[i,j],
            dC_dJ_y[i,j], dC_dh[i,j], I13_matrix[i][j], D13_matrix[i][j], E_global_matrix[i][j]
        ])
' > "$OUTDIR/results.csv"
