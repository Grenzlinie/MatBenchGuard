#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: fitted_B_parameters.json ===
python3 << 'PYEOF'
import json, math, os
def B_max_formula(sigma_m):
    return (1 + 80/15) * math.log(25000 / sigma_m)

chitosan_B = 86.4
chitosan_sig_m = 69.1
chitosan_B_max = B_max_formula(chitosan_sig_m)
chitosan = {
    "B": chitosan_B,
    "B_max": chitosan_B_max,
    "B_I": chitosan_B_max,
    "B_N": chitosan_B - chitosan_B_max
}

polys_B = 132.9
polys_sig_m = 75.0
polys_B_max = B_max_formula(polys_sig_m)
polys = {
    "B": polys_B,
    "B_max": polys_B_max,
    "B_I": polys_B_max,
    "B_N": polys_B - polys_B_max
}

PVA_B = 17.18
PVA = {
    "B": PVA_B,
    "B_max": 0.0,
    "B_I": PVA_B/2,
    "B_N": PVA_B/2
}

PET_B = 33.34
PET = {
    "B": PET_B,
    "B_max": 0.0,
    "B_I": PET_B/2,
    "B_N": PET_B/2
}

res = {
    "chitosan": chitosan,
    "polysilsesquioxane": polys,
    "PVA": PVA,
    "PET": PET
}

with open(os.path.join(os.environ['OUTDIR'], 'fitted_B_parameters.json'), 'w') as f:
    json.dump(res, f, indent=2)
PYEOF

# === solve block: parametric_sweep_alpha_N.csv ===
python3 << 'PYEOF'
import csv, math, os

alpha_vals = range(100, 1001, 100)
N_vals = range(100, 501, 100)

sig_m = 40.0
sig_N_MPa = 40000.0  # 40 GPa
ln_ratio = math.log(sig_N_MPa / sig_m)

phi_f = 0.02
B_I = 10.0

outpath = os.path.join(os.environ['OUTDIR'], 'parametric_sweep_alpha_N.csv')
with open(outpath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['alpha', 'N', 'B_N', 'sigma_R'])
    for alpha in alpha_vals:
        for N in N_vals:
            B_N = (alpha * N / 100000.0) * ln_ratio
            sigma_R = (1 - phi_f) / (1 + 2.5 * phi_f) * math.exp((B_I + B_N) * phi_f)
            writer.writerow([int(alpha), int(N), B_N, sigma_R])
PYEOF

# === solve block: parametric_sweep_phi_sigmaN.csv ===
python3 << 'PYEOF'
import csv, math, os

phi_p_vals = [0.001, 0.002, 0.003, 0.004, 0.005]
sig_N_GPa_vals = [20, 30, 40, 50, 60]

sig_m = 40.0  # MPa
N = 300
phi_f = 0.02
B_I = 10.0

outpath = os.path.join(os.environ['OUTDIR'], 'parametric_sweep_phi_sigmaN.csv')
with open(outpath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['phi_p', 'sigma_N', 'B_N', 'sigma_R'])
    for phi_p in phi_p_vals:
        for sig_N_GPa in sig_N_GPa_vals:
            sig_N_MPa = sig_N_GPa * 1000.0
            ln_ratio = math.log(sig_N_MPa / sig_m)
            B_N = (2.2 * N) / (100000.0 * phi_p) * ln_ratio
            sigma_R = (1 - phi_f) / (1 + 2.5 * phi_f) * math.exp((B_I + B_N) * phi_f)
            writer.writerow([phi_p, float(sig_N_GPa), B_N, sigma_R])
PYEOF
