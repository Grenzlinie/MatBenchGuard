#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: strain_profiles.csv ===
python3 << 'EOF'
import math
import csv
import os

# Ensure output directory exists
os.makedirs('/app/outputs', exist_ok=True)

# Material parameters
E1 = 200e9
M1 = 1e-6
H1 = 20e9
J1 = 1e-6
E2 = 100e9
M2 = 5e-7
H2 = 10e9
J2 = 5e-7
sigma = 300e6
sigma_y = 250e6

# Internal length scales
ell1 = math.sqrt(M1 / E1)
ell2 = math.sqrt(M2 / E2)
ell1p = math.sqrt(J1 / H1)
ell2p = math.sqrt(J2 / H2)

# Coupling coefficients for general case
Omega_e = (E2 - E1) / (E1 * ell1 + E2 * ell2)
Omega_p = (H2 - H1) / (H1 * ell1p + H2 * ell2p)

# Uniform grid
x_max = 5.0 * max(ell1, ell1p)
n = 500   # at least 500 points
xs = [i * 2.0 * x_max / (n - 1) - x_max for i in range(n)]

cases = ['general', 'case1', 'case2', 'case3']

with open('/app/outputs/strain_profiles.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['case', 'x', 'epsilon_e', 'epsilon_p'])
    for case in cases:
        for x in xs:
            if case == 'general':
                if x >= 0.0:
                    ee = (sigma / E1) * (1.0 - Omega_e * ell2 * math.exp(-x / ell1))
                    ep = ((sigma - sigma_y) / H1) * (1.0 - Omega_p * ell2p * math.exp(-x / ell1p))
                else:
                    ee = (sigma / E2) * (1.0 + Omega_e * ell1 * math.exp(x / ell2))
                    ep = ((sigma - sigma_y) / H2) * (1.0 + Omega_p * ell1p * math.exp(x / ell2p))
            elif case == 'case1':
                if x >= 0.0:
                    ee = (sigma / E1) * (1.0 - math.exp(-x / ell1))
                    ep = ((sigma - sigma_y) / H1) * (1.0 - math.exp(-x / ell1p))
                else:
                    ee = 0.0
                    ep = 0.0
            elif case == 'case2':
                if x > 0.0:
                    ee = sigma / E1
                    ep = (sigma - sigma_y) / H1
                else:
                    ee = 0.0
                    ep = 0.0
            elif case == 'case3':
                if x > 0.0:
                    ee = sigma / E1
                    ep = ((sigma - sigma_y) / H1) * (1.0 - math.exp(-x / ell1p))
                else:
                    ee = 0.0
                    ep = 0.0
            else:
                continue
            w.writerow([case, x, ee, ep])
EOF
