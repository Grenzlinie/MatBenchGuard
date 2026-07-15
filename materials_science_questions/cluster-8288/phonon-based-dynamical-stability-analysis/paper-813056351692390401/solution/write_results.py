#!/usr/bin/env python3
"""Reference oracle: write results.json with paper‑reported asymptotic energies,
optical fitting coefficients, and a synthetic 2H‑band‑gap table."""

import json
import math

# ----------------------- asymptotic energies -----------------------
energies = {
    "1T'": {
        "surface_energy_asymptote_J_per_m2": 0.005,
        "cleaving_energy_asymptote_J_per_m2": 0.288,
        "binding_energy_asymptote_eV": 22.28,
        "vdw_energy_asymptote_J_per_m2": 0.47
    },
    "2H": {
        "surface_energy_asymptote_J_per_m2": 0.183,
        "cleaving_energy_asymptote_J_per_m2": 0.304,
        "binding_energy_asymptote_eV": 22.04,
        "vdw_energy_asymptote_J_per_m2": 0.36
    },
    "3R": {
        "surface_energy_asymptote_J_per_m2": 0.233,
        "cleaving_energy_asymptote_J_per_m2": 0.351,
        "binding_energy_asymptote_eV": 22.86,
        "vdw_energy_asymptote_J_per_m2": 0.37
    }
}

# ----------------------- 2H band gap vs layer -----------------------
# Exponential model: gap(N) = G_bulk + A * exp(-k*(N-1))
# With G_bulk = 1.441, monolayer G₁ = 2.219, bilayer G₂ = 1.707 (from text: drop of 0.512)
G_bulk = 1.441
G1 = 2.219
G2 = 1.707
A = G1 - G_bulk
k = -math.log((G2 - G_bulk) / A)   # k ≈ 1.074
bandgap_2H = []
max_layers = 20
for n in range(1, max_layers + 1):
    gap = G_bulk + A * math.exp(-k * (n - 1))
    bandgap_2H.append({"layer": n, "bandgap_eV": round(gap, 6)})
# Ensure the last entry is close to bulk
bandgap_2H[-1]["bandgap_eV"] = round(G_bulk + A * math.exp(-k * (max_layers - 1)), 6)

# ----------------------- optical fitting coefficients -----------------------
# Coefficients correspond to the model y = A - B * exp(-N / C)
# Extracted from Equations (1)–(9) in the paper.
optical = {
    "1T'": {
        "eps1_0_fit_coeffs":  [15.967, 17.158, 4.25],
        "n_0_fit_coeffs":     [3.991,  3.338,  3.278],
        "eps1_inf_fit_coeffs":[0.552, -0.363, 25.419],  # original eqn had +0.363*exp(...), so B is negative
        "n_inf_fit_coeffs":   [0.729, -0.228, 29.029],
        "absorption_fit_coeffs": [2.360, 1.558, 3.60],
        "reflectivity_fit_coeffs": [0.440, -0.320, 2.952]
    },
    "2H": {
        "eps1_0_fit_coeffs":  [5.580, 5.512, 2.44],
        "n_0_fit_coeffs":     [2.330, 1.392, 2.401],
        "eps1_inf_fit_coeffs":[0.552, -0.362, 27.178],
        "n_inf_fit_coeffs":   [0.735, -0.221, 30.181],
        "absorption_fit_coeffs": [2.725, 1.656, 3.973],
        "reflectivity_fit_coeffs": [0.492, -0.312, 3.30]
    },
    "3R": {
        "eps1_0_fit_coeffs":  [12.565, 15.117, 2.758],
        "n_0_fit_coeffs":     [3.588,  3.176,  2.416],
        "eps1_inf_fit_coeffs":[0.640, -0.272, 21.539],
        "n_inf_fit_coeffs":   [0.791, -0.164, 24.048],
        "absorption_fit_coeffs": [1.797, 1.262, 3.220],
        "reflectivity_fit_coeffs": [0.392, -0.306, 2.866]
    }
}

# Assemble final JSON
results = {
    "energies": energies,
    "bandgap_2H": bandgap_2H,
    "optical": optical
}

outpath = "/app/outputs/results.json"
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Wrote {outpath}")
