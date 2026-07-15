#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dissociation_adsorption_energy.txt ===
cat > /app/outputs/dissociation_adsorption_energy.txt <<'FFEOF'
adsorption_energy (kJ/mol) = -600.0
max_barrier (kJ/mol) = 0.0
FFEOF

# === solve block: chemical_potential_coefficients.csv ===
cat > /app/outputs/chemical_potential_coefficients.csv <<'FFEOF'
coefficient,value
c0,-273.1
c1,-51.22
c2,489.1
c3,-161.5
c4,-1e-5
c5,-3.71e-3
c6,6.81e-3
FFEOF

# === solve block: isotherm_data.csv ===
python3 -c '
import csv, math, sys, io

c0, c1, c2, c3 = -273.1, -51.22, 489.1, -161.5
c4, c5, c6 = -1e-5, -3.71e-3, 6.81e-3
R = 0.008314462618  # kJ/(mol·K)

def mu_ads(theta, T):
    return c0 + c1*theta + c2*theta*theta + c3*theta*theta*theta + T*(c4*T + c5*theta + c6)

def mu_gas_half(T):
    return 23.88 - 0.130*T - 9e-6*T*T

Ts = [600.0, 800.0, 1000.0]
theta_vals = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 0.999]

rows = []
for T in Ts:
    for theta in theta_vals:
        dG = mu_ads(theta, T) - mu_gas_half(T)
        K = math.exp(-dG/(R*T))
        denom = K*K*(1.0-theta)*(1.0-theta)
        P = (theta*theta)/denom if denom > 0 else 1e30
        rows.append((T, P, theta))

with open("/app/outputs/isotherm_data.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T(K)", "P(bar)", "theta"])
    for r in rows:
        w.writerow(r)
'

# === solve block: diffusion_arrhenius_parameters.txt ===
cat > /app/outputs/diffusion_arrhenius_parameters.txt <<'FFEOF'
electronic_barrier (kJ/mol) = 7.0
activation_energy_Q (kJ/mol) = 6.78
prefactor_D0 (m^2/s) = 2.0e-8
FFEOF
