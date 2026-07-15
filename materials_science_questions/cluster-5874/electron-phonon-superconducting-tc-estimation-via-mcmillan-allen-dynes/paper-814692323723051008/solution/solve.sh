#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: calculated_properties.csv ===
python3 <<'PYEOF'
import math, csv, os

theta_D, theta_bp = 80.0, 3000.0
ln_ratio = math.log(theta_bp / theta_D)

systems = [
    ('K3C60', 0.2575, 0.1609, 0.14091, [0.0, 0.08, 0.33, 0.68, 1.02, 2.33]),
    ('Rb3C60', 0.4355, 0.1715, 0.1936, [0.0, 0.18, 0.58, 1.03, 1.50, 1.92]),
]

outdir = os.environ.get('OUTDIR', '/app/outputs')
outpath = os.path.join(outdir, 'calculated_properties.csv')

with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'pressure_GPa', 'Tc_K', 'alpha', 'beta', 'dTc_dP_K_GPa'])
    for syst, lam_ph0, lam_bp0, A, pressures in systems:
        for P in pressures:
            lam_ph = lam_ph0 * math.exp(-A * P)
            lam_bp = lam_bp0 * math.exp(-A * P)
            lam_bp_star = lam_bp / (1.0 - lam_bp * ln_ratio)
            lam_sum = lam_bp_star + lam_ph
            Tc = 1.14 * theta_D * math.exp(-1.0 / lam_sum)
            alpha = 0.5 * (1.0 - (1.0 + lam_ph * math.log(Tc / (1.14 * theta_D))) ** 2)
            beta = 4.0 / (1.14 - Tc / theta_D)
            dTc_dP = -A * Tc * (math.log(1.14 * theta_D / Tc) + (1.0 - 2.0 * alpha) * ln_ratio)
            w.writerow([syst, f'{P:.2f}', f'{Tc:.4f}', f'{alpha:.4f}', f'{beta:.4f}', f'{dTc_dP:.4f}'])
PYEOF
