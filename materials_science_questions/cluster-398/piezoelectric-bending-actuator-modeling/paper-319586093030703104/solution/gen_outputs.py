#!/usr/bin/env python3
"""Write the oracle outputs for the piezo-quasi-mosaic effect.
Usage: python gen_outputs.py <output_name>
Output names: relative_gain.json, w_pl_distribution.csv
"""
import sys, math, json, csv

# Fixed parameters from the paper example
U0_V = 3000.0
L_mm = 1.0
d24_CGSE = 9e-8
omega_g_arcsec = 0.7

# Standard conversions
V_PER_STATVOLT = 299.792458   # 1 statvolt ≈ 299.792458 V
RAD_TO_ARCSEC = 206265.0       # 1 radian = 206265 arcseconds

# Derived quantities
U0_statvolt = U0_V / V_PER_STATVOLT
L_cm = L_mm / 10.0             # 1 mm = 0.1 cm
Phi_rad = 2.0 * U0_statvolt * d24_CGSE / L_cm
Phi_arcsec = Phi_rad * RAD_TO_ARCSEC
gain = Phi_arcsec / omega_g_arcsec

OUTPUTS = {
    "relative_gain.json": {
        "piezo_quasi_mosaic_width_arcsec": Phi_arcsec,
        "natural_mosaic_width_arcsec": omega_g_arcsec,
        "relative_gain": gain
    },
    "w_pl_distribution.csv": None  # generated differently
}

def write_relative_gain():
    data = {
        "piezo_quasi_mosaic_width_arcsec": Phi_arcsec,
        "natural_mosaic_width_arcsec": omega_g_arcsec,
        "relative_gain": gain
    }
    with open("/app/outputs/relative_gain.json", "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

def write_w_pl_distribution():
    epsilon_min = 1e-9  # avoid division by zero
    epsilon_max = Phi_rad * (1.0 - 1e-9)
    n_points = 200
    with open("/app/outputs/w_pl_distribution.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["epsilon_arcsec", "w_pl"])
        for i in range(n_points):
            frac = i / (n_points - 1)
            eps_rad = epsilon_min + (epsilon_max - epsilon_min) * frac
            w_pl = (1.0 / math.pi) / math.sqrt(eps_rad * (Phi_rad - eps_rad))
            eps_arcsec = eps_rad * RAD_TO_ARCSEC
            writer.writerow([eps_arcsec, w_pl])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: gen_outputs.py <output_name>")
    target = sys.argv[1]
    if target == "relative_gain.json":
        write_relative_gain()
    elif target == "w_pl_distribution.csv":
        write_w_pl_distribution()
    else:
        sys.exit(f"Unknown output: {target}")
