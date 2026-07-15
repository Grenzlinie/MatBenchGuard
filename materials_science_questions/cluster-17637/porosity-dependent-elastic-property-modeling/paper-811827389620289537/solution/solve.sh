#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json, math
x1 = 0.5
x2 = 2/3
den1 = (1-x1) + (4*x1)/(4 - math.pi*x1*x1)
num1_den2 = (1-x1) + x1*(4 - 0.667*math.pi*x1*x1)/(4 - math.pi*x1*x1)
r1 = den1 / num1_den2
den2 = (1-x2) + (4*x2)/(4 - math.pi*x2*x2)
num2_den2 = (1-x2) + x2*(4 - 0.667*math.pi*x2*x2)/(4 - math.pi*x2*x2)
r2 = den2 / num2_den2
data = {
    'hollow_ww_at_0': -0.5,
    'hollow_ww_at_pi2': 2.0,
    'water_ww_at_0': -5/6,
    'water_ww_at_pi2': 5/3,
    'internal_pressure_q': 2/3,
    'delta_L1_delta_L2_DL_0_5': r1,
    'delta_L1_delta_L2_DL_0_667': r2,
    'tension_hollow_ww_at_0': 0.5,
    'tension_water_ww_at_0': 0.5
}
with open('$OUTDIR/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
