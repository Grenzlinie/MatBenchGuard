#!/usr/bin/env python3
"""Generate gamma_C_data.csv using the Wagner analysis with
regular‑solution temperature extrapolation."""
import csv
import math

OUTDIR = "/app/outputs"
OUTFILE = f"{OUTDIR}/gamma_C_data.csv"

# Interaction parameters at reference temperature T0 = 1000 °C (1273.15 K).
# Derived from Heckler & Winchell (1963) and Chipman & Brush (1968),
# converted to natural logarithm and mole‑fraction basis, with
# regular‑solution assumption for temperature extrapolation.
T0_K = 1273.15
ln_gamma_C0 = 0.712        # ln(gamma°_C) at T0
eps_Cr = -5.09             # ∂lnγ_C/∂X_Cr  (mole fraction)
eps_Ni = 2.5               # ∂lnγ_C/∂X_Ni  (mole fraction)

# Atomic masses (g/mol) – IUPAC standard
M_Cr = 51.9961
M_Ni = 58.6934
M_Fe = 55.845

def compute_x_cr_x_ni(wt_cr, wt_ni):
    """Convert weight percent to mole fractions (carbon neglected)."""
    wt_fe = 100.0 - wt_cr - wt_ni
    n_cr = wt_cr / M_Cr
    n_ni = wt_ni / M_Ni
    n_fe = wt_fe / M_Fe
    total = n_cr + n_ni + n_fe
    return n_cr/total, n_ni/total

def compute_gamma_c(wt_cr, wt_ni, t_celsius):
    """Return γ_C at given composition (wt%) and temperature (°C)."""
    x_cr, x_ni = compute_x_cr_x_ni(wt_cr, wt_ni)
    ln_1000 = ln_gamma_C0 + eps_Cr * x_cr + eps_Ni * x_ni
    t_k = t_celsius + 273.15
    ln_t = ln_1000 * (T0_K / t_k)
    return math.exp(ln_t)

def main():
    with open(OUTFILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["T_C", "Cr_wt", "Ni_wt", "gamma_C"])

        # Grid (a): Cr from 0 to 24 wt% step 2, Ni=10 wt%, T=500,600,700,800 °C
        for t_c in (500, 600, 700, 800):
            for cr_wt in range(0, 25, 2):
                gamma = compute_gamma_c(cr_wt, 10.0, t_c)
                writer.writerow([t_c, cr_wt, 10.0, f"{gamma:.6f}"])

        # Grid (b): Ni from 0 to 20 wt% step 2, Cr=5,10,18 wt%, T=600 °C
        for cr_wt in (5.0, 10.0, 18.0):
            for ni_wt in range(0, 21, 2):
                gamma = compute_gamma_c(cr_wt, ni_wt, 600.0)
                writer.writerow([600.0, cr_wt, ni_wt, f"{gamma:.6f}"])

if __name__ == "__main__":
    main()
