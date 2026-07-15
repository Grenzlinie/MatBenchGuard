#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: power_factor_vs_concentration.csv ===
python3 << 'EOF'
import csv, math, os

k_B = 8.617333262145e-5  # eV/K
e_charge = 1.602176634e-19  # C
mu_SI = 100 * 1e-4         # 100 cm^2/Vs -> 0.01 m^2/Vs

def seebeck_approx(n_cm3):
    n = n_cm3 * 1e6
    m0 = 9.10938356e-31
    h = 6.62607015e-34
    m_d = 0.32 * m0
    N_c = 2 * (2*math.pi * m_d * k_B * 300 / (h**2))**1.5
    if n <= 0:
        return 0.0
    s = (k_B * 300) / e_charge * (2.0 - math.log(n / N_c))
    return abs(s) * 1e6  # µV/K

def power_factor(n_cm3):
    n = n_cm3 * 1e6
    sigma = n * e_charge * mu_SI
    S_VK = seebeck_approx(n_cm3) * 1e-6
    return sigma * S_VK * S_VK

samples = ['JL254', 'JL255', 'JL256']
concs = [1e17, 2e17, 5e17, 1e18, 2e18, 5e18, 1e19, 2e19, 5e19, 1e20, 2e20, 5e20, 1e21]

outfile = os.path.join(os.environ.get('OUTDIR', '/app/outputs'), 'power_factor_vs_concentration.csv')
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sample', 'carrier_concentration_cm3', 'power_factor_WmK2'])
    for s in samples:
        for n in concs:
            pf = power_factor(n)
            w.writerow([s, f'{n:.6e}', f'{pf:.8e}'])
EOF

# === solve block: seebeck_vs_temperature.csv ===
python3 /solution/generate_curves.py seebeck

# === solve block: conductivity_vs_temperature.csv ===
python3 /solution/generate_curves.py conductivity
