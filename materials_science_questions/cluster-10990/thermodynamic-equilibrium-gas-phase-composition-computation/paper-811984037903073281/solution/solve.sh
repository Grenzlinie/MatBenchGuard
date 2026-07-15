#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: gas_composition.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import csv
import math

# Thermochemical data: ΔH_1000 (kcal/mol), S_1000 (cal/mol·K)
# Species names in order we will use
species_names = [
    "NbOCl3", "NbCl4", "NbCl5", "TeOCl2", "TeCl2", "TeCl4",
    "TeO2", "TeO", "Te2", "Te", "Cl2", "Cl", "O2"
]

idx = {name: i for i, name in enumerate(species_names)}

data = {
    "NbOCl3": (-166.46, 112.2),
    "NbCl4":  (-114.92, 121.8),
    "NbCl5":  (-144.62, 145.2),
    "TeOCl2": (-31.00, 101.0),
    "TeCl2":  (-5.10, 86.0),
    "TeCl4":  (-32.45, 119.0),
    "TeO2":   (-6.20, 82.6),
    "TeO":    (22.82, 69.5),
    "Te2":    (46.44, 74.7),
    "Te":     (50.39, 49.7),
    "Cl2":    (6.06, 63.7),
    "Cl":     (32.73, 45.9),
    "O2":     (5.39, 58.2),
    # Solid NbO2 (for reactions that involve the solid)
    "NbO2_f": (-177.20, 34.2),
}

def get_dH_S(name):
    return data[name]

# Reaction stoichiometry vectors (coefficients for each gas species, reactant negative, product positive)
# Order: NbOCl3, NbCl4, NbCl5, TeOCl2, TeCl2, TeCl4, TeO2, TeO, Te2, Te, Cl2, Cl, O2
# Solid species coefficients are not included in the matrix (activity=1), but their thermodynamic contributions are added separately.
reactions = []
# Reaction (1): 2 NbO2(f) + 3 Cl2 -> 2 NbOCl3 + 1 O2
react1 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 1]
# Reaction (2): 1 NbO2(f) + 2 Cl2 -> 1 NbCl4 + 1 O2
react2 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 1]
# (3) NbCl4 + 0.5 Cl2 -> NbCl5
react3 = [0, -1, 1, 0, 0, 0, 0, 0, 0, 0, -0.5, 0, 0]
# (4) TeCl4 -> TeCl2 + Cl2
react4 = [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 1, 0, 0]
# (5) TeCl2 + 0.5 O2 -> TeOCl2
react5 = [0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, -0.5]
# (6) TeCl2 + O2 -> TeO2 + Cl2
react6 = [0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, 0, -1]
# (7) TeO2 -> 0.5 Te2 + O2
react7 = [0, 0, 0, 0, 0, 0, -1, 0, 0.5, 0, 0, 0, 1]
# (8) TeO -> 0.5 Te2 + 0.5 O2
react8 = [0, 0, 0, 0, 0, 0, 0, -1, 0.5, 0, 0, 0, 0.5]
# (9) Te2 -> 2 Te
react9 = [0, 0, 0, 0, 0, 0, 0, 0, -1, 2, 0, 0, 0]
# (10) Cl2 -> 2 Cl
react10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 2, 0]

reactions = [react1, react2, react3, react4, react5, react6, react7, react8, react9, react10]

# Solid contribution for reactions 1 and 2
# Reaction 1: 2 NbO2_f (reactant) -> ΔH = 2*Hf, ΔS = 2*Sf
# Reaction 2: 1 NbO2_f -> ΔH = 1*Hf, ΔS = 1*Sf
solid_coeff_vs_react = [2, 1, 0, 0, 0, 0, 0, 0, 0, 0]

def compute_K(T):
    K = np.zeros(10)
    for i, coeffs in enumerate(reactions):
        dH_gas = sum(coeff * data[species_names[j]][0] for j, coeff in enumerate(coeffs))
        dS_gas = sum(coeff * data[species_names[j]][1] for j, coeff in enumerate(coeffs))
        # Add solid
        if solid_coeff_vs_react[i] != 0:
            dH_s = solid_coeff_vs_react[i] * data["NbO2_f"][0]
            dS_s = solid_coeff_vs_react[i] * data["NbO2_f"][1]
            # Note: solid is reactant, so subtract from product side? In our coeffs, solids are not in the vector.
            # The gas-phase ΔH_R_gas = sum(product gas - reactant gas). For reaction (1), 2 NbOCl3 + O2 - 3 Cl2, which is the net gas change.
            # The solid term is: -2 * H(NbO2), because 2 NbO2 are reactants. So total ΔH_R = dH_gas - 2*H(NbO2).
            dH_R = dH_gas - dH_s
            dS_R = dS_gas - dS_s
        else:
            dH_R = dH_gas
            dS_R = dS_gas
        # Compute lg K = ΔS/(4.574) - ΔH/(4.574 T)
        lgK = dS_R / 4.574 - dH_R / (4.574 * T)
        K[i] = 10 ** lgK
    return K

