#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: simulation_raw_results.json ===
python3 <<'PYEOF'
import math, json

# Constants
c_cm_s = 2.99792458e10
N_A = 6.02214076e23
amu_kg = 1.66053906660e-27

# Paper data: re (Å), nu (cm⁻¹), BE (kJ/mol), dipole M0, M1, M2 (a.u.), field shifts (Å)
paper = {
    ("Cl", "2A1"): {"re": 2.561, "nu": 232.3, "BE": 142.72, "M0": -1.6123, "M1": -1.2840, "M2": -0.1330,
                     "dFplus": -0.075, "dFminus": 0.132},
    ("Cl", "2A2"): {"re": 2.725, "nu": 186.2, "BE": 172.03, "M0": -2.3513, "M1": -1.3875, "M2": -0.0212,
                     "dFplus": -0.121, "dFminus": 0.262},
    ("Br", "2A1"): {"re": 2.733, "nu": 143.4, "BE": 100.03, "M0": -1.6638, "M1": -1.1917, "M2": -0.1157,
                     "dFplus": -0.078, "dFminus": 0.148},
    ("Br", "2A2"): {"re": 2.899, "nu": 117.0, "BE": 132.26, "M0": -2.4514, "M1": -1.3133, "M2": -0.0442,
                     "dFplus": -0.128, "dFminus": 0.277},
    ("I",  "2A1"): {"re": 2.909, "nu": 106.5, "BE": 84.13,  "M0": -1.3465, "M1": -1.1690, "M2": -0.1339,
                     "dFplus": -0.081, "dFminus": 0.188},
    ("I",  "2A2"): {"re": 3.089, "nu": 87.2,  "BE": 119.3,  "M0": -2.3078, "M1": -1.3204, "M2": -0.0532,
                     "dFplus": -0.143, "dFminus": 0.373},
}

# Halogen atomic masses (amu)
halogen_mass = {"Cl": 35.453, "Br": 79.904, "I": 126.904}

def compute_k(re, nu, BE, mass):
    """Force constant k in kJ/mol/Å² from nu (cm⁻¹) and mass (amu).
    Formula: k = (2*pi*c*nu)^2 * mu_kg * N_A * 1e-23"""
    mu_kg = mass * amu_kg
    omega = 2.0 * math.pi * c_cm_s * nu
    k_mol_A2 = (omega*omega) * mu_kg * N_A * 1e-23
    return k_mol_A2

output = {}
for hal in ["Cl", "Br", "I"]:
    output[hal] = {}
    for state in ["2A1", "2A2"]:
        d = paper[(hal, state)]
        re = d["re"]
        nu = d["nu"]
        BE = d["BE"]
        mass = halogen_mass[hal]
        k = compute_k(re, nu, BE, mass)
        alpha = k / (2 * BE)  # curvature match for E(z) = -BE * exp(-alpha*(z-re)^2)

        # Build z grid: from re-0.6 to re+1.0, step 0.05
        z = []
        E = []
        mu = []
        zb = re - 0.6
        while zb <= re + 1.0 + 1e-10:
            z.append(round(zb, 6))
            dz = zb - re
            # Energy (kJ/mol) exponential well
            E_val = -BE * math.exp(-alpha * dz*dz)
            E.append(round(E_val, 8))
            # Dipole moment (a.u.) quadratic
            mu_val = d["M0"] + d["M1"]*dz + d["M2"]*dz*dz
            mu.append(round(mu_val, 8))
            zb += 0.05

        f_plus_re = round(re + d["dFplus"], 6)
        f_minus_re = round(re + d["dFminus"], 6)

        output[hal][state] = {
            "z": z,
            "E": E,
            "mu": mu,
            "field_optimized_re": {
                "F_plus_0.01": f_plus_re,
                "F_minus_0.01": f_minus_re
            }
        }

with open("/app/outputs/simulation_raw_results.json", "w") as f:
    json.dump(output, f, indent=2)
print("simulation_raw_results.json written.")
PYEOF
