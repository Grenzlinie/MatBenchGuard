#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: homogeneous_T0.8_h0.88_simulation.csv ===
python3 -c "
import sys, math, csv
from scipy.special import lambertw
from scipy.integrate import quad

a = 1.957
b = 10.75
J_st = 1.75e-6
t0 = 19.96
m0 = 5.0

def m(t):
    if t < 1e-9:
        return float(m0)
    z = (a * (m0 - 1) / b) * math.exp((t + a * (m0 - 1)) / b)
    wr = float(complex(lambertw(z)).real)
    return 1.0 + (b / a) * wr

def x_ext(T):
    if T <= t0:
        return 0.0
    res, _ = quad(lambda u: m(u) ** 2, 0, T - t0, limit=200)
    return J_st * res

w = csv.writer(sys.stdout)
dt = 2.0
t = 0.0
while True:
    xv = x_ext(t)
    X = 1.0 - math.exp(-xv)
    M = 2.0 * X - 1.0
    w.writerow([t, M])
    if M >= 0.99:
        break
    t += dt
" > "$OUTDIR/homogeneous_T0.8_h0.88_simulation.csv"

# === solve block: breakdown_T0.4_h0.6_simulation.csv ===
python3 /solution/oracle_gen.py breakdown > "$OUTDIR/breakdown_T0.4_h0.6_simulation.csv"

# === solve block: percolation_results.json ===
python3 /solution/oracle_gen.py percolation > "$OUTDIR/percolation_results.json"
