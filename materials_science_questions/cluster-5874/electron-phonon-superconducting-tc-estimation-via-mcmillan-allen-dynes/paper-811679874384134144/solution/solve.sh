#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hopfield_eta.csv ===
# Write hopfield_eta.csv
cat > "/app/outputs/hopfield_eta.csv" <<'FFEOF'
lattice_constant,pressure_gpa,eta_total_eV_Ang2
4.60,307,14.588
FFEOF

# === solve block: tc_vs_params.csv ===
# Compute and write tc_vs_params.csv
python3 <<'PYEOF'
import csv
import math

# Constants from the paper
eta_eV_Ang2 = 14.588
m_u = 10.811
ha_eV = 27.2114
bohr_ang = 0.529177
m_e_u = 1822.888
k_ha = 1.0 / 315775.0

# Convert to atomic units
eta_au = eta_eV_Ang2 / ha_eV * (bohr_ang ** 2)
m_au = m_u * m_e_u

def compute_lambda(omega_K):
    omega_au = omega_K * k_ha
    return eta_au / (m_au * omega_au**2)

def compute_Tc(omega_K, mu_star):
    lam = compute_lambda(omega_K)
    denominator = lam - mu_star * (1.0 + 0.62 * lam)
    if denominator <= 0:
        return 0.0
    exponent = -1.04 * (1.0 + lam) / denominator
    Tc = (omega_K / 1.45) * math.exp(exponent)
    return Tc

# Generate output
omega_values = range(1200, 1450, 50)
mu_values = [x/100.0 for x in range(9, 14)]

with open('/app/outputs/tc_vs_params.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['omega_K', 'mu_star', 'Tc_K'])
    for omega in omega_values:
        for mu in mu_values:
            Tc = compute_Tc(omega, mu)
            writer.writerow([omega, mu, f"{Tc:.2f}"])
PYEOF

# === solve finalize ===
# Finalize: no extra steps needed
echo "Oracle artifacts generated successfully."
