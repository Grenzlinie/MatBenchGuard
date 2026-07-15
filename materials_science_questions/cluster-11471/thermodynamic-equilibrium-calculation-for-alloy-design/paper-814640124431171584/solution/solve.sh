#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/gen_outputs.py

# === solve block: predicted_properties.csv ===
python3 << 'PYEOF'
import numpy as np
import csv
import os

OUTDIR = "/app/outputs"
TEMPERATURES = [600, 625, 650]

# Initial phase fractions [austenite, ferrite, martensite]
PHASE_FRACS = {
    600: [0.318, 0.682, 0.0],
    625: [0.379, 0.621, 0.0],
    650: [0.443, 0.528, 0.029]
}

# Hollomon parameters (K [MPa], n)
HOLLOMON = {
    'ferrite':    (581.0, 0.30),
    'austenite':  (2936.0, 0.67),
    'martensite': (2652.0, 0.08)
}

# Olson-Cohen [alpha, beta, m]
OC_PARAMS = {
    600: (5.75, 2.5, 3),
    625: (18.6, 1.86, 2),
    650: (49.5, 1.8, 2)
}

def secant_solve_conssidere(eps_grid, sigma_c):
    """Find the true strain where dsigma/de = sigma using linear interpolation."""
    dsigma = np.gradient(sigma_c, eps_grid)
    diff = dsigma - sigma_c
    # find sign change from positive to negative
    for i in range(1, len(diff)):
        if diff[i-1] >= 0 and diff[i] <= 0:
            # linear interpolation for zero crossing
            eps_root = eps_grid[i-1] - diff[i-1] * (eps_grid[i] - eps_grid[i-1]) / (diff[i] - diff[i-1])
            return eps_root
    # if no crossing found, return max strain (should not happen)
    return eps_grid[-1]

def compute_properties(temp):
    V_a0, V_f0, V_m0 = PHASE_FRACS[temp]
    alpha, beta, m = OC_PARAMS[temp]

    # fine true strain grid
    eps_true = np.linspace(0, 1.5, 300001)
    
    # transformed fraction of initial austenite
    f_trans = 1.0 - np.exp(-beta * (1.0 - np.exp(-alpha * eps_true))**m)
    
    # phase fractions
    V_aus = V_a0 * (1.0 - f_trans)
    V_mar = V_m0 + V_a0 * f_trans
    V_fer = np.full_like(eps_true, V_f0)
    
    # Hollomon flow stresses
    s_fer = HOLLOMON['ferrite'][0] * eps_true**HOLLOMON['ferrite'][1]
    s_aus = HOLLOMON['austenite'][0] * eps_true**HOLLOMON['austenite'][1]
    s_mar = HOLLOMON['martensite'][0] * eps_true**HOLLOMON['martensite'][1]
    
    # composite true stress (rule of mixtures)
    sigma_c = s_fer * V_fer + s_aus * V_aus + s_mar * V_mar
    
    # apply Considère condition to get instability true strain
    eps_inst_true = secant_solve_conssidere(eps_true, sigma_c)
    
    # convert to engineering quantities at instability
    eps_inst_eng = np.exp(eps_inst_true) - 1.0
    # interpolate composite stress at that strain
    sigma_inst_true = np.interp(eps_inst_true, eps_true, sigma_c)
    sigma_inst_eng = sigma_inst_true / np.exp(eps_inst_true)
    
    # generate engineering stress-strain curve up to instability (step <= 0.001)
    n_points = max(int(np.ceil(eps_inst_eng / 0.001)) + 1, 2)
    eps_sampled = np.linspace(0, eps_inst_eng, n_points)
    # convert corresponding true strains
    eps_true_sampled = np.log(1.0 + eps_sampled)
    # recompute sigma_c at those strains (via interpolation for speed)
    sigma_c_sampled = np.interp(eps_true_sampled, eps_true, sigma_c)
    sig_eng_sampled = sigma_c_sampled / np.exp(eps_true_sampled)
    
    return sigma_inst_eng, eps_inst_eng, eps_sampled, sig_eng_sampled

# Compute for each temperature
prop_rows = []
curve_rows = []
for T in TEMPERATURES:
    uts, ue, eps_curve, sig_curve = compute_properties(T)
    prop_rows.append([T, round(uts, 2), round(ue, 6)])
    for e, s in zip(eps_curve, sig_curve):
        curve_rows.append([T, round(e, 6), round(s, 3)])

# Write predicted_properties.csv
with open(os.path.join(OUTDIR, "predicted_properties.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["annealing_temperature_C", "predicted_UTS_MPa", "predicted_uniform_elongation"])
    w.writerows(prop_rows)

# Write stress_strain_curves.csv
with open(os.path.join(OUTDIR, "stress_strain_curves.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["annealing_temperature_C", "engineering_strain", "engineering_stress_MPa"])
    w.writerows(curve_rows)

print("predicted_properties.csv and stress_strain_curves.csv written successfully")
PYEOF

# === solve block: stress_strain_curves.csv ===
# already written by gen_outputs.py
