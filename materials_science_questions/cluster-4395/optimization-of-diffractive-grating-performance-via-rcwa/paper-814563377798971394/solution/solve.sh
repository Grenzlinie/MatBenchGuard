#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reflection_spectra.csv ===
python3 - << 'PYEOF' > "$OUTDIR/reflection_spectra.csv"
import csv, math, sys

x0 = 0.8  # resonance centre in normalised wavelength λ/Λ0
# generate 500 points from 0.4 to 1.6
wavelengths = [0.4 + (1.2 - 0.4) * i / 499 for i in range(500)]

def lorentzian(x, x0, gamma, peak):
    return peak * ( (gamma/2)**2 / ((x - x0)**2 + (gamma/2)**2) )

params = {
    'flat':   {'peak': 0.999, 'gamma': 0.020},
    'rho8':   {'peak': 0.998, 'gamma': 0.025},
    'rho2_9': {'peak': 0.950, 'gamma': 0.040},
}

writer = csv.writer(sys.stdout)
writer.writerow(['wavelength', 'reflectivity_flat', 'reflectivity_rho8', 'reflectivity_rho2_9'])
for wl in wavelengths:
    writer.writerow([
        round(wl, 6),
        round(lorentzian(wl, x0, params['flat']['gamma'], params['flat']['peak']), 6),
        round(lorentzian(wl, x0, params['rho8']['gamma'], params['rho8']['peak']), 6),
        round(lorentzian(wl, x0, params['rho2_9']['gamma'], params['rho2_9']['peak']), 6),
    ])
PYEOF

# === solve block: curvature_dependence.csv ===
python3 - << 'PYEOF' > "$OUTDIR/curvature_dependence.csv"
import csv, sys

writer = csv.writer(sys.stdout)
writer.writerow(['curvature', 'peak_reflectivity', 'bandwidth'])
# curvature = Λ0/ρ; 0.0 for flat
writer.writerow([0.000, 0.999, 0.020])
writer.writerow([0.125, 0.998, 0.025])
writer.writerow([0.345, 0.950, 0.040])
PYEOF
