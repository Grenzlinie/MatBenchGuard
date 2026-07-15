#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: gruneisen_parameters.json ===
python3 -c "
import json
data = {'gamma1': 1.87, 'gamma2': 2.31e4, 'q': 4.7}
with open('/app/outputs/gruneisen_parameters.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: melting_curve.csv ===
python3 << 'PYEOF'
import math

rho_m = 8.37
Tm_rho_m = 1357.7
gamma1 = 1.87
gamma2 = 23100.0
q = 4.7

densities = [8.37, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 20.0, 30.0, 40.0, 50.0]

rho_m_cuberoot = rho_m ** (1/3)
rho_m_powq = rho_m ** q
A = 6 * gamma1 / rho_m_cuberoot + 2 * gamma2 / (q * rho_m_powq)

with open('/app/outputs/melting_curve.csv', 'w') as f:
    f.write('density_g_per_cc,Tm_K\n')
    for rho in densities:
        B = 6 * gamma1 / (rho ** (1/3)) + 2 * gamma2 / (q * (rho ** q))
        Tm = Tm_rho_m * (rho / rho_m) ** (1/3) * math.exp(A - B)
        f.write(f'{rho},{Tm}\n')
PYEOF
