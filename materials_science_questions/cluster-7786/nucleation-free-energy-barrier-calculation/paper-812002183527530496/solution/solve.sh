#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nucleation_curve.csv ===
python3 << 'PYEOF'
import math
import csv

# Given parameters
x_A = 2.5e-3
x_B = x_A
a_A_sat = 1.0e-3
a_B_sat = 1.0e-3
v_n = 2.0e-5   # m^3 mol^-1
sigma = 0.8    # N m^-1
N = 1e16
T = 1000.0
R = 8.314      # J mol^-1 K^-1

# Initial mole numbers (1 mol system)
n_A0 = x_A
n_B0 = x_B
n_C0 = 1.0 - 2.0 * x_A

# Activity denominators
# (initial activities are just the mole fractions)
a_A0 = n_A0
a_B0 = n_B0
a_C0 = n_C0

def n_AB_from_r(r):
    return (4.0 * math.pi * r**3 * N) / (3.0 * v_n)

def A_from_r(r):
    return 4.0 * math.pi * r**2 * N

r = 1e-11
dr = 1e-11
rows = []
max_steps = 20000
for step in range(max_steps):
    n_AB = n_AB_from_r(r)
    # Mole fraction of nuclei must not exceed x_A (all A consumed)
    if n_AB >= x_A:
        break
    denom = 1.0 - 2.0 * n_AB
    if denom <= 0:
        break
    a_A_star = (x_A - n_AB) / denom
    a_B_star = a_A_star
    a_C_star = n_C0 / denom

    if a_A_star <= 0 or a_B_star <= 0 or a_C_star <= 0:
        break

    # Supersaturation ratio for AB compound
    S_arg = (a_A_star * a_B_star) / (a_A_sat * a_B_sat)
    term1 = -n_AB * R * T * math.log(S_arg)
    term2 = n_A0 * R * T * math.log(a_A_star / a_A0)
    term3 = n_B0 * R * T * math.log(a_B_star / a_B0)
    term4 = n_C0 * R * T * math.log(a_C_star / a_C0)
    term5 = sigma * A_from_r(r)
    dG = term1 + term2 + term3 + term4 + term5
    rows.append((r, dG))

    # Stop when parent-phase activity reaches saturation
    if a_A_star <= a_A_sat:
        break

    r += dr

# Write the CSV file (with header allowed by contract)
with open('/app/outputs/nucleation_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r', 'dG'])
    for r_val, dG_val in rows:
        writer.writerow([r_val, dG_val])

PYEOF
