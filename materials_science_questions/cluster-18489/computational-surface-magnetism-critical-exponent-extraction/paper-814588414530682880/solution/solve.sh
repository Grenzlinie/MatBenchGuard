#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: t_c_vs_delta_s.csv ===
OUTDIR="$OUTDIR" python3 - << 'PYEOF'
import os, csv, math

J = 1.0
Omega_s = 0.0
Omega_b = 0.0

def f_omega(x, Omega, beta):
    if x == 0.0:
        return 0.0
    denom = math.sqrt(x*x + Omega*Omega)
    return (x / denom) * math.tanh(beta * denom)

def apply_operator(factors, Omega, beta):
    def rec(idx, current_coeff, current_shift):
        if idx == len(factors):
            return current_coeff * f_omega(current_shift, Omega, beta)
        typ, alpha = factors[idx]
        total = 0.0
        if typ == 'ch':
            total += rec(idx+1, current_coeff * 0.5, current_shift + alpha)
            total += rec(idx+1, current_coeff * 0.5, current_shift - alpha)
        else:  # 'sh'
            total += rec(idx+1, current_coeff * 0.5, current_shift + alpha)
            total += rec(idx+1, -current_coeff * 0.5, current_shift - alpha)
        return total
    return rec(0, 1.0, 0.0)

def compute_k_series(ds, r, beta):
    Js = J * (1.0 + ds)
    Jr = r * J
    # k1
    k1 = apply_operator([('sh', Js), ('ch', Js), ('ch', Jr), ('ch', J)], Omega_s, beta)
    # k2
    k2 = apply_operator([('ch', Js), ('ch', Js), ('sh', Jr), ('ch', J)], Omega_s, beta)
    # k3
    k3 = apply_operator([('ch', Js), ('ch', Js), ('ch', Jr), ('sh', J)], Omega_s, beta)
    # k4
    k4 = apply_operator([('ch', Jr), ('sh', J)] + [('ch', J)] * 5, Omega_b, beta)
    # k5
    k5 = apply_operator([('sh', Jr)] + [('ch', J)] * 6, Omega_b, beta)
    return k1, k2, k3, k4, k5

def equation(t, ds, r):
    beta = 1.0 / t
    k1, k2, k3, k4, k5 = compute_k_series(ds, r, beta)
    return (1.0 - (2*k1 + k2)) * (1.0 - k5) - 6*k3*k4

def solve_tc(ds, r):
    lo, hi = 0.1, 50.0
    f_lo = equation(lo, ds, r)
    f_hi = equation(hi, ds, r)
    if f_lo * f_hi > 0:
        return None  # root not bracketed, should not happen
    for _ in range(60):
        mid = (lo + hi) / 2
        f_mid = equation(mid, ds, r)
        if f_mid == 0.0:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2

outdir = os.environ['OUTDIR']
outpath = os.path.join(outdir, 't_c_vs_delta_s.csv')
with open(outpath, 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(['delta_s', 'r', 't_c'])
    for r_val in [0.0, 1.5]:
        for i in range(0, 11):
            ds = i * 0.5
            tc = solve_tc(ds, r_val)
            writer.writerow([ds, r_val, tc])
PYEOF

# === solve block: t_c_vs_r.csv ===
python3 /solution/compute.py --mode t_c_vs_r --out "$OUTDIR/t_c_vs_r.csv"

# === solve block: t_c_vs_q.csv ===
python3 /solution/compute.py --mode t_c_vs_q --out "$OUTDIR/t_c_vs_q.csv"

# === solve block: m_T_vs_T.csv ===
python3 /solution/compute.py --mode m_T_vs_T --out "$OUTDIR/m_T_vs_T.csv"