def constraint_func(p, T, pO2_target):
    K = compute_K(T)
    # p is array of 13 partial pressures
    eqs = np.zeros(13)
    # Mass action equations (K - Q = 0)
    # (1)
    eqs[0] = p[idx["NbOCl3"]]**2 * p[idx["O2"]] - K[0] * p[idx["Cl2"]]**3
    # (2)
    eqs[1] = p[idx["NbCl4"]] * p[idx["O2"]] - K[1] * p[idx["Cl2"]]**2
    # (3)
    eqs[2] = p[idx["NbCl5"]] - K[2] * p[idx["NbCl4"]] * p[idx["Cl2"]]**0.5
    # (4)
    eqs[3] = p[idx["TeCl2"]] * p[idx["Cl2"]] - K[3] * p[idx["TeCl4"]]
    # (5)
    eqs[4] = p[idx["TeOCl2"]] - K[4] * p[idx["TeCl2"]] * p[idx["O2"]]**0.5
    # (6)
    eqs[5] = p[idx["TeO2"]] * p[idx["Cl2"]] - K[5] * p[idx["TeCl2"]] * p[idx["O2"]]
    # (7)
    eqs[6] = p[idx["Te2"]]**0.5 * p[idx["O2"]] - K[6] * p[idx["TeO2"]]
    # (8)
    eqs[7] = p[idx["Te2"]]**0.5 * p[idx["O2"]]**0.5 - K[7] * p[idx["TeO"]]
    # (9)
    eqs[8] = p[idx["Te"]]**2 - K[8] * p[idx["Te2"]]
    # (10)
    eqs[9] = p[idx["Cl"]]**2 - K[9] * p[idx["Cl2"]]
    # Total pressure constraint
    eqs[10] = sum(p) - 1.0
    # Cl/Te balance ratio
    pCl_star = (3*p[idx["NbOCl3"]] + 4*p[idx["NbCl4"]] + 5*p[idx["NbCl5"]] +
                2*p[idx["TeOCl2"]] + 2*p[idx["TeCl2"]] + 4*p[idx["TeCl4"]] +
                2*p[idx["Cl2"]] + 1*p[idx["Cl"]])
    pTe_star = (1*p[idx["TeOCl2"]] + 1*p[idx["TeCl2"]] + 1*p[idx["TeCl4"]] +
                1*p[idx["TeO2"]] + 1*p[idx["TeO"]] + 2*p[idx["Te2"]] + 1*p[idx["Te"]])
    eqs[11] = pCl_star - 4.0 * pTe_star
    # pO2 target
    eqs[12] = p[idx["O2"]] - pO2_target
    return eqs

def solve_composition(T, pO2_target):
    # Initial guess: rough estimate with dominant species
    guess = np.zeros(13)
    # dominant: NbOCl3 and Te2 roughly 0.4 each, others small
    guess[idx["NbOCl3"]] = 0.35
    guess[idx["Te2"]] = 0.4
    guess[idx["Te"]] = 0.1
    guess[idx["O2"]] = pO2_target
    guess[idx["Cl2"]] = 0.01
    guess[idx["Cl"]] = 0.01
    guess[idx["NbCl4"]] = 0.005
    guess[idx["NbCl5"]] = 0.005
    guess[idx["TeCl2"]] = 0.005
    guess[idx["TeCl4"]] = 0.005
    guess[idx["TeOCl2"]] = 0.005
    guess[idx["TeO2"]] = 0.005
    guess[idx["TeO"]] = 0.005
    # ensure sum about 1
    s = sum(guess)
    guess /= s
    sol = fsolve(lambda p: constraint_func(p, T, pO2_target), guess, maxfev=2000, xtol=1e-12)
    # clamp tiny negative values to 0
    sol[sol < 0] = 1e-30
    return sol

# Temperature range
Ts = list(range(1000, 1550, 50))  # 1000,1050,...,1500
boundaries = {
    "upper": ("11.5965", "37452"),  # log10(pO2) = 11.5965 - 37452/T
    "lower": ("10.1624", "38951")   # log10(pO2) = 10.1624 - 38951/T
}

rows = []
for T in Ts:
    for bname, (A, B) in boundaries.items():
        A_val = float(A)
        B_val = float(B)
        log10_pO2 = A_val - B_val / T
        pO2 = 10 ** log10_pO2
        sol = solve_composition(T, pO2)
        for i, name in enumerate(species_names):
            rows.append([T, name, float(sol[i]), bname])

# Write CSV
csv_path = "/app/outputs/gas_composition.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T", "species", "p", "boundary"])
    writer.writerows(rows)
print("gas_composition.csv written")
PYEOF
