#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: spin_current.csv ===
python3 <<'PYEOF'
import numpy as np
from scipy.special import loggamma

M = 600  # truncation dimension

def get_p(gamma, h):
    return 1j / (2.0 * (gamma - 1j * h))

def build_B0(p):
    k = np.arange(M, dtype=float)
    p_minus_k_sq = (p.real - k)**2 + p.imag**2
    two_p_minus_k_sq = (2*p.real - k)**2 + (2*p.imag)**2
    B0 = np.zeros((M, M), dtype=float)
    for i in range(M):
        B0[i, i] = 2.0 * p_minus_k_sq[i]
        if i > 0:
            B0[i, i-1] = two_p_minus_k_sq[i-1]
        if i < M-1:
            B0[i, i+1] = (i+1)**2
    return B0

def compute_vR(p, theta):
    if theta == 0.0:
        vR = np.zeros(M, dtype=float)
        vR[0] = 1.0
        return vR
    tan = np.tan(theta / 2.0)
    psi_sq = tan ** 2
    vR = np.zeros(M, dtype=float)
    for k in range(M):
        # |binom(2p, k)|^2 using loggamma for safety
        log_bin = loggamma(2*p + 1) - loggamma(k + 1) - loggamma(2*p - k + 1)
        abs_bin2 = np.exp(2 * np.real(log_bin))
        vR[k] = (psi_sq ** k) * abs_bin2
    # normalize to avoid underflow? Not needed.
    return vR

def compute_J(N, h, gamma, theta):
    p = get_p(gamma, h)
    B0 = build_B0(p)
    vR = compute_vR(p, theta)
    v = np.zeros(M, dtype=float)
    v[0] = 1.0
    scale_product = 1.0
    Z_vals = []
    for i in range(N + 1):
        Z_i = scale_product * np.dot(v, vR)
        Z_vals.append(Z_i)
        if i == N:
            break
        v = v @ B0
        max_abs = np.max(np.abs(v))
        if max_abs > 0:
            v /= max_abs
            scale_product *= max_abs
        else:
            # fill remaining with last computed Z to avoid error
            Z_vals.extend([Z_vals[-1]] * (N - len(Z_vals) + 1))
            break
    Z_N = Z_vals[N]
    Z_Nm1 = Z_vals[N-1] if N > 0 else 1.0
    if Z_N == 0:
        return 0.0
    prefactor = 2.0 * gamma / (gamma**2 + h**2)
    J = prefactor * (Z_Nm1 / Z_N)
    return J

# Fixed parameter grid as specified in the task instructions
rows = [
    (10, 0.0, 1e-5, 0.0),
    (10, 0.0, 0.01, 0.0),
    (10, 0.0, 1.0, 0.0),
    (50, 0.0, 1e-5, 0.0),
    (50, 0.0, 0.01, 0.0),
    (50, 0.0, 1.0, 0.0),
    (100, 0.0, 1e-5, 0.0),
    (100, 0.0, 0.01, 0.0),
    (100, 0.0, 1.0, 0.0),
    (200, 0.0, 1e-5, 0.0),
    (200, 0.0, 0.01, 0.0),
    (200, 0.0, 1.0, 0.0),
    (500, 0.0, 1e-5, 0.0),
    (500, 0.0, 0.01, 0.0),
    (500, 0.0, 1.0, 0.0),
    (500, -0.1, 1e-5, 0.0),
    (500, -0.05, 1e-5, 0.0),
    (500, -0.02, 1e-5, 0.0),
    (500, -0.01, 1e-5, 0.0),
    (500, 0.01, 1e-5, 0.0),
    (500, 0.05, 1e-5, 0.0),
    (100, -0.1, 0.01, 0.0),
    (100, -0.05, 0.01, 0.0),
    (100, 0.0, 0.01, 0.0),
    (100, 0.05, 0.01, 0.0),
    (100, -0.1, 1.0, 0.0),
    (100, 0.0, 1.0, 0.0),
    (100, 0.1, 1.0, 0.0),
    (500, 0.0, 1e-5, 0.1),
]

import csv
output_path = "/app/outputs/spin_current.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "h", "gamma", "theta", "J"])
    for (N, h, gamma, theta) in rows:
        J = compute_J(N, h, gamma, theta)
        writer.writerow([N, h, gamma, theta, J])

print("spin_current.csv written with", len(rows), "rows.")
PYEOF
