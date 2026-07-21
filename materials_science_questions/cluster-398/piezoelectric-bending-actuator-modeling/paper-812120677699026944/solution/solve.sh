#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_hole_results.csv ===
python3 << 'PYEOF'
import json, csv, os
with open('/solution/hole_data.json') as f:
    data = json.load(f)
with open('/app/outputs/step_01_hole_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['angle_deg', 'sigma_normalized', 'D_normalized'])
    for row in data:
        w.writerow([row['angle_deg'], row['sigma_normalized'], row['D_normalized']])
PYEOF

# === solve block: step_02_actuator_results.csv ===
python3 << 'PYEOF'
import json, csv, os
with open('/solution/actuator_data.json') as f:
    data = json.load(f)
with open('/app/outputs/step_02_actuator_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x_over_H', 'Ex_field', 'sigma_yy'])
    for row in data:
        w.writerow([row['x_over_H'], row['Ex_field'], row['sigma_yy']])
PYEOF
