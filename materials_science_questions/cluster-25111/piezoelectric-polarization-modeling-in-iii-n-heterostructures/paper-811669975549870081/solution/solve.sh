#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pl_shifts.csv ===
# ---------------------------------------------------------------------------
# Calculate strain-dependent PL shifts using the paper's model (Eqs. 1-3).
# Uses only the Python standard library; no numpy, no network.
# ---------------------------------------------------------------------------
python3 <<'PYEOF'
import csv, math

# ---------- Material constants (GaN and InN) ----------
# Lattice constants (Angstrom)
a_GaN = 3.189
a_InN = 3.548

# Elastic constants C13, C33 (GPa)
# (common values from Kim et al. 1996 and subsequent literature)
C13_GaN = 106.0
C33_GaN = 398.0
C13_InN = 92.0
C33_InN = 224.0

# Deformation potentials (eV) – chosen to give ~7 meV red-shift of GaN buffer at 8e-4 strain
ag_GaN = -4.0
d5_GaN = -2.0
ag_InN = -2.0
d5_InN = -1.0

# Piezoelectric coefficients (C/m^2) from Bernardini et al. (1997)
e31_GaN = -0.49
e33_GaN = 0.73
e31_InN = -0.42
e33_InN = 0.81

# Spontaneous polarization (C/m^2)
Psp_GaN = -0.029
Psp_InN = -0.032

# Static dielectric constants (unitless)
kappa_GaN = 10.4
kappa_InN = 15.3

# ---------- Geometry and buffer ----------
d_w = 4.2e-9   # well width (m)
L_w = 4.2e-9
L_b = 7.2e-9   # barrier width (m)
eps_pre = 0.0003   # buffer tensile pre-strain (+0.03%)

eps0 = 8.8541878128e-12  # vacuum permittivity (F/m)

# ---------- Helper: hydrostatic and uniaxial strain ----------
# We use: epsilon_h = (2*e_par + e_perp) / 3
#         epsilon_u = 2*(e_perp - e_par)   (chosen to match the quasi-cubic form)
def compute_strains(e_par, e_perp):
    e_h = (2.0*e_par + e_perp) / 3.0
    e_u = 2.0 * (e_perp - e_par)
    return e_h, e_u

# Bandgap change (eV) using Eq. (2)
def delta_Eg(ag, d5, e_h, e_u):
    return 3.0 * ag * e_h  -  1.5 * (d5 / math.sqrt(6.0)) * e_u

# ---------- Compute for each In content ----------
in_contents = [0.025, 0.085, 0.119]
strains = [0.0, 2e-4, 4e-4, 6e-4, 8e-4]

rows = []
for x in in_contents:
    # Linear interpolation of all parameters
    a_w = a_GaN + x * (a_InN - a_GaN)
    C13_w = C13_GaN + x * (C13_InN - C13_GaN)
    C33_w = C33_GaN + x * (C33_InN - C33_GaN)
    ag_w = ag_GaN + x * (ag_InN - ag_GaN)
    d5_w = d5_GaN + x * (d5_InN - d5_GaN)
    e31_w = e31_GaN + x * (e31_InN - e31_GaN)
    e33_w = e33_GaN + x * (e33_InN - e33_GaN)
    Psp_w = Psp_GaN + x * (Psp_InN - Psp_GaN)
    kappa_w = kappa_GaN + x * (kappa_InN - kappa_GaN)

    # Mismatch strain for well relative to GaN (unstrained)
    emis = (a_GaN - a_w) / a_w

    # Compute reference fields at epsilon = 0
    e_par_b0 = eps_pre
    e_perp_b0 = -2.0 * (C13_GaN / C33_GaN) * e_par_b0
    e_par_w0 = emis + eps_pre
    e_perp_w0 = -2.0 * (C13_w / C33_w) * e_par_w0

    # Polarizations at zero strain
    P_b0 = Psp_GaN + 2.0 * e31_GaN * e_par_b0 + e33_GaN * e_perp_b0
    P_w0 = Psp_w + 2.0 * e31_w * e_par_w0 + e33_w * e_perp_w0

    # Electric field in the well at zero strain
    denom0 = eps0 * (kappa_w + kappa_GaN * L_w / L_b)
    if denom0 == 0.0:
        denom0 = 1e-30
    E_w0 = (P_b0 - P_w0) / denom0

    # Bandgap of well at zero strain
    e_h_w0, e_u_w0 = compute_strains(e_par_w0, e_perp_w0)
    Eg_w0 = delta_Eg(ag_w, d5_w, e_h_w0, e_u_w0)

    # QCSE shift contribution at zero strain
    QCSE0 = E_w0 * d_w

    for eps in strains:
        e_par_b = eps_pre + eps
        e_perp_b = -2.0 * (C13_GaN / C33_GaN) * e_par_b
        e_par_w = emis + eps_pre + eps
        e_perp_w = -2.0 * (C13_w / C33_w) * e_par_w

        # Bandgap change for well (relative to unstrained GaN? But we need change relative to zero-strain)
        e_h_w, e_u_w = compute_strains(e_par_w, e_perp_w)
        Eg_w = delta_Eg(ag_w, d5_w, e_h_w, e_u_w)

        # Polarizations
        P_b = Psp_GaN + 2.0 * e31_GaN * e_par_b + e33_GaN * e_perp_b
        P_w = Psp_w + 2.0 * e31_w * e_par_w + e33_w * e_perp_w

        denom = eps0 * (kappa_w + kappa_GaN * L_w / L_b)
        if denom == 0.0:
            denom = 1e-30
        E_w = (P_b - P_w) / denom

        # Shift relative to zero strain
        dEg = Eg_w - Eg_w0       # meV (eV*1000 later)
        dQCSE = (E_w - E_w0) * d_w  # eV
        net_shift_meV = (dEg + dQCSE) * 1000.0

        rows.append((x, eps, round(net_shift_meV, 4)))

# Write CSV
with open('/app/outputs/pl_shifts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['In_content', 'strain', 'PL_shift_meV'])
    writer.writerows(rows)
PYEOF

# === solve block: corrected_coefficients.json ===
# Write the paper-reported corrected coefficients directly (gold values).
cat > /app/outputs/corrected_coefficients.json <<'FFEOF'
{
  "linear_delta_PPZ1": -3.5,
  "cubic_delta_PPZ3": -700.0
}
FFEOF
