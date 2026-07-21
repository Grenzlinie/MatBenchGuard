#!/usr/bin/env python3
"""Reference Oracle: Computes HYBAS actuator c values and max displacements."""
import sys
import json
import numpy as np

# ---- Constants (all SI) ----
L0 = 5.5e-3                 # initial length (m)
N_INT = 1000                # Riemann sum subintervals
TOL_ERROR = 1e-5            # stop when percent error < 0.001% (1e-5 fraction)

# Original negative strain component (ESC) geometry
T_NEG = 470e-6              # thickness (m)
B_NEG = 3e-3                # width (m)
E_NEG_ORIG = 20e9           # Young's modulus (Pa)
D31_NEG_ORIG = -970e-12     # d31 (C/N) = -970 pC/N

# Original positive strain component (EAP) geometry (active layer)
T_POS = 16e-6               # thickness (m)
B_POS_ACT = 3e-3            # effective width (m)
E_POS_ORIG = 1e9            # Young's modulus (Pa)
D31_POS_ORIG = 20e-12       # d31 (C/N) = 20 pC/N

# Inactive layer dimensions (all lengths in m, widths in m)
# inactive EAP layer
E_INACT_EAP = 1e9
T_INACT_EAP = 15e-6
B_INACT_EAP = 4.5e-3
# epoxy layer
E_EPOXY = 5e9
T_EPOXY = 1e-6
B_EPOXY = 4.5e-3
# gold electrodes (two, each 0.1 um)
E_GOLD = 74e9
T_GOLD = 0.1e-6
B_GOLD = 3e-3
# unelectroded margins (total margin width = 1.5 mm)
E_MARGIN = 1e9
T_MARGIN = 16e-6
B_MARGIN_TOTAL = 1.5e-3

# Total inactive stiffness (N) – constant for all configurations
INACT_STIFF = (
    E_INACT_EAP * T_INACT_EAP * B_INACT_EAP
    + E_EPOXY * T_EPOXY * B_EPOXY
    + 2 * E_GOLD * T_GOLD * B_GOLD
    + E_MARGIN * T_MARGIN * B_MARGIN_TOTAL
)

# Trade study materials (negative strain)
NEG_MATERIALS = [
    {"name": "Hard PZT (TRS100HD)", "d31": -150e-12, "E": 79e9},
    {"name": "Soft PZT (TRSHK1HD)", "d31": -360e-12, "E": 67e9},
    {"name": "PZN-4.5%PT single crystal", "d31": -970e-12, "E": 12e9},
]

# Trade study materials (positive strain)
POS_MATERIALS = [
    {"name": "Uni-axial PVDF", "d31": 20e-12, "E": 2e9},
    {"name": "Bi-axial PVDF", "d31": 8e-12, "E": 2e9},
]

def compute_k(E_active):
    """Clamping ratio k = inactive stiffness / active stiffness."""
    active_stiff = E_active * T_POS * B_POS_ACT
    return INACT_STIFF / active_stiff

def integrate_lhs(c, Ld, N=N_INT):
    """Left Riemann sum of sqrt( [c (4x^3 - Ld^2 x)]^2 + 1 ) dx over [-Ld/2, Ld/2]."""
    dx = Ld / N
    x = np.linspace(-Ld/2, Ld/2 - dx, N)   # left endpoints
    f = np.sqrt((c * (4*x**3 - Ld**2*x))**2 + 1)
    return np.sum(f) * dx

def solve_c(s_neg, s_pos):
    """Find c satisfying arc-length equality; returns (c_m3, percent_error)."""
    Ld = L0 * (1 + s_neg)
    RHS = L0 * (1 + s_pos)
    if RHS == 0:
        return 0.0, 0.0
    # Bracket root: f(c) = LHS(c) - RHS, monotone increasing in c
    c_lo = 0.0
    f_lo = integrate_lhs(c_lo, Ld) - RHS
    c_hi = 1.0
    while integrate_lhs(c_hi, Ld) - RHS < 0:
        c_hi *= 2.0
        if c_hi > 1e12:
            raise RuntimeError("Failed to bracket root")
    # Bisection
    for _ in range(200):
        c_mid = (c_lo + c_hi) / 2.0
        f_mid = integrate_lhs(c_mid, Ld) - RHS
        error = abs(f_mid) / RHS if RHS != 0 else 0.0
        if error < TOL_ERROR:
            return c_mid, error * 100  # return percent
        if f_mid < 0:
            c_lo = c_mid
        else:
            c_hi = c_mid
    # fallback
    c = (c_lo + c_hi) / 2.0
    error = abs(integrate_lhs(c, Ld) - RHS) / RHS * 100
    return c, error

def generate_c_values():
    voltages = [200.0, 400.0, 800.0, 1600.0]
    modes = ["EAP", "ESC", "HYBAS"]
    results = []
    k_orig = compute_k(E_POS_ORIG)
    for V in voltages:
        # strains for original materials
        s_neg = D31_NEG_ORIG * V / T_NEG     # negative
        s_free_pos = D31_POS_ORIG * V / T_POS
        s_pos = s_free_pos / (1 + k_orig)    # positive effective
        for mode in modes:
            if mode == "EAP":
                sn = 0.0
                sp = s_pos
            elif mode == "ESC":
                sn = s_neg
                sp = 0.0
            else:  # HYBAS
                sn = s_neg
                sp = s_pos
            c_m3, pct_err = solve_c(sn, sp)
            c_106 = c_m3 / 1e6   # convert to 10^6 m^{-3}
            results.append({
                "voltage": V,
                "active_elements": mode,
                "c": c_106,
                "percent_error": pct_err
            })
    return results

def generate_max_displacements():
    voltages = [100.0, 650.0]
    results = []
    for neg in NEG_MATERIALS:
        for pos in POS_MATERIALS:
            k_pos = compute_k(pos["E"])
            for V in voltages:
                s_neg = neg["d31"] * V / T_NEG
                s_free_pos = pos["d31"] * V / T_POS
                s_pos_eff = s_free_pos / (1 + k_pos)
                c, _ = solve_c(s_neg, s_pos_eff)
                Ld = L0 * (1 + s_neg)
                w_max_m = c * Ld**4 / 16.0
                w_max_um = w_max_m * 1e6
                results.append({
                    "negative_strain_material": neg["name"],
                    "positive_strain_material": pos["name"],
                    "voltage": V,
                    "max_displacement": w_max_um
                })
    return results

def main():
    out = None
    for arg in sys.argv[1:]:
        if arg.startswith("--output="):
            out = arg.split("=", 1)[1]
        elif arg == "--output":
            # placeholder
            pass
    if out == "c_values.json":
        data = generate_c_values()
    elif out == "max_displacements.json":
        data = generate_max_displacements()
    else:
        print("Usage: compute.py --output <c_values.json|max_displacements.json>", file=sys.stderr)
        sys.exit(1)
    path = f"/app/outputs/{out}"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
