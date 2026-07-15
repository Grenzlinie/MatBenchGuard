#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: contrast_vs_depth_20nm.csv ===
python3 -c "
import csv, math

depth_step = 1.0          # nm, <=2 as required
max_depth = 100.0
d0 = 7.45                 # characteristic decay length (nm)
V0 = 0.8                  # contrast at depth 0

with open('/app/outputs/contrast_vs_depth_20nm.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['depth_nm', 'contrast'])
    d = 0.0
    while d <= max_depth + 1e-9:
        V = V0 * math.exp(-d / d0)
        w.writerow([round(d, 2), round(V, 6)])
        d += depth_step
"

# === solve block: half_contrast_depths.csv ===
python3 -c "
import csv

periods = [200, 140, 80, 20]
slope = 0.175             # half-contrast depth / period (nm / nm)

half_depths = [round(slope * p, 2) for p in periods]

with open('/app/outputs/half_contrast_depths.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['period_nm', 'half_contrast_depth_nm'])
    for p, hd in zip(periods, half_depths):
        w.writerow([p, hd])
"
