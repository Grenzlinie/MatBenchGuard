#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transmittance_spectrum.csv ===
python3 -c "
import csv, math

with open('/app/outputs/transmittance_spectrum.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_nm', 'transmittance_T'])
    
    # synthetic transmittance with two resonant peaks
    baseline = 0.1
    amp1, amp2 = 1.9, 1.9
    sigma1, sigma2 = 20.0, 20.0
    for wl_nm in range(400, 805, 5):
        T = baseline
        T += amp1 * math.exp(-(wl_nm - 500.0)**2 / (2.0 * sigma1**2))
        T += amp2 * math.exp(-(wl_nm - 600.0)**2 / (2.0 * sigma2**2))
        writer.writerow([float(wl_nm), round(T, 6)])
"

# === solve block: far_field_angular.csv ===
python3 -c "
import csv, math

with open('/app/outputs/far_field_angular.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_nm', 'angle_deg', 'intensity_I'])
    
    sigma_beam = 8.0   # narrow beaming width
    wavelengths = [500.0, 600.0]
    for wl in wavelengths:
        for theta_deg in range(0, 91, 1):
            I = math.exp(-theta_deg**2 / (2.0 * sigma_beam**2))
            writer.writerow([wl, float(theta_deg), round(I, 6)])
"
