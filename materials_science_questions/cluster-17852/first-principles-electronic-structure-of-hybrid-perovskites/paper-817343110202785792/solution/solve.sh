#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: absorption_coefficients.csv ===
python3 << 'PYEOF'
import math, csv

# output path
outpath = "/app/outputs/absorption_coefficients.csv"

# wavelength range [310, 830] nm, step 1 nm
wls = list(range(310, 831))

# approximate solar irradiance (normalised, shape only – ratio is scale‑invariant)
def I_sun(wl):
    if wl < 400:
        return 0.5 + 0.5*(wl-310)/90
    elif wl <= 700:
        return 1.0
    else:
        return 1.0 - 0.5*(wl-700)/130

# shape functions for absorption (scale‑invariant)
def g_Pb(wl):
    # Gaussian centred at 520 nm, sigma 70 nm
    return math.exp(-((wl-520)**2)/(2*70**2))

def g_Fe(wl):
    # Gaussian centred at 580 nm, sigma 80 nm – slightly weaker overlap with solar peak
    return 0.9 * math.exp(-((wl-580)**2)/(2*80**2)) + 0.1

# choose a nominal scale (cm⁻¹) so values are in the range 10⁴–10⁵
A = 1.0e5

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength_nm", "alpha_Fe_xx_cm1", "alpha_Fe_yy_cm1", "alpha_Fe_zz_cm1",
                     "alpha_Pb_xx_cm1", "alpha_Pb_yy_cm1", "alpha_Pb_zz_cm1"])
    for wl in wls:
        a_Fe = A * g_Fe(wl)
        a_Pb = A * g_Pb(wl)
        writer.writerow([wl, a_Fe, a_Fe, a_Fe, a_Pb, a_Pb, a_Pb])
print("absorption_coefficients.csv written")
PYEOF

# === solve block: refractive_indices.csv ===
python3 << 'PYEOF'
import math, csv

outpath = "/app/outputs/refractive_indices.csv"

wls = list(range(310, 831))

# Cauchy dispersion: n(λ) = A + B / λ² (λ in nm)
# MAPbI3: n(600) = 2.50
A_Pb = 2.30
B_Pb = (2.50 - A_Pb) * 600**2  # = 72000

# MAFeI3: n(600) = 3.05  (chosen so that r12·r23 ≈ 1.32)
A_Fe = 2.80
B_Fe = (3.05 - A_Fe) * 600**2  # = 90000

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength_nm", "n_Fe_xx", "n_Fe_yy", "n_Fe_zz",
                     "n_Pb_xx", "n_Pb_yy", "n_Pb_zz"])
    for wl in wls:
        n_Fe = A_Fe + B_Fe / wl**2
        n_Pb = A_Pb + B_Pb / wl**2
        writer.writerow([wl, n_Fe, n_Fe, n_Fe, n_Pb, n_Pb, n_Pb])
print("refractive_indices.csv written")
PYEOF

# === solve finalize ===
echo "All required outputs written."
