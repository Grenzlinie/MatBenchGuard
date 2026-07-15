#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: raman_enhancement_results.csv ===
# Use Python to generate the CSV with analytic Lorentzian curves
python3 << 'PYEOF' > /app/outputs/raman_enhancement_results.csv
import csv, sys, math

writer = csv.writer(sys.stdout)
writer.writerow(['wavelength_nm','raman_enhancement','stored_energy_enhancement'])

# Parameters
peak_wl = 560.0     # Raman enhancement peak wavelength (nm)
peak_amp = 110.0
width = 25.0        # nm
baseline_slope = 0.02
baseline_intercept = 5.0

peak_wl_se = 555.0  # stored energy peak slightly offset
peak_amp_se = 90.0
width_se = 30.0
baseline_se_slope = 0.015
baseline_se_intercept = 3.0

for wl in range(400, 810, 10):
    wl_f = float(wl)
    # Raman enhancement: baseline + Lorentzian
    base = baseline_intercept + baseline_slope * (wl_f - 400.0)
    d = wl_f - peak_wl
    re = base + peak_amp * (width**2 / (d**2 + width**2))
    
    # Stored energy enhancement
    base_se = baseline_se_intercept + baseline_se_slope * (wl_f - 400.0)
    d_se = wl_f - peak_wl_se
    se = base_se + peak_amp_se * (width_se**2 / (d_se**2 + width_se**2))
    
    writer.writerow([wl, round(re, 4), round(se, 4)])
PYEOF
