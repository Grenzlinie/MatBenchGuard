#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phasediagram.csv ===
python3 - << 'PYEOF'
import csv

# Computed from eq. (4) with k_inf=15, beta=1/3, rho0_M=0.160, f(E)=exp(-E), Tc_inf_half=3.199
# For E=10, f(E)~0 -> Tc = Tc_inf_half - k_inf * (0.5 - rho)^3
# For E=1,  f(E)=0.3679 -> Tc = Tc_inf_half - 15*0.3679*(0.5-0.16)^3 - 15*(1-0.3679)*(0.5-rho)^3

def compute_Tc(rho, E):
    if E == 10:
        return 3.199 - 15.0 * (0.5 - rho)**3
    else:  # E == 1
        const = 15.0 * 0.36787944117144233 * (0.5 - 0.16)**3
        return 3.199 - const - 15.0 * (1 - 0.36787944117144233) * (0.5 - rho)**3

densities = [0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]
fields = [1, 10]

rows = []
for rho in densities:
    for E in fields:
        Tc = compute_Tc(rho, E)
        rows.append([rho, E, round(Tc, 6)])

with open('/app/outputs/phasediagram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['density','field','Tc'])
    writer.writerows(rows)
PYEOF
