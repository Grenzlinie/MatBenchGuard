#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: finite_N_timeseries.csv ===
mkdir -p "$OUTDIR"
python3 - "$OUTDIR/finite_N_timeseries.csv" <<'PYEOF'
import sys
import csv
import numpy as np

out_path = sys.argv[1]

N_spin = 10
lam = 1.0 / N_spin
sx = 1.0
sy = 0.0

tau = np.arange(0.0, 20.0 + 1e-12, 0.01)

# β_n = n (1 - n λ)  for n = 1, 2, ... , N
beta = [n * (1.0 - n * lam) for n in range(1, N_spin + 1)]

def poly_asc(deg, j):
    """Return the polynomial p_deg^{(j)} as a list of
    ascending-degree coefficients [c0, c1, ..., c_deg].
    Recurrence: p_{n+1}(x) = x p_n(x) - β_{n+j} p_{n-1}(x),
    with p_0 = 1, p_1 = x.
    """
    if deg < 0:
        return [0.0]
    if deg == 0:
        return [1.0]
    # p_1
    p_prev2 = [1.0]          # p_0
    p_prev1 = [0.0, 1.0]     # p_1
    if deg == 1:
        return p_prev1
    for n in range(1, deg):          # n goes 1 .. deg-1, computes p_{n+1}
        # x*p_n: shift p_prev1 right by 1 (constant becomes 0)
        new = [0.0] + p_prev1        # length = len(p_prev1)+1
        # subtract β_{n+j} * p_{n-1}
        bn = beta[n + j - 1]
        for i in range(len(p_prev2)):
            new[i] -= bn * p_prev2[i]
        # prepare for next iteration
        p_prev2 = p_prev1
        p_prev1 = new
    return p_prev1

def compute_u1(ell):
    p0_asc = poly_asc(ell, 0)             # p_ell^(0)
    p1_asc = poly_asc(ell - 1, 1)         # p_{ell-1}^(1)
    # numpy.roots expects descending-degree coefficients
    p0_desc = list(reversed(p0_asc))
    p1_desc = list(reversed(p1_asc))
    roots = np.roots(p0_desc)
    # all zeros are real and symmetric -> sort and take the positive half
    x_vals = np.sort(roots.real)
    # for even ell, ℓ/2 positive zeros starting at ell//2
    pos_roots = x_vals[ell // 2:]

    poly_p0 = np.poly1d(p0_desc)
    poly_p0_der = np.poly1d.deriv(poly_p0)
    poly_p1 = np.poly1d(p1_desc)

    # residues a_{ℓj} = p_{ℓ-1}^{(1)}(x_j) / p_ℓ^{(0)'}(x_j)
    a = poly_p1(pos_roots) / poly_p0_der(pos_roots)

    # u₁(τ) = 2 (sˣ + i sʸ) Σ_{j=1}^{ℓ/2} a_{ℓj} cos(x_{ℓj} τ)
    sum_cos = np.sum(a[:, np.newaxis] * np.cos(pos_roots[:, np.newaxis] * tau[np.newaxis, :]), axis=0)
    u1_cpx = (sx + 1j * sy) * 2.0 * sum_cos
    return np.real(u1_cpx), np.imag(u1_cpx)

with open(out_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['tau', 'u1_real', 'u1_imag', 'closure_order', 'N'])
    for ell in [2, 4]:
        real, imag = compute_u1(ell)
        for i in range(len(tau)):
            w.writerow([tau[i], real[i], imag[i], ell, N_spin])
PYEOF

# === solve block: thermodynamic_limit_timeseries.csv ===
python3 /solution/produce_outputs.py thermo /app/outputs/thermodynamic_limit_timeseries.csv
