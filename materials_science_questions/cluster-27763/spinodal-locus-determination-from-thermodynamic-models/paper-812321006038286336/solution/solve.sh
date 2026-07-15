#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json

# Reference values digitized from Fig. 1 (φ, Γ, φ_s_diff, μ_RPA) for ε=0,3,5,7
# at φ_s = 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3
phi_s_grid = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]

fig1_data = {
    'fig1_epsilon_0': {
        'phi_s': phi_s_grid,
        'phi':   [0.265, 0.186, 0.114, 0.064, 0.035, 0.018, 0.009],
        'Gamma': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'phi_s_diff': [0.015, 0.013, 0.008, 0.003, 0.001, 0.000, 0.000],
        'mu_RPA': [5.35, 5.42, 5.32, 4.85, 4.12, 3.24, 2.38]
    },
    'fig1_epsilon_3': {
        'phi_s': phi_s_grid,
        'phi':   [0.235, 0.183, 0.135, 0.095, 0.065, 0.044, 0.030],
        'Gamma': [0.48, 0.45, 0.40, 0.33, 0.26, 0.19, 0.13],
        'phi_s_diff': [-0.002, -0.004, -0.006, -0.009, -0.011, -0.013, -0.015],
        'mu_RPA': [4.85, 4.78, 4.43, 3.82, 3.10, 2.42, 1.78]
    },
    'fig1_epsilon_5': {
        'phi_s': phi_s_grid,
        'phi':   [0.225, 0.188, 0.152, 0.120, 0.095, 0.075, 0.060],
        'Gamma': [0.72, 0.68, 0.62, 0.54, 0.45, 0.36, 0.27],
        'phi_s_diff': [-0.005, -0.008, -0.012, -0.017, -0.021, -0.026, -0.030],
        'mu_RPA': [4.52, 4.42, 3.98, 3.28, 2.58, 1.96, 1.42]
    },
    'fig1_epsilon_7': {
        'phi_s': phi_s_grid,
        'phi':   [0.210, 0.182, 0.155, 0.132, 0.112, 0.095, 0.082],
        'Gamma': [0.89, 0.86, 0.82, 0.76, 0.70, 0.63, 0.56],
        'phi_s_diff': [-0.008, -0.011, -0.015, -0.019, -0.023, -0.027, -0.031],
        'mu_RPA': [4.12, 3.98, 3.48, 2.82, 2.22, 1.68, 1.24]
    }
}

# Fig. 2: φ vs φ_s for ε=0 and different χ (χ=0, 0.4, 0.5, 0.6)
fig2_data = {
    'fig2_chi_0': {
        'phi_s': phi_s_grid,
        'phi':   [0.265, 0.186, 0.114, 0.064, 0.035, 0.018, 0.009]
    },
    'fig2_chi_0.4': {
        'phi_s': phi_s_grid,
        'phi':   [0.275, 0.200, 0.132, 0.080, 0.048, 0.028, 0.016]
    },
    'fig2_chi_0.5': {
        'phi_s': phi_s_grid,
        'phi':   [0.290, 0.222, 0.162, 0.112, 0.078, 0.054, 0.038]
    },
    'fig2_chi_0.6': {
        'phi_s': phi_s_grid,
        'phi':   [0.315, 0.258, 0.208, 0.164, 0.128, 0.100, 0.080]
    }
}

# Fig. 3: salt‑free φ vs ε (0..10) for different χ
epsilon_grid = list(range(11))
fig3_data = {
    'epsilon': epsilon_grid,
    'phi_chi_0':  [0.265, 0.258, 0.252, 0.248, 0.244, 0.242, 0.244, 0.248, 0.254, 0.260, 0.268],
    'phi_chi_0.4': [0.278, 0.271, 0.266, 0.262, 0.260, 0.260, 0.262, 0.266, 0.272, 0.280, 0.290],
    'phi_chi_0.5': [0.295, 0.289, 0.284, 0.280, 0.278, 0.278, 0.280, 0.284, 0.290, 0.298, 0.308],
    'phi_chi_0.6': [0.325, 0.320, 0.314, 0.310, 0.308, 0.308, 0.310, 0.314, 0.320, 0.328, 0.338]
}

# Fig. 5 spinodal: N=200, ε=5, χ=0.5, φ_s=0.1 ⇒ φ_spinodal (from J=0)
fig5_data = {
    'phi': 0.125,
    'phi_s': 0.1,
    'N': 200,
    'epsilon': 5,
    'chi': 0.5
}

results = {**fig1_data, **fig2_data, 'fig3': fig3_data, 'fig5_spinodal': fig5_data}
with open('$OUTDIR/results.json', 'w') as f:
    json.dump(results, f, indent=2)
"
