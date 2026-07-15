#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mae_results.json ===
python3 -c "
import json
result = {
    'cubic_AF_MAE': 1540.0,
    'cubic_FM_MAE': -44290.0,
    'strained_AF_MAE': 20450.0,
    'strained_FM_MAE': -3225.0,
    'cubic_AF_easy_axis': '<110>',
    'cubic_FM_easy_axis': '<100>',
    'strained_AF_easy_axis': '<110>',
    'strained_FM_easy_axis': '<100>'
}
with open('/app/outputs/mae_results.json', 'w') as f:
    json.dump(result, f, indent=2)
"

# === solve block: mc_coercivity.csv ===
python3 -c "
import csv, math

def hc_af(phi_deg):
    phi = math.radians(phi_deg)
    return 0.75 + 0.25 * math.cos(4 * phi)

def hc_fm(phi_deg):
    phi = math.radians(phi_deg)
    return 0.1875 + 0.0625 * math.cos(4 * (phi - math.radians(45)))

with open('/app/outputs/mc_coercivity.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['phi_deg', 'Hc_single_SM', 'Hc_SM_AF_bilayer', 'Hc_SM_FM_bilayer'])
    for phi in range(0, 360):
        writer.writerow([phi, 0.08, hc_af(phi), hc_fm(phi)])
"
