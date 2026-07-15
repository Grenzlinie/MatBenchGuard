#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: computed_curves.csv ===
python3 <<'EOF'
import numpy as np
from scipy.integrate import quad
import csv

A_e1_C = 727.0
A_e1_K = A_e1_C + 273.15
s_cem = 25e-9

D0_g = 2.3e-5
Q_g  = 137700.0
def D_gamma(T_K):
    return D0_g * np.exp(-Q_g / (8.314 * T_K))

D0_a = 1.1e-6
Q_a  = 87500.0
def D_alpha(T_K):
    return D0_a * np.exp(-Q_a / (8.314 * T_K))

T_max_C_list = [750.0, 800.0, 850.0, 900.0]
tau_values   = np.logspace(np.log10(1e-5), np.log10(0.5), num=500)

rows = []
for T_max_C in T_max_C_list:
    T_max_K = T_max_C + 273.15
    # average austenite diffusion coefficient
    int_g, _    = quad(D_gamma, A_e1_K, T_max_K)
    D_avg_g     = int_g / (T_max_K - A_e1_K)
    D_Tmax_g    = D_gamma(T_max_K)
    # average ferrite diffusion coefficient
    int_a, _    = quad(D_alpha, A_e1_K, T_max_K)
    D_avg_a     = int_a / (T_max_K - A_e1_K)
    D_Tmax_a    = D_alpha(T_max_K)
    # mixed average
    D_mixed     = (D_avg_g + D_avg_a) / 2.0
    # thermodynamic factor: (T_max/A_e1 - 1) in Kelvin
    ratio_factor = (T_max_K / A_e1_K - 1.0) / s_cem
    candidates = [
        ('Dγ_avg',   D_avg_g),
        ('Dγ_Tmax',  D_Tmax_g),
        ('Dα_avg',   D_avg_a),
        ('Dα_Tmax',  D_Tmax_a),
        ('D_mixed',  D_mixed),
    ]
    for label, D_val in candidates:
        prefactor = ratio_factor * np.sqrt(D_val)
        for tau in tau_values:
            f_p_gamma = prefactor * np.sqrt(tau)
            rows.append((T_max_C, label, tau, f_p_gamma))

with open('/app/outputs/computed_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T_max_C', 'D_candidate', 'tau_s', 'f_p_gamma'])
    writer.writerows(rows)
EOF
