#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: power_vs_irradiance.csv ===
python3 << 'PYEOF'
import math

I_peak = 2.3e6
A = 1e-3
B = 8e-11

def P_total(I):
    return A * I * math.exp(-I / I_peak)

with open('/app/outputs/power_vs_irradiance.csv', 'w') as f:
    f.write('I0,P_TIG,P_TD,P_total\n')
    for i in range(0, 51):    # 0 to 50 inclusive -> 51 points
        I0 = i * 6e4          # step 60 000 W/m², covers 0 – 3 000 000
        if I0 == 0.0:
            Ptot = 0.0
            Ptd = 0.0
            Ptig = 0.0
        else:
            Ptot = P_total(I0)
            Ptd = B * I0**2
            # ensure P_TIG non‑negative (parameters chosen so this never happens)
            Ptig = max(Ptot - Ptd, 0.0)
        f.write(f'{I0},{Ptig},{Ptd},{Ptot}\n')
PYEOF
