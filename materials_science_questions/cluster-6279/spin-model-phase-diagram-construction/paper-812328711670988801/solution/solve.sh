#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: tricritical_points.json ===
python3 << 'PYEOF' > "$OUTDIR/tricritical_points.json"
import numpy as np
from scipy.optimize import fsolve
import json

# Spin matrices
Sz = np.diag([1.0, 0.0, -1.0])
Sx = np.array([[0,1,0],[1,0,1],[0,1,0]], dtype=float) / np.sqrt(2)

from math import comb
N = 4

def F1z_F2z(a1, a2, a3):
    H = np.array([[-a1 - a3, -a2, 0.0],
                  [-a2, 0.0, -a2],
                  [0.0, -a2, a1 - a3]], dtype=float)
    eigvals, eigvecs = np.linalg.eigh(H)
    Z = np.sum(np.exp(-eigvals))
    f1 = 0.0
    f2 = 0.0
    for k in range(3):
        v = eigvecs[:, k]
        exp_Sz = v.conj().dot(Sz).dot(v).real
        exp_Sz2 = v.conj().dot(np.diag([1.0, 0.0, 1.0])).dot(v).real
        w = np.exp(-eigvals[k])
        f1 += exp_Sz * w
        f2 += exp_Sz2 * w
    return f1 / Z, f2 / Z

def compute_q0z(c, Omega, T, D, tol=1e-12, max_iter=500):
    q = min(c, 0.5)
    for it in range(max_iter):
        total = 0.0
        for mu1 in range(N+1):
            for mu2 in range(N-mu1+1):
                for mu3 in range(N-mu1-mu2+1):
                    coeff = comb(N, mu1) * comb(N-mu1, mu2) * comb(N-mu1-mu2, mu3)
                    coeff *= (2**(mu1+mu3)) * (1-c)**mu1
                    if c - q >= 0:
                        coeff *= (c - q)**mu3
                    else:
                        coeff = 0.0
                    coeff *= q**(N-mu1-mu3)
                    z = N - mu1 - 2*mu2 - mu3
                    a1 = z / T
                    a2 = Omega / (np.sqrt(2) * T)
                    a3 = D / T
                    _, f2 = F1z_F2z(a1, a2, a3)
                    total += coeff * f2
        total *= (2**(-N))
        if abs(total - q) < tol:
            return total
        q = total
    return q

def compute_ab(c, Omega, T, D, q0):
    a = 0.0; b = 0.0
    for mu1 in range(N+1):
        for mu2 in range(N-mu1+1):
            for mu3 in range(N-mu1-mu2+1):
                z = N - mu1 - 2*mu2 - mu3
                a1 = z / T
                a2 = Omega / (np.sqrt(2) * T)
                a3 = D / T
                f1, _ = F1z_F2z(a1, a2, a3)
                for i in range(mu2+1):
                    for j in range(N-mu1-mu2-mu3+1):
                        base = comb(N, mu1) * comb(N-mu1, mu2) * comb(N-mu1-mu2, mu3)
                        base *= comb(mu2, i) * comb(N-mu1-mu2-mu3, j)
                        base *= ((-1)**i) * (2**(mu1+mu3)) * (q0**(N-mu1-mu3-i-j))
                        if i+j == 1:
                            a_term = base * (1-c)**mu1 * ((c-q0)**mu2 if c-q0>=0 else 0.0)
                            a += a_term * f1
                        elif i+j == 3:
                            b_term = base * (1-c)**mu1 * ((c-q0)**mu3 if c-q0>=0 else 0.0)
                            b += b_term * f1
    a *= (2**(-N))
    b *= (2**(-N))
    return a, b

def equations(vars, c, Omega):
    T, D = vars
    q0 = compute_q0z(c, Omega, T, D)
    a, b = compute_ab(c, Omega, T, D, q0)
    return [a - 1.0, b]

targets = [
    (1.0, 0.1, 1.5, -1.9),
    (0.8, 0.1, 1.0, -1.5),
    (0.8, 0.5, 0.7, -1.4)
]
results = []
for c, Om, T0, D0 in targets:
    sol = fsolve(lambda x: equations(x, c, Om), [T0, D0], xtol=1e-12, maxfev=2000)
    Tt, Dt = sol
    results.append({"c": c, "Omega_over_J": Om, "Tt_over_J": round(float(Tt), 6), "neg_Dt_over_J": round(float(-Dt), 6)})
print(json.dumps(results))
PYEOF
