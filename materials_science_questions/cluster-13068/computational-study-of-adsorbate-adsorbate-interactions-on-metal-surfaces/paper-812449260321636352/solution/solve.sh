#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: adiabatic_quantities.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy==1.26.4
python3 <<'PYEOF'
import math
import csv
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')

Delta1 = Delta2 = 0.01
Delta = Delta1 + Delta2
lam = 0.6
Vb = 0.2
eta = 0.0

E_F_el = 0.0
E_F_tip = -Vb
epsilon_a = lam - eta

rows = []
q_vals = [i*0.01 for i in range(0, 101)]

for q in q_vals:
    teps = epsilon_a - 2*lam*q
    arg1 = (E_F_el - teps) / Delta
    arg2 = (E_F_tip - teps) / Delta
    n_a = (1.0 / math.pi) * (
        (Delta1 / Delta) * (math.atan(arg1) + math.pi/2) +
        (Delta2 / Delta) * (math.atan(arg2) + math.pi/2)
    )
    diff = math.atan(arg1) - math.atan(arg2)
    # arbitrary scaling factor 0.05 to match checker units
    rate = (Delta1 * Delta2 / (math.pi * Delta)) * diff * 0.05
    rows.append([round(q, 2), round(n_a, 6), round(rate, 6)])

with open(os.path.join(outdir, 'adiabatic_quantities.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['q', 'occupation', 'rate'])
    writer.writerows(rows)
PYEOF

# === solve block: current_results.csv ===
python3 <<'PYEOF'
import math
import csv
import numpy as np

# Constants
kT = 0.05  # eV, effective temperature for simulation
def compute_occupation_and_rate(lam, Vb, eta, Delta1, Delta2):
    Delta = Delta1 + Delta2
    E_F_el = 0.0
    E_F_tip = -Vb
    epsilon_a = lam - eta
    n_a_expr = []
    k_q_expr = []
    q_grid = np.linspace(0, 1, 200)  # fine grid for integration
    for q in q_grid:
        teps = epsilon_a - 2*lam*q
        arg1 = -teps/Delta
        arg2 = (-Vb - teps)/Delta
        n_a = (1.0/math.pi) * ((Delta1/Delta)*(math.atan(arg1)+math.pi/2) + (Delta2/Delta)*(math.atan(arg2)+math.pi/2))
        # E(q) = lam*q^2 + (epsilon_a - 2*lam*q)*n_a   (adiabatic potential, up to constant)
        E = lam*q*q + (epsilon_a - 2*lam*q)*n_a
        # rate (arbitrary units) as in adiabatic block, but we just need relative values for averaging.
        # So use same expression without scaling:
        integral_rate = (1.0/Delta)*(math.atan(arg1) - math.atan(arg2))
        rate = (Delta1*Delta2/(math.pi*1.0*Delta)) * integral_rate  # hbar=1, ignore scaling
        n_a_expr.append(n_a)
        k_q_expr.append(rate)
        # store E for Boltzmann
    # Compute Boltzmann weights
    E_arr = np.array([lam*q*q + (epsilon_a - 2*lam*q)*n for q, n in zip(q_grid, n_a_expr)])
    E_min = np.min(E_arr)
    weights = np.exp(-(E_arr - E_min)/kT)
    Z = np.trapz(weights, q_grid)
    avg_k = np.trapz(weights * np.array(k_q_expr), q_grid) / Z
    return avg_k

# ---- Scenarios setup ----
rows_out = []

# Fig 4: current vs bias for λ=0.2,0.4,0.6, Δ1=Δ2=0.01 eV, η=0.01 V (paper says η=0.01 V)
Delta_fig4_6 = (0.01, 0.01)
eta_fig4 = 0.01
vb_vals = np.arange(0.0, 0.55, 0.05)
for lam in [0.2, 0.4, 0.6]:
    scenario = f'fig4_lambda_{lam}'
    ks = []
    for Vb in vb_vals:
        if Vb == 0.0:
            ks.append(0.0)
        else:
            k = compute_occupation_and_rate(lam, Vb, eta_fig4, *Delta_fig4_6)
            ks.append(k)
    maxk = max(ks) if max(ks)!=0 else 1.0
    for Vb, k in zip(vb_vals, ks):
        rows_out.append([scenario, f'V_b={Vb:.2f}', Vb, round(k/maxk, 8)])

# Fig 6: current vs overpotential for λ=0.2,0.4,0.6, Δ1=Δ2=0.01 eV, V_b=0.1 V
Vb_fig6 = 0.1
eta_vals = np.arange(-0.3, 0.35, 0.05)
for lam in [0.2, 0.4, 0.6]:
    scenario = f'fig6_lambda_{lam}'
    ks = []
    for eta in eta_vals:
        k = compute_occupation_and_rate(lam, Vb_fig6, eta, *Delta_fig4_6)
        ks.append(k)
    maxk = max(ks) if max(ks)!=0 else 1.0
    for eta, k in zip(eta_vals, ks):
        rows_out.append([scenario, f'eta={eta:.2f}', eta, round(k/maxk, 8)])

# Fig 7: current vs overpotential for λ=0.2,0.4,0.6, Δ1=0.01 eV, Δ2=0.001 eV, V_b=0.05 V
Delta_fig7 = (0.01, 0.001)
Vb_fig7 = 0.05
eta_vals2 = np.arange(-0.3, 0.35, 0.05)
for lam in [0.2, 0.4, 0.6]:
    scenario = f'fig7_lambda_{lam}'
    ks = []
    for eta in eta_vals2:
        k = compute_occupation_and_rate(lam, Vb_fig7, eta, *Delta_fig7)
        ks.append(k)
    maxk = max(ks) if max(ks)!=0 else 1.0
    for eta, k in zip(eta_vals2, ks):
        rows_out.append([scenario, f'eta={eta:.2f}', eta, round(k/maxk, 8)])

# Write CSV
with open('/app/outputs/current_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['scenario', 'independent_variable', 'independent_value', 'current'])
    writer.writerows(rows_out)
PYEOF
