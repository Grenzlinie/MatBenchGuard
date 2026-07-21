#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: superposition_errors.csv ===
python3 << 'PYEOF'
import csv, math

# Fixed input parameters
A_c = 1.0
phi_c = 0.0
phi_1 = math.pi / 6.0
t_u = 1.0e-5
t_d = 1.01e-5
m_c = 0.1

# Assembly amplitude ratios
assemblies = [
    ("fluoroplastic", 0.09),
    ("metal", 0.225)
]

frequencies_MHz = [1.0, 2.0, 4.0]  # MHz

# Undisturbed frequency difference
Delta_f = 1.0/t_u - 1.0/t_d

rows = []
for atype, A1 in assemblies:
    A = math.sqrt(A_c**2 + A1**2 + 2*A_c*A1*math.cos(phi_c - phi_1))
    # Composite phase φ
    numer = A_c*math.sin(phi_c) + A1*math.sin(phi_1)
    denom = A_c*math.cos(phi_c) + A1*math.cos(phi_1)
    phi = math.atan2(numer, denom)
    m = m_c * A_c / A   # since A_c=1 => m = m_c / A
    for f_MHz in frequencies_MHz:
        f = f_MHz * 1e6
        # Phase-induced time shift
        td_prime = (phi - phi_c) / (2*math.pi*f)
        Delta_f_prime = 1.0/t_u - 1.0/(t_d + td_prime)
        delta_prime = (Delta_f - Delta_f_prime) / Delta_f
        # Amplitude-induced time shift
        td_double_prime = (math.asin(m_c) - math.asin(m)) / (2*math.pi*f)
        Delta_f_double_prime = 1.0/t_u - 1.0/(t_d + td_double_prime)
        delta_double_prime = (Delta_f - Delta_f_double_prime) / Delta_f
        rows.append([atype, f_MHz, delta_prime, delta_double_prime])

# Write CSV
with open("/app/outputs/superposition_errors.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["assembly_type", "frequency_MHz", "delta_prime", "delta_double_prime"])
    writer.writerows(rows)
PYEOF
