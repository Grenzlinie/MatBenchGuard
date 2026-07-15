#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: size_distribution.csv ===
python3 - <<'PYEOF'
import math

params = {
    4006: {'n_total':0.00897,'delta':0.1675,'lam':1.0877,'S':0.9576,'Z':0.94},
    5005: {'n_total':0.0649,'delta':0.1335,'lam':0.9517,'S':0.9910,'Z':0.75},
    6004: {'n_total':0.250,'delta':0.1317,'lam':0.7125,'S':1.0,'Z':0.55}
}

def k0_of_k(k, lam, delta):
    A = (lam + 2*delta) / 2
    lo, hi = 1.0, k
    for _ in range(200):
        mid = (lo + hi) / 2
        rhs = A * (3 * (k - mid)**(2/3) + 3*lam * (k - mid)**(1/3) + lam**2)
        if rhs > mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def compute_R(T_info, max_k=26):
    S = T_info['S']
    lam = T_info['lam']
    delta = T_info['delta']
    target = 1.0 / T_info['Z'] - 1.0
    # binary search for R
    lo, hi = 0.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2
        tot = 0.0
        for k in range(2, max_k+1):
            k0 = k0_of_k(k, lam, delta)
            term = k * S**(k-1) * mid**(k0 - 1)
            tot += term
        if tot < target:
            lo = mid
        else:
            hi = mid
    R = (lo + hi) / 2
    return R

outpath = '/app/outputs/size_distribution.csv'
with open(outpath, 'w') as f:
    f.write('temperature,cluster_size,number_density\n')
    for T, p in params.items():
        Z = p['Z']
        n_total = p['n_total']
        n1 = Z * n_total
        S = p['S']
        lam = p['lam']
        delta = p['delta']
        R = compute_R(p)
        for k in range(2, 27):
            k0 = k0_of_k(k, lam, delta)
            nk = n1 * S**(k-1) * R**(k0 - 1)
            f.write(f'{T},{k},{nk}\n')
PYEOF

# === solve block: structure_parameter.json ===
python3 /solution/make_outputs.py --json

# === solve block: transition_temperature.txt ===
python3 /solution/make_outputs.py --txt
