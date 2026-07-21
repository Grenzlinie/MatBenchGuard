#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: force_constants.csv ===
python3 <<'PYEOF'
import math

def R(x, y):
    """Auxiliary function from Eq. (12)"""
    if y == 0.0:
        # limit y->0: R = ln( (1 - cos(2πx)) / (1 - cos(2πx)) ) - 0 = 0
        return 0.0
    c = math.cosh(4 * math.pi * y)
    cos_term = math.cos(2 * math.pi * x)
    log_arg = (c - cos_term) / (1.0 - cos_term)
    if log_arg <= 0:
        return 0.0
    term1 = math.log(log_arg)
    term2 = 8 * (math.pi * y) ** 2 * (c * cos_term - 1.0) / (c - cos_term) ** 2
    return term1 - term2

# Combinations
modes = ['h', 'sc', 'sa']
d_over_D_vals = [0.3, 0.5, 0.7]
D_over_H_vals = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]

rows = []
for dods in d_over_D_vals:
    for Doh in D_over_H_vals:
        # x and y arguments for R
        y = (Doh / 2.0)  # H/(2D) = 1/(2*(D/H))
        x1 = dods / 2.0
        x2 = x1 + 0.5
        x_half = 0.5
        R1 = R(x1, y)
        R2 = R(x2, y)
        Rhalf = R(x_half, y)
        prefactor = math.sqrt(2.0) / math.pi
        k_h = prefactor * (R1 + R2)
        k_sc = prefactor * (R1 - Rhalf)
        k_sa = prefactor * (R2 - Rhalf)
        rows.append(('h', dods, Doh, k_h))
        rows.append(('sc', dods, Doh, k_sc))
        rows.append(('sa', dods, Doh, k_sa))

with open('/app/outputs/force_constants.csv', 'w') as f:
    f.write('mode,d_over_D,D_over_H,k_norm\n')
    for mode, dods, Doh, k in rows:
        f.write(f"{mode},{dods},{Doh},{k}\n")
PYEOF

# === solve block: dielectric_contribution.csv ===
python3 <<'PYEOF'
import math

def R(x, y):
    if y == 0.0:
        return 0.0
    c = math.cosh(4 * math.pi * y)
    cos_term = math.cos(2 * math.pi * x)
    log_arg = (c - cos_term) / (1.0 - cos_term)
    if log_arg <= 0:
        return 0.0
    term1 = math.log(log_arg)
    term2 = 8 * (math.pi * y) ** 2 * (c * cos_term - 1.0) / (c - cos_term) ** 2
    return term1 - term2

# Equilibrium geometry from model for S_r/S_r^0 = 0.5
h_norm_vals = [0.1, 1.0, 10.0, 100.0]
doh_vals = [1.2, 2.0, 3.8, 6.5]  # D/H
d_over_D = 0.7

with open('/app/outputs/dielectric_contribution.csv', 'w') as f:
    f.write('H_norm,delta_epsilon_norm\n')
    for h_norm, doh in zip(h_norm_vals, doh_vals):
        y = doh / 2.0
        x1 = d_over_D / 2.0
        x_half = 0.5
        k_sc_norm = (math.sqrt(2.0) / math.pi) * (R(x1, y) - R(x_half, y))
        if k_sc_norm <= 0:
            k_sc_norm = 1e-12  # avoid division by zero
        delta_eps = (2.0 * math.sqrt(2.0)) / (k_sc_norm * doh)
        f.write(f"{h_norm},{delta_eps}\n")
PYEOF
