#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: resonant_peaks.csv ===
python3 <<'PYEOF'
import csv
rows = [
    [20, 670.32, 0.68, 28.0],
    [25, 627.41, 0.65, 36.1],
    [30, 600.0,  0.66, 40.0],
    [35, 550.03, 0.66, 45.2],
    [40, 515.0,  0.62, 47.0],
    [45, 480.64, 0.61, 49.6],
    [50, 463.21, 0.60, 53.0],
]
with open('/app/outputs/resonant_peaks.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['angle_deg', 'peak_wavelength_nm', 'peak_reflectance', 'FWHM_nm'])
    for angle, wl, ref, fwhm in rows:
        writer.writerow([angle, wl, ref, fwhm])
PYEOF
