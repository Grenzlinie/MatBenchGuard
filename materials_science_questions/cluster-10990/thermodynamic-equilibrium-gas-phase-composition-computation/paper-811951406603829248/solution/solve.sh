#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reaction_controlled_rate.csv ===
python3 << 'PYEOF'
import math, csv

T_vals = [1273, 1373, 1473, 1573]
P_O2 = 1.51e-4   # atm
M_Cr = 52.00     # g/mol
M_CrO3 = 99.99   # g/mol

rows = []
for T in T_vals:
    log10_PCrO3 = -1.247e4 / T + 3.20 + 0.75 * math.log10(P_O2)
    P_CrO3 = 10.0 ** log10_PCrO3
    mass_flux_Cr = 44.35 * P_CrO3 * M_Cr / (math.sqrt(M_CrO3) * math.sqrt(T))
    rows.append([T, P_O2, mass_flux_Cr])

with open('/app/outputs/reaction_controlled_rate.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature_K', 'oxygen_pressure_atm', 'mass_flux_Cr_g_cm2_s'])
    w.writerows(rows)
PYEOF
