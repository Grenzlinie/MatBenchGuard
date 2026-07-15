#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: step_02_orowan_contribution.csv ===
python3 << 'PYEOF'
import csv
import math

def compute(d_nm, N_V, T=750):
    # Convert to SI
    d_m = d_nm * 1e-9
    # Elastic modulus
    E_GPa = 140.0 - 0.07 * T
    # Shear modulus
    nu = 0.25
    G_GPa = E_GPa / (2.0 * (1.0 + nu))
    G_Pa = G_GPa * 1e9
    # Constants
    M = 3.06
    b = 2.53e-10
    r0 = b
    # Planar inter-particle separation
    lambda_S_m = 1.0 / (2.0 * math.sqrt(N_V * d_m))
    # Mean planar intersection diameter
    d_S_m = d_m * math.sqrt(2.0/3.0)
    # Orowan stress
    tau_Pa = (0.81 * M * G_Pa * b) / (2.0 * math.pi * math.sqrt(1.0 - nu)) * math.log(d_S_m / r0) / (lambda_S_m - d_S_m)
    tau_MPa = tau_Pa * 1e-6
    return {
        'd_nm': d_nm,
        'N_V_per_m3': N_V,
        'lambda_S_nm': lambda_S_m * 1e9,
        'd_S_nm': d_S_m * 1e9,
        'G_GPa': G_GPa,
        'tau_MPa': tau_MPa
    }

# Inputs from the paper
CF8C_Plus = compute(d_nm=16, N_V=6.8e20)
CF8C = compute(d_nm=55, N_V=4.6e19)

rows = [
    {**CF8C_Plus, 'alloy': 'CF8C-Plus'},
    {**CF8C, 'alloy': 'CF8C'}
]

fieldnames = ['alloy', 'd_nm', 'N_V_per_m3', 'lambda_S_nm', 'd_S_nm', 'G_GPa', 'tau_MPa']

with open('/app/outputs/step_02_orowan_contribution.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
PYEOF
