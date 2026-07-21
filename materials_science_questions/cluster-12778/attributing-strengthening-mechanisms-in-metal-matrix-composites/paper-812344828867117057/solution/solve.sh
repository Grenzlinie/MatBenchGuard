#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: nucleation_work_results.json ===
python3 -c "
import math, json
theta1 = math.radians(94)
theta2 = math.radians(45)
ratio1 = (2 - 3*math.cos(theta1) + math.cos(theta1)**3) / 4
ratio2 = (2 - 3*math.cos(theta2) + math.cos(theta2)**3) / 4
reduction = (ratio1 - ratio2) / ratio1 * 100
data = {
    'wetting_angle_Al2O3': 94,
    'nucleation_work_ratio_Al2O3': ratio1,
    'wetting_angle_NiAl2O3': 45,
    'nucleation_work_ratio_NiAl2O3': ratio2,
    'reduction_percent': reduction
}
with open('$OUTDIR/nucleation_work_results.json', 'w') as f:
    json.dump(data, f, indent=2)
print('nucleation_work_results.json written.')
"
