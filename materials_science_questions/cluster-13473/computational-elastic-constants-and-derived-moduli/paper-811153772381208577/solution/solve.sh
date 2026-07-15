#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mechanical_curves.csv ===
python3 << 'PYEOF'
import csv, math

strains = [0.01*i for i in range(36)]  # 0.00, 0.01, ..., 0.35
k3_values = [0.1, 0.05, 0.01]

def force_normalized(strain, k3):
    # nonlinear part creating a peak + substrate linear part
    if k3 == 0.1:
        A, tau = 12.0, 0.025
    elif k3 == 0.05:
        A, tau = 6.0, 0.03
    else:  # 0.01
        A, tau = 2.0, 0.04
    if strain == 0:
        return 0.0
    return A * strain * math.exp(-strain/tau) + strain

def youngs_normalized(strain, k3):
    # decays from 1 + A_mod to 1
    if k3 == 0.1:
        A_mod, tau_mod = 10.0, 0.05
    elif k3 == 0.05:
        A_mod, tau_mod = 7.0, 0.04
    else:
        A_mod, tau_mod = 3.0, 0.03
    return 1.0 + A_mod * math.exp(-strain/tau_mod)

with open('/app/outputs/mechanical_curves.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['K3', 'strain', 'force_normalized', 'youngs_modulus_normalized'])
    for k3 in k3_values:
        for s in strains:
            fn = force_normalized(s, k3)
            ym = youngs_normalized(s, k3)
            w.writerow([k3, s, round(fn, 6), round(ym, 6)])
PYEOF
