#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_defect_levels.csv ===
python3 <<'PYEOF'
import math
eps_Si = 0.24
beta = -0.39
metals = [('Ni', 5.39), ('Pd', 5.35), ('Pt', 5.08)]
with open('/app/outputs/step_01_defect_levels.csv', 'w') as f:
    f.write('metal,defect_level_eV\n')
    for metal, eps_metal in metals:
        V = eps_metal - eps_Si
        term = math.sqrt(4*beta*beta + beta*V + (V*V)/4.0)
        E_minus = eps_Si + beta + V/2.0 - term
        f.write(f'{metal},{E_minus:.6f}\n')
PYEOF
