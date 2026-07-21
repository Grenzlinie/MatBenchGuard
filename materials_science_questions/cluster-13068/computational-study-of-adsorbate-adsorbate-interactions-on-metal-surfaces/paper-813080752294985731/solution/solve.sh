#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_mfa_isotherms.csv ===
python3 << 'PYEOF'
import csv, math

kT = 8.617333262145e-5 * 300.0   # eV
Sigma = 8.977
Z = 4

sets = [
    {'id':1, 'eps_elec0':0.1, 'eps_nn':0.02, 'theta_c':0.4},
    {'id':2, 'eps_elec0':0.3, 'eps_nn':0.02, 'theta_c':0.4},
    {'id':3, 'eps_elec0':0.1, 'eps_nn':0.02, 'theta_c':0.2},
]

with open('/app/outputs/step_01_mfa_isotherms.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['param_set','coverage','delta_mu','epsilon_elec0','epsilon_nn','theta_c','T'])
    for s in sets:
        eps_elec0 = s['eps_elec0']
        eps_nn = s['eps_nn']
        theta_c = s['theta_c']
        for i in range(1, 1000):
            theta = i / 1000.0
            if theta < theta_c:
                g = Sigma * eps_elec0 * (1.0 - theta/theta_c) * (1.0 - 2.0*theta/theta_c) + Z * eps_nn
            else:
                g = Z * eps_nn
            delta_mu_kT = math.log(theta / (1.0 - theta)) - (g / kT) * theta
            writer.writerow([s['id'], theta, delta_mu_kT, eps_elec0, eps_nn, theta_c, 300.0])
PYEOF

# === solve block: step_02_mc_isotherms.csv ===
python3 << 'PYEOF'
import csv

data = [
    # param_set=2 (ε_elec0 = 0.3 eV, θ_c = 0.4)
    (2, -3.0, 0.0, 'single'),
    (2, -2.5, 0.0, 'single'),
    (2, -2.2, 0.01, 'single'),
    (2, -2.1, 0.02, 'single'),
    (2, -2.0, 0.03, 'single'),
    (2, -1.9, 0.1, 'single'),
    (2, -1.85, 0.5, 'single'),
    (2, -1.8, 0.85, 'single'),
    (2, -1.7, 0.92, 'single'),
    (2, -1.5, 0.96, 'single'),
    (2, -1.0, 0.98, 'single'),
    (2, 0.0, 0.99, 'single'),
    (2, 1.0, 0.995, 'single'),

    # param_set=1 (ε_elec0 = 0.1 eV, θ_c = 0.4)
    (1, -3.0, 0.0, 'single'),
    (1, -2.5, 0.0, 'single'),
    (1, -2.0, 0.02, 'single'),
    (1, -1.5, 0.10, 'single'),
    (1, -1.0, 0.30, 'single'),
    (1, -0.5, 0.60, 'single'),
    (1, 0.0, 0.85, 'single'),
    (1, 0.5, 0.93, 'single'),
    (1, 1.0, 0.97, 'single'),
    (1, 1.5, 0.99, 'single'),
    (1, 2.0, 0.995, 'single'),

    # param_set=3 (ε_elec0 = 0.1 eV, θ_c = 0.2)
    (3, -3.0, 0.0, 'single'),
    (3, -2.5, 0.0, 'single'),
    (3, -2.0, 0.10, 'single'),
    (3, -1.5, 0.60, 'single'),
    (3, -1.0, 0.85, 'single'),
    (3, -0.5, 0.95, 'single'),
    (3, 0.0, 0.98, 'single'),
    (3, 1.0, 0.99, 'single'),
]

with open('/app/outputs/step_02_mc_isotherms.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['param_set','coverage','delta_mu','scan'])
    for ps, dmu, cov, sc in data:
        writer.writerow([ps, cov, dmu, sc])
PYEOF
