#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivity_results.csv ===
cat > /tmp/compute.py << 'PYEOF'
import math, csv

T = 300.0
omega_D1 = 2.66e14
hbar = 1.054571817e-34
kB = 1.380649e-23
theta = hbar * omega_D1 / kB
Theta = T / theta

L = 10.0  # in um

# Ideal graphene parameters
A1 = 1310.0 / (0.573 + L**(-0.45))
A2 = 3.0 / (26.0 * L**0.07) - 0.0594
A3 = 5.0 / (121.0 * L**0.35) - 0.005

kappa_I = A1 * Theta**2 / ((Theta + A2)**3 + A3**2)

# Defect term parameters
B1 = -14.9 * L**(7.0/13.0) + 1711.0 / (11.0 - math.log(L)) - 107.0
B2 = 46.5 * (L - 153.0) / (L**0.5 + 8.0) + 913.0
B3 = 13.6 * L**0.42 - 3.7 * math.log(L) - 16.8

def kappa_doped(mu, n):
    kappa_D = B1 * math.sqrt(Theta) + B2 * mu * n**0.53 + B3
    return 1.0 / (1.0 / kappa_I + mu**2 * n / kappa_D)

# Conditions
ideal_kappa = kappa_I
Al_kappa = kappa_doped(1.25, 0.01)
N_kappa  = kappa_doped(0.1667, 0.01)

with open('/app/outputs/thermal_conductivity_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['condition', 'kappa_W_mK'])
    writer.writerow(['ideal', format(ideal_kappa, '.1f')])
    writer.writerow(['doped_Al', format(Al_kappa, '.1f')])
    writer.writerow(['doped_N', format(N_kappa, '.1f')])
PYEOF
python3 /tmp/compute.py
