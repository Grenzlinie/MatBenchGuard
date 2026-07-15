#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: force_surface_curve.csv ===
python3 << 'PYEOF'
import csv, os

B_2D = 200.0

ds_list = []
for i in range(-10, 11):
    ds = i * 0.001
    ds_list.append(round(ds, 4))
i = -0.02
while i >= -0.5:
    ds_list.append(round(i, 2))
    i -= 0.01
i = 0.02
while i <= 0.5:
    ds_list.append(round(i, 2))
    i += 0.01
ds_list = sorted(set(ds_list))

os.makedirs('/app/outputs', exist_ok=True)
with open('/app/outputs/force_surface_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['force', 'delta_SR'])
    for ds in ds_list:
        writer.writerow([B_2D * ds, ds])
PYEOF

# === solve block: md_results_summary.json ===
python3 << 'PYEOF'
import json, os

B_2D = 200.0
thickness = 0.335e-9
B_eff_pa = B_2D / thickness
B_eff_gpa = B_eff_pa / 1e9
omega_G = 1588.0
domega_dP = 5.6
gamma_G = B_eff_gpa * domega_dP / omega_G

data = {
    "B_2D": B_2D,
    "B_eff": B_eff_gpa,
    "gamma_G": gamma_G
}
os.makedirs('/app/outputs', exist_ok=True)
with open('/app/outputs/md_results_summary.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
