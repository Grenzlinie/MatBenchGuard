#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reflection_spectra.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 << 'PYEOF'
import csv, math

wavelengths = [1500.0 + i*0.1 for i in range(int((1600.0-1500.0)/0.1)+1)]

def gauss(x, mu, sigma):
    return math.exp(-((x-mu)**2)/(2.0*sigma*sigma))

def reflectivity_spectrum(wls, peaks, amp=0.97, sigma=1.5, background=0.03):
    r = [background for _ in wls]
    for p in peaks:
        for idx, w in enumerate(wls):
            r[idx] += amp * gauss(w, p, sigma)
    return r

front_peaks = [1522.3, 1550.0, 1577.7]
rear_peaks = [1527.2, 1550.0, 1572.8]

front_ref = reflectivity_spectrum(wavelengths, front_peaks)
rear_ref = reflectivity_spectrum(wavelengths, rear_peaks)

with open('/app/outputs/reflection_spectra.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_nm', 'front_reflectivity', 'rear_reflectivity'])
    for i, w in enumerate(wavelengths):
        writer.writerow([w, front_ref[i], rear_ref[i]])
PYEOF
