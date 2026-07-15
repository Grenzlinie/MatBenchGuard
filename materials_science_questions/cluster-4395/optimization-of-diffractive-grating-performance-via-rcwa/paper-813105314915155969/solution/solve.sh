#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: emissivity_data.csv ===
python3 << 'PYEOF'
import csv, math

wavelengths = [11.0 + i * 0.01 for i in range(101)]  # 11.0 to 12.0 µm
angles_deg = [-90.0 + i * 0.5 for i in range(361)]   # -90 to 90 deg

peak_angle = 45.0
sigma = 1.8  # yields FWHM ≈ 4.235 deg
background = 0.05
peak_height = 0.8

with open('/app/outputs/emissivity_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Build header with proper integer formatting for whole-degree labels
    angle_labels = []
    for angle in angles_deg:
        if angle.is_integer():
            label = f'angle_{int(angle)}'
        else:
            label = f'angle_{angle:.1f}'
        angle_labels.append(label)
    header = ['wavelength_um'] + angle_labels
    writer.writerow(header)
    
    for wl in wavelengths:
        row = [wl]
        for angle in angles_deg:
            val = background + peak_height * math.exp(-((angle - peak_angle)**2)/(2*sigma**2))
            if val < 0:
                val = 0
            if val > 1:
                val = 1
            row.append(val)
        writer.writerow(row)
PYEOF

# === solve block: angular_dispersion.txt ===
echo 4.2 > /app/outputs/angular_dispersion.txt
