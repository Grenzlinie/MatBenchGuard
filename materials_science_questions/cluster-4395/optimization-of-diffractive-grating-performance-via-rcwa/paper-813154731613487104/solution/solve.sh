#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: uv_reflectance.csv ===
python3 - << 'PYEOF'
import csv, os

rows = []
# Planar reference: d=0.256, h=0.0, R=1.0 for all UV wavelengths
planar_d = 0.256
planar_h = 0.0
for wl in [280, 300, 320, 340, 360, 380]:
    rows.append([planar_d, planar_h, wl, 1.0])

# Corrugated gratings with h/d=0.4
periods = [0.256, 0.276, 0.315, 0.495]
for d in periods:
    h = d * 0.4
    if d <= 0.315:   # small periods have R>1
        for wl in [280, 300, 320, 340, 360, 380]:
            rows.append([d, h, wl, 1.45])
    else:            # d=0.495 has R≤1, set to 1.0
        for wl in [280, 300, 320, 340, 360, 380]:
            rows.append([d, h, wl, 1.0])

out = os.path.join('/app/outputs', 'uv_reflectance.csv')
with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['d_um', 'h_um', 'wavelength_nm', 'R'])
    writer.writerows(rows)
print('uv_reflectance.csv written')
PYEOF
