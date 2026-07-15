#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: yield_strength_components.csv ===
python3 - <<'PYEOF'
import csv, os

rows = [
    # (form, condition, sigma_s_min, sigma_s_max, sigma_g, sigma_d_min, sigma_d_max, sigma_y_min, sigma_y_max,
    #  delta_sigma_g, delta_sigma_d_min, delta_sigma_d_max, delta_sigma_y_min, delta_sigma_y_max)
    # Absolute rows (delta columns empty)
    ['CR', 'before_EFA', 107, 109, 187, 86, 106, 410, 432, '', '', '', '', ''],
    ['CR', 'after_EFA', 107, 109, 170, 51, 62, 358, 371, '', '', '', '', ''],
    ['HR', 'before_EFA', 95, 97, 202, 71, 87, 398, 416, '', '', '', '', ''],
    ['HR', 'after_EFA', 95, 97, 179, 51, 63, 355, 369, '', '', '', '', ''],
    # Delta rows (sigma columns empty)
    ['CR', 'delta', '', '', '', '', '', '', '', -17, -44, -35, -61, -52],
    ['HR', 'delta', '', '', '', '', '', '', '', -23, -24, -20, -47, -43],
]

columns = [
    'form', 'condition',
    'sigma_s_min', 'sigma_s_max', 'sigma_g', 'sigma_d_min', 'sigma_d_max', 'sigma_y_min', 'sigma_y_max',
    'delta_sigma_g', 'delta_sigma_d_min', 'delta_sigma_d_max', 'delta_sigma_y_min', 'delta_sigma_y_max'
]

outpath = '/app/outputs/yield_strength_components.csv'
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)

print(f'Wrote {outpath}')
PYEOF
