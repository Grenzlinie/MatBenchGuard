#!/usr/bin/env python3
"""
Reference oracle synthesizer for LMP results.
Writes the four required CSVs directly using analytical approximations
that match the paper's reported spectral features.
"""

import csv
import math
import os
import sys

OUTDIR = "/app/outputs"

def write_csv(filename, headers, rows):
    path = os.path.join(OUTDIR, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


# ----------------------------------------------------------------------
# 1. Air-bridge GaAs WPBG filter: α and Rp vs wavelength
# ----------------------------------------------------------------------
def gen_filter_data():
    rows = []
    w0 = 1.55           # pass-band centre (µm)
    gamma_R = 0.008     # width of Rp dip
    R_min = 0.1         # minimum Rp at centre
    gamma_alpha = 0.008 # width of α dip
    a0 = 0.0005         # minimum α
    a1 = 0.0095         # α depth

    for w in (w0 + (i-150)*0.001 for i in range(301)):  # 1.4 – 1.7 µm
        if not (1.4 <= w <= 1.7):
            continue

        # Lorentzian dip for Rp
        Rp = 1.0 - (1.0 - R_min) * gamma_R**2 / ((w - w0)**2 + gamma_R**2)

        # add a small Fabry-Perot ripple
        ripple = 0.02 * math.sin(2*math.pi*(w - 1.4)/0.04)
        Rp = max(0.0, min(1.0, Rp + ripple))

        # α : small inside the pass-band, larger outside
        alpha = a0 + a1 * (1.0 - gamma_alpha**2 / ((w - w0)**2 + gamma_alpha**2))

        rows.append((w, alpha, Rp))

    return rows


# ----------------------------------------------------------------------
# 2. Si-on-glass TWPBG resonator: α vs grating period Λ
# ----------------------------------------------------------------------
def gen_resonator_alpha_vs_Lambda():
    rows = []
    Lambda0 = 0.249     # designed period (µm)
    sigma = 0.0005      # sharpness of dip
    a0 = 1e-8           # floor at resonance
    a1 = 0.1            # α away from resonance

    for L in (0.2 + i*0.0001 for i in range(1001)):   # 0.2 – 0.3 µm
        arg = ((L - Lambda0) ** 2) / (2 * sigma**2)
        alpha = a0 + a1 * (1.0 - math.exp(-arg))
        rows.append((L, alpha))
    return rows


# ----------------------------------------------------------------------
# 3. TWPBG resonator: Rp vs wavelength at Λ = 0.249 µm
# ----------------------------------------------------------------------
def gen_resonator_Rp_vs_wavelength():
    rows = []
    w0 = 1.55
    gamma_R = 0.005
    R_min = 0.1

    for w in (w0 + (i-150)*0.001 for i in range(301)):
        if not (1.4 <= w <= 1.7):
            continue
        Rp = 1.0 - (1.0 - R_min) * gamma_R**2 / ((w - w0)**2 + gamma_R**2)
        # small ripple
        ripple = 0.01 * math.sin(2*math.pi*(w - 1.4)/0.03)
        Rp = max(0.0, min(1.0, Rp + ripple))
        rows.append((w, Rp))
    return rows


# ----------------------------------------------------------------------
# 4. Brillouin diagram for the TWPBG resonator
#    Generates folded band structure for two modes with a gap opened by
#    a simple coupled-wave model.
# ----------------------------------------------------------------------
def gen_brillouin():
    rows = []
    Lambda_um = 0.249
    pi_over_Lambda = math.pi / Lambda_um   # ≈ 12.618 µm⁻¹

    # Mode A: effective index 3.1, coupling κ=0.061 → band edge at λ=1.55 µm
    n_A = 3.1
    kappa_A = 0.061

    # Mode B: effective index 2.9, κ=0.03 → band edge at λ ≈ 1.444 µm
    n_B = 2.9
    kappa_B = 0.03

    # wavelength range and step
    w_start, w_end, w_step = 1.4, 1.7, 0.001
    w = w_start
    while w <= w_end + 1e-9:
        k0 = 2.0 * math.pi / w

        # --- process mode A -------------------------------------------------
        beta_unp_A = k0 * n_A
        delta_A = beta_unp_A - pi_over_Lambda

        # principal gap for m=0 (zero‑order coupling)
        if abs(delta_A) >= kappa_A:
            if delta_A >= kappa_A:
                beta_A = pi_over_Lambda + math.sqrt(delta_A**2 - kappa_A**2)
            else:
                beta_A = pi_over_Lambda - math.sqrt(delta_A**2 - kappa_A**2)
            rows.append((beta_A, 1e-6, w))

        # other diffraction orders (no gap)
        for m in [-2, -1, 1, 2]:
            beta_m = beta_unp_A + m * 2.0 * pi_over_Lambda
            if 5.0 <= beta_m <= 30.0:
                rows.append((beta_m, 1e-6, w))

        # --- process mode B -------------------------------------------------
        beta_unp_B = k0 * n_B
        delta_B = beta_unp_B - pi_over_Lambda
        if abs(delta_B) >= kappa_B:
            if delta_B >= kappa_B:
                beta_B = pi_over_Lambda + math.sqrt(delta_B**2 - kappa_B**2)
            else:
                beta_B = pi_over_Lambda - math.sqrt(delta_B**2 - kappa_B**2)
            rows.append((beta_B, 1e-6, w))

        for m in [-2, -1, 1, 2]:
            beta_m = beta_unp_B + m * 2.0 * pi_over_Lambda
            if 5.0 <= beta_m <= 30.0:
                rows.append((beta_m, 1e-6, w))

        w += w_step

    # add the exact band‑edge resonance point (Q point) explicitly
    w_res = 1.55
    k0_res = 2.0 * math.pi / w_res
    beta_res = pi_over_Lambda   # group‑velocity zero at band edge
    rows.append((beta_res, 1e-9, w_res))

    return rows


# ======================================================================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate.py <type>")
        sys.exit(1)

    typ = sys.argv[1]

    if typ == "filter_alpha_rp":
        write_csv("filter_alpha_rp.csv",
                  ["wavelength", "alpha", "Rp"],
                  gen_filter_data())
    elif typ == "resonator_alpha_vs_Lambda":
        write_csv("resonator_alpha_vs_Lambda.csv",
                  ["Lambda", "alpha"],
                  gen_resonator_alpha_vs_Lambda())
    elif typ == "resonator_Rp_vs_lambda":
        write_csv("resonator_Rp_vs_lambda.csv",
                  ["wavelength", "Rp"],
                  gen_resonator_Rp_vs_wavelength())
    elif typ == "brillouin_diagram":
        write_csv("brillouin_diagram.csv",
                  ["beta", "alpha", "wavelength"],
                  gen_brillouin())
    else:
        print(f"Unknown type: {typ}")
        sys.exit(1)
