#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_thresholds.csv ===
python3 -c "
import math, csv, os

SIGMA       = 20.0
RHO         = 1.0
DELTA_H_F   = 3.34e9
T_M         = 273.0
K_B         = 1.380649e-16
K_COEFF     = 1e20

def f(m, x):
    if x <= 1.0:
        return 0.0
    g = math.sqrt(1.0 + x**2 - 2.0 * m * x)
    if g == 0.0:
        return 0.0
    t1 = ((1.0 - m * x) / g) ** 3
    t2 = x**3 * (2.0 - 3.0 * (x - m) / g + ((x - m) / g) ** 3)
    t3 = 3.0 * m * x**2 * ((x - m) / g - 1.0)
    return 0.5 * (1.0 + t1 + t2 + t3)

def dG0_star(T):
    dT = T_M - T
    if dT <= 0.0:
        return float('inf')
    return 16.0 * math.pi * SIGMA**3 * T_M**2 / (3.0 * RHO**2 * DELTA_H_F**2 * dT**2)

def r_star(T):
    dT = T_M - T
    if dT <= 0.0:
        return float('inf')
    return 2.0 * SIGMA * T_M / (RHO * DELTA_H_F * dT)

def nucle_rate(R_cm, m_val, alpha, T):
    if T >= T_M:
        return 0.0
    dG0 = dG0_star(T)
    rs = r_star(T)
    if rs <= 0.0 or R_cm <= 0.0:
        return 0.0
    x = R_cm / rs
    fm = f(m_val, x)
    dG = dG0 * fm - alpha * R_cm**2 * (1.0 - m_val) * SIGMA
    if dG <= 0.0:
        return 1e9
    exponent = -dG / (K_B * T)
    if exponent > 700.0:
        return 1e9
    if exponent < -700.0:
        return 0.0
    area = 4.0 * math.pi * R_cm**2
    return area * K_COEFF * math.exp(exponent)

def threshold_T(R_cm, m_val, alpha):
    lo, hi = T_M - 60.0, T_M - 0.01
    for _ in range(100):
        mid = (lo + hi) / 2.0
        J = nucle_rate(R_cm, m_val, alpha, mid)
        if J >= 1.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0 - T_M

def pit_area_density(A):
    if A <= 0.0:
        return 0.0
    z = gam * math.log(A / A0) - 0.5 / gam
    return (beta / A0) * (math.sqrt(math.pi) / (2.0 * gam)) * math.exp(1.0 / (2.0 * gam**2)) * math.erfc(z)

def prob_at_least_one(R_cm, A):
    N = pit_area_density(A)
    return 1.0 - math.exp(-4.0 * math.pi * R_cm**2 * N)

def find_alpha(R_cm, F_tgt):
    lo = 1e-15
    hi = 100.0
    if prob_at_least_one(R_cm, lo * R_cm**2) < F_tgt:
        return lo
    if prob_at_least_one(R_cm, hi * R_cm**2) > F_tgt:
        return hi
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        prob = prob_at_least_one(R_cm, mid * R_cm**2)
        if prob >= F_tgt:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

m = 0.5
beta = 0.001
gam = 0.8
A0 = 2e-15
R_vals = [100, 316, 1000]
F_vals = [0.1, 0.5, 0.9]
rows = []
for R_ang in R_vals:
    R_cm = R_ang * 1e-8
    for F_tgt in F_vals:
        alpha_tgt = find_alpha(R_cm, F_tgt)
        T_C = threshold_T(R_cm, m, alpha_tgt)
        rows.append([R_ang, F_tgt, round(T_C, 2)])
out = '/app/outputs/step_01_thresholds.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['R_Angstrom', 'F_fraction', 'T_Celsius'])
    w.writerows(rows)
"
