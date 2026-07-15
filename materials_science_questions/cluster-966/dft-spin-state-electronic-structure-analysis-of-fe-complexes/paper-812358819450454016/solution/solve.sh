#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/compute_moments.py

# === solve block: calculated_moments.csv ===
python3 /dev/stdin << 'PYEOF'
import csv
import numpy as np

# =========================
# Physical operators
# =========================

# L operators in the spherical basis |ml=+2,+1,0,-1,-2> (5x5)
Lz_sp = np.diag([2, 1, 0, -1, -2])
Lp_sp = np.zeros((5, 5))
Lm_sp = np.zeros((5, 5))
for i in range(5):
    ml = 2 - i
    if ml < 2:
        Lp_sp[i - 1, i] = np.sqrt(6 - ml * (ml + 1))
    if ml > -2:
        Lm_sp[i + 1, i] = np.sqrt(6 - ml * (ml - 1))
Lx_sp = (Lp_sp + Lm_sp) / 2.0
Ly_sp = (Lp_sp - Lm_sp) / (2j)

# S operators for spin S=2 (5x5)
Sz_sp = np.diag([2, 1, 0, -1, -2])
Sp_sp = np.zeros((5, 5))
Sm_sp = np.zeros((5, 5))
for i in range(5):
    ms = 2 - i
    if ms < 2:
        Sp_sp[i - 1, i] = np.sqrt(6 - ms * (ms + 1))
    if ms > -2:
        Sm_sp[i + 1, i] = np.sqrt(6 - ms * (ms - 1))
Sx_sp = (Sp_sp + Sm_sp) / 2.0
Sy_sp = (Sp_sp - Sm_sp) / (2j)

# Transformation from spherical to t₂g orbital basis:
# |+1> (ml=+1), |-1> (ml=-1), |xy> = (|+2> - |-2>)/√2
inv_sqrt2 = 1.0 / np.sqrt(2)
U = np.zeros((5, 3), dtype=complex)
U[1, 0] = 1.0               # |+1>
U[3, 1] = 1.0               # |-1>
U[0, 2] = inv_sqrt2         # |xy>
U[4, 2] = -inv_sqrt2

# 3×3 L operators in t₂g basis
Lz_t2g = U.conj().T @ Lz_sp @ U
Lx_t2g = U.conj().T @ Lx_sp @ U
Ly_t2g = U.conj().T @ Ly_sp @ U

# Identity matrices
I3 = np.eye(3)
I5 = np.eye(5)

# Combined 15×15 operators
Lz_full = np.kron(Lz_t2g, I5)
Sz_full = np.kron(I3, Sz_sp)

Lx_full = np.kron(Lx_t2g, I5)
Ly_full = np.kron(Ly_t2g, I5)
Sx_full = np.kron(I3, Sx_sp)
Sy_full = np.kron(I3, Sy_sp)

# Spin-orbit coupling L·S
LS = Lx_full @ Sx_full + Ly_full @ Sy_full + Lz_full @ Sz_full

# Magnetic moment operator for the z-direction
mu_z_op = lambda k: k * Lz_full + 2.0 * Sz_full

# =========================
# Parameter grid
# =========================
ks = [1.0, 0.9, 0.8, 0.7]
vs = [10, 5, 3, 2, 1, 0, -1, -2, -3, -5, -10]
kts = [0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0,
       -0.1, -0.2, -0.3, -0.5, -0.75, -1.0, -1.5, -2.0, -3.0]

rows = []
for k_val in ks:
    for v_val in vs:
        # Set lambda = -1 (energy scale); Delta = v * lambda
        lam = -1.0
        Delta = v_val * lam
        # Axial field Hamiltonian in orbital space
        H_ax_orb = np.diag([Delta / 3.0, Delta / 3.0, -2.0 * Delta / 3.0])
        H_ax_full = np.kron(H_ax_orb, I5)

        # Full perturbation Hamiltonian
        H = H_ax_full + lam * LS

        # Diagonalization
        evals, evecs = np.linalg.eigh(H)

        # mu_z operator and its square
        mu_z = mu_z_op(k_val)
        mu_z2 = mu_z @ mu_z

        # Diagonal elements of mu_z^2 in the eigenbasis
        tmp = evecs.conj().T @ mu_z2 @ evecs
        mu2_diag = np.real(np.diag(tmp))

        for kt in kts:
            if kt == 0.0:
                mu_eff = 0.0
            else:
                # Boltzmann weight = exp(E/kt) when λ = -1 (see instructions)
                weights = np.exp(evals / kt)
                Z = np.sum(weights)
                mu2_avg = np.sum(mu2_diag * weights) / Z
                mu_eff = np.sqrt(np.abs(mu2_avg))
            rows.append([k_val, v_val, kt, round(mu_eff, 2)])

# =========================
# Write output CSV
# =========================
with open('/app/outputs/calculated_moments.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['k', 'v', 'kT_over_lambda', 'mu_eff'])
    for r in rows:
        writer.writerow(r)
PYEOF
