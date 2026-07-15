#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_simulated_reflectivity.csv ===
# Write step_01_simulated_reflectivity.csv
python3 - "$OUTDIR/step_01_simulated_reflectivity.csv" << 'PYEOF'
import math, csv, sys
out_path = sys.argv[1]
center = 1064.0
peak_r = 0.989
fwhm = 10.0
half_fwhm = fwhm / 2.0
wavelengths = range(1000, 1201)
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_nm', 'reflectivity'])
    for wl in wavelengths:
        r = peak_r / (1.0 + ((wl - center) / half_fwhm) ** 2)
        writer.writerow([wl, round(r, 6)])
PYEOF
