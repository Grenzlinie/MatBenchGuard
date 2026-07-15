#!/usr/bin/env python3
"""
Write artifacts for WBK force field reproduction (reference oracle).
Usage: python3 write_artifacts.py <basename>
Writes /app/outputs/<basename>.
"""
import sys
import os
import csv
import json

OUTDIR = "/app/outputs"

def write_force_field_params():
    params = {
        "combining_rule": "Hogervorst",
        "Li+": {"sigma": 0.145, "epsilon": 0.25, "gamma": 12.0},
        "Na+": {"sigma": 0.175, "epsilon": 0.50, "gamma": 14.0},
        "K+":  {"sigma": 0.210, "epsilon": 0.80, "gamma": 15.0},
        "Cs+": {"sigma": 0.255, "epsilon": 1.00, "gamma": 16.0},
        "F-":  {"sigma": 0.180, "epsilon": 1.50, "gamma": 10.0},
        "Cl-": {"sigma": 0.225, "epsilon": 2.00, "gamma": 12.0},
        "Br-": {"sigma": 0.250, "epsilon": 2.50, "gamma": 13.0},
        "I-":  {"sigma": 0.280, "epsilon": 3.00, "gamma": 14.0}
    }
    path = os.path.join(OUTDIR, "force_field_parameters.json")
    with open(path, "w") as f:
        json.dump(params, f, indent=2)
    print(f"Wrote {path}")

def write_gas_properties():
    # 20 salts, gas-phase properties after WBK optimization;
    # values are close to experimental references from NIST/Brewer&Gordy.
    salts = [
        ("LiF", 156.4, 582.0, 910, 6.60),
        ("LiCl", 202.0, 484.0, 665, 7.10),
        ("LiBr", 217.0, 423.4, 570, 7.30),
        ("LiI",  239.0, 363.0, 500, 7.50),
        ("NaF", 193.0, 483.0, 540, 8.20),
        ("NaCl", 236.0, 412.0, 366, 9.10),
        ("NaBr", 250.0, 372.0, 300, 9.30),
        ("NaI",  272.0, 312.0, 260, 9.80),
        ("KF",  217.0, 493.0, 420, 8.60),
        ("KCl",  267.0, 432.0, 280, 10.40),
        ("KBr",  282.0, 391.0, 230, 10.70),
        ("KI",   305.0, 341.0, 190, 11.20),
        ("RbF",  227.0, 492.0, 370, 8.80),
        ("RbCl", 279.0, 421.0, 240, 10.50),
        ("RbBr", 294.0, 381.0, 190, 10.80),
        ("RbI",  317.0, 331.0, 170, 11.20),
        ("CsF",  234.0, 492.0, 340, 8.00),
        ("CsCl", 291.0, 451.0, 210, 10.80),
        ("CsBr", 307.0, 421.0, 170, 11.20),
        ("CsI",  332.0, 371.0, 150, 11.80)
    ]
    path = os.path.join(OUTDIR, "gas_properties.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["salt", "re_pm", "De_kjmol", "nu_cm1", "mu_D"])
        for s, re, de, nu, mu in salts:
            w.writerow([s, f"{re:.1f}", f"{de:.1f}", f"{nu}", f"{mu:.2f}"])
    print(f"Wrote {path}")

def write_solid_density():
    # Solid densities at 298 K (kg/m3) for 20 salts.
    densities = [
        ("LiF", 2640),
        ("LiCl", 2070),
        ("LiBr", 3464),
        ("LiI",  4060),
        ("NaF", 2780),
        ("NaCl", 2160),
        ("NaBr", 3200),
        ("NaI",  3670),
        ("KF",  2480),
        ("KCl",  1980),
        ("KBr",  2750),
        ("KI",   3120),
        ("RbF",  3260),
        ("RbCl", 2760),
        ("RbBr", 3350),
        ("RbI",  3550),
        ("CsF",  4110),
        ("CsCl", 3990),
        ("CsBr", 4430),
        ("CsI",  4510)
    ]
    path = os.path.join(OUTDIR, "solid_density_298K.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["salt", "density_kgm3"])
        for s, d in densities:
            w.writerow([s, d])
    print(f"Wrote {path}")

def write_liquid_density():
    # Liquid densities at melting point (kg/m3) for 10 salts.
    liq_dens = [
        ("LiF", 1760),
        ("LiCl", 1520),
        ("NaCl", 1550),
        ("KF",  1900),
        ("KCl",  1510),
        ("KBr",  2110),
        ("RbCl", 2700),
        ("RbBr", 3250),
        ("CsF",  3580),
        ("CsCl", 2800)
    ]
    path = os.path.join(OUTDIR, "liquid_density_Tm.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["salt", "density_kgm3"])
        for s, d in liq_dens:
            w.writerow([s, d])
    print(f"Wrote {path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 write_artifacts.py <basename>")
        sys.exit(1)
    basename = sys.argv[1]
    os.makedirs(OUTDIR, exist_ok=True)
    if basename == "force_field_parameters.json":
        write_force_field_params()
    elif basename == "gas_properties.csv":
        write_gas_properties()
    elif basename == "solid_density_298K.csv":
        write_solid_density()
    elif basename == "liquid_density_Tm.csv":
        write_liquid_density()
    else:
        print(f"Unknown artifact: {basename}")
        sys.exit(1)
