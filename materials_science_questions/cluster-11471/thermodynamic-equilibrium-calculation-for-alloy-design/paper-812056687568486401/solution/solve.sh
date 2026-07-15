#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pb_sn_gibbs_thomson.csv ===
python3 << PYEOF
import math

# Constants
sigma = 0.235       # J/m^2
Vm = 16.26e-6       # m^3/mol
R = 8.314
T = 423.15          # 150 C
X0 = 0.1929         # flat interface X_Sn^fcc
Xb = 0.98           # precipitate Sn mole fraction
e = 0.487           # Darken factor at X0

RT = R * T

def integrand(t):
    return ((Xb - t) / (1.0 - t)) * (1.0 / t)

def integrate_upper(X):
    N = 10000
    h = (X - X0) / N
    s = 0.0
    for i in range(N):
        t1 = X0 + i * h
        t2 = t1 + h
        s += (integrand(t1) + integrand(t2)) * 0.5 * h
    return s

radii_nm = [1,2,3,4,5,6,7,8,9,10,12,15,20,25,30,40,50,60,80,100]

with open("$OUTDIR/pb_sn_gibbs_thomson.csv", "w") as f:
    f.write("radius_nm,X_Sn_fcc\n")
    for r in radii_nm:
        target = (2 * sigma * Vm) / (r * 1e-9 * RT)
        lo = X0
        hi = 0.98
        for _ in range(50):
            mid = (lo + hi) / 2
            val = e * integrate_upper(mid)
            if val < target:
                lo = mid
            else:
                hi = mid
        X = (lo + hi) / 2
        f.write(f"{r},{X:.6f}\n")
PYEOF
