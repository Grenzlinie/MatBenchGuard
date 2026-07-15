#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: driving_forces.csv ===
python3 - << 'PYEOF'
import numpy as np
import csv, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
R = 8.314

# --- parameters (W in K, E in kJ/mol -> convert to J/mol) ---
W_CuZn1 = 955; W_CuZn2 = 535
W_CuAl1 = 1345; W_CuAl2 = 825
W_ZnAl1 = -50; W_ZnAl2 = 200
W_CuZn_a = 582; W_CuAl_a = 1459; W_ZnAl_a = 0

E_CuZn_a = -29.047 * 1000
E_CuZn_b = -43.014 * 1000
E_CuAl_a = -72.781 * 1000
E_CuAl_b = -65.306 * 1000
E_ZnAl_a = 0.0
E_ZnAl_b = -3.326 * 1000

# lattice stability functions (J/mol)
def DG_Cu1_b_a(T): return 7232.40 + 3.14348 * T
def DG_Cu2_b_a(T): return -1221.81 + 0.11418 * T + 8.837e-5 * T**2
def DG_Zn_b_a(T): return -325.08 - 0.79713 * T - 8.1704e-4 * T**2
def DG_Al_b_a(T): return 8212.38 + 2.75113 * T

x_CuZn = 0.67; x_CuAl = 0.78

# compositions
X_Cu_main = 0.6933; X_Zn_main = 0.2667; X_Al_main = 0.0400
X_Zn_bp = 0.2477; X_Al_bp = 0.0900; X_Cu_bp = 1 - X_Zn_bp - X_Al_bp
X_Zn_b1p = 0.2480; X_Al_b1p = 0.0902; X_Cu_b1p = 1 - X_Zn_b1p - X_Al_b1p
X_Zn_a = 0.2218; X_Al_a = 0.0738; X_Cu_a = 1 - X_Zn_a - X_Al_a

def eta_beta(T):
    if T >= 770: return 0.0
    return 0.32 * np.sqrt(1 - (T/770)**5)
def eta_alpha(T):
    if T >= 770: return 0.0
    return 0.20 * np.sqrt(1 - (T/770)**5)

def safe_log(x):
    return np.log(x) if x > 0 else 0.0

def S_conf(X_Cu, eta):
    return (2*X_Cu*safe_log(X_Cu)
            + 2*(1-X_Cu)*safe_log(1-X_Cu)
            - (eta+X_Cu)*safe_log(eta+X_Cu)
            - (1-X_Cu-eta)*safe_log(1-X_Cu-eta)
            - (eta+1-X_Cu)*safe_log(eta+1-X_Cu)
            - (X_Cu-eta)*safe_log(X_Cu-eta))

def x_tern(X_Zn, X_Al):
    denom = X_Zn + X_Al
    return (X_Zn * x_CuZn + X_Al * x_CuAl) / denom if denom != 0 else 0.0

def G_regular_phase(phase, X_Cu, X_Zn, X_Al, T):
    if phase == 'beta':
        G_Cu = 0.0; G_Zn = 0.0; G_Al = 0.0
        E_CuZn = E_CuZn_b; E_CuAl = E_CuAl_b; E_ZnAl = E_ZnAl_b
    else:
        denom = X_Zn + X_Al
        if denom == 0:
            G_Cu = DG_Cu1_b_a(T)
        else:
            G_Cu = (X_Zn * DG_Cu1_b_a(T) + X_Al * DG_Cu2_b_a(T)) / denom
        G_Zn = DG_Zn_b_a(T); G_Al = DG_Al_b_a(T)
        E_CuZn = E_CuZn_a; E_CuAl = E_CuAl_a; E_ZnAl = E_ZnAl_a
    G0 = X_Cu*G_Cu + X_Zn*G_Zn + X_Al*G_Al
    S_ideal = -(X_Cu*safe_log(X_Cu) + X_Zn*safe_log(X_Zn) + X_Al*safe_log(X_Al))
    H_mix = E_CuZn*X_Cu*X_Zn + E_CuAl*X_Cu*X_Al + E_ZnAl*X_Zn*X_Al
    return G0 - R*T*S_ideal + H_mix

def DeltaU_beta_to_betaprime(X_Zn, X_Al, eta):
    total_XZ = X_Zn + X_Al
    if total_XZ == 0: return 0.0
    frac_Zn = X_Zn / total_XZ; frac_Al = X_Al / total_XZ
    term1 = frac_Zn * (6*W_CuZn2 - 8*W_CuZn1)
    term2 = frac_Al * (6*W_CuAl2 - 8*W_CuAl1)
    cross = (X_Zn*X_Al) / total_XZ**2
    term3 = cross * (6*W_ZnAl2 - 8*W_ZnAl1)
    return 0.5 * R * eta**2 * (term1 + term2 - term3)

def DeltaU_alpha_to_alphaprime(X_Zn, X_Al, eta):
    total_XZ = X_Zn + X_Al
    if total_XZ == 0: return 0.0
    frac_Zn = X_Zn / total_XZ; frac_Al = X_Al / total_XZ
    cross = (X_Zn*X_Al) / total_XZ**2
    term = -frac_Zn * W_CuZn_a - frac_Al * W_CuAl_a + cross * W_ZnAl_a
    return 2 * R * eta**2 * term

def DeltaG_beta_to_betaprime_full(X_Cu, X_Zn, X_Al, eta, T):
    DeltaU = DeltaU_beta_to_betaprime(X_Zn, X_Al, eta)
    x_val = x_tern(X_Zn, X_Al)
    if x_val == 0: return DeltaU
    return DeltaU - (R * T / (2 * x_val)) * S_conf(X_Cu, eta)

Ts = np.arange(300, 751, 50)
dG_bap = []; dG_ba = []; dG_diff = []; dG_aap = []

for T in Ts:
    eta = eta_beta(T); eta_a = eta_alpha(T)
    G_beta_main = G_regular_phase('beta', X_Cu_main, X_Zn_main, X_Al_main, T)
    G_alpha_main = G_regular_phase('alpha', X_Cu_main, X_Zn_main, X_Al_main, T)
    dgba = G_alpha_main - G_beta_main
    dG_ba.append(dgba)

    DeltaU_bbp = DeltaU_beta_to_betaprime(X_Zn_main, X_Al_main, eta)
    DeltaU_aap = DeltaU_alpha_to_alphaprime(X_Zn_a, X_Al_a, eta_a)
    dG_bap.append(-DeltaU_bbp + dgba + DeltaU_aap)

    G_beta_bp = G_regular_phase('beta', X_Cu_bp, X_Zn_bp, X_Al_bp, T)
    DG_bp = DeltaG_beta_to_betaprime_full(X_Cu_bp, X_Zn_bp, X_Al_bp, eta, T)
    G_bp_ordered = G_beta_bp + DG_bp

    G_beta_b1p = G_regular_phase('beta', X_Cu_b1p, X_Zn_b1p, X_Al_b1p, T)
    DG_b1p = DeltaG_beta_to_betaprime_full(X_Cu_b1p, X_Zn_b1p, X_Al_b1p, eta, T)
    G_b1p_disordered = G_beta_b1p
    G_alpha_a = G_regular_phase('alpha', X_Cu_a, X_Zn_a, X_Al_a, T)

    num = X_Zn_bp - X_Zn_a; den = X_Zn_b1p - X_Zn_a
    factor = num / den if den != 0 else 0
    dG_diff.append(G_alpha_a + factor * (G_b1p_disordered - G_alpha_a) - G_bp_ordered)

    DeltaU_a_ord = DeltaU_alpha_to_alphaprime(X_Zn_a, X_Al_a, eta_a)
    x_a = x_tern(X_Zn_a, X_Al_a)
    if x_a == 0:
        dG_a_ord = DeltaU_a_ord
    else:
        dG_a_ord = DeltaU_a_ord - (R * T / (2 * x_a)) * S_conf(X_Cu_a, eta_a)
    dG_aap.append(dG_a_ord)

# write CSV
header = ['T', "DG_beta'_to_alpha'", 'DG_beta_to_alpha', "DG_beta'_to_beta1'_plus_alpha", "DG_alpha_to_alpha'"]
with open(f'{OUTDIR}/driving_forces.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i, T in enumerate(Ts):
        writer.writerow([T, dG_bap[i], dG_ba[i], dG_diff[i], dG_aap[i]])

# Write a self-contained script to produce polynomial_coefficients.json from the CSV
script = r"""
import csv, json, os
import numpy as np

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
Ts = []
dGs = []
with open(f'{OUTDIR}/driving_forces.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        Ts.append(float(row[0]))
        dGs.append(float(row[1]))

coeffs = np.polyfit(Ts, dGs, 3)
a0, a1, a2, a3 = coeffs[3], coeffs[2], coeffs[1], coeffs[0]
with open(f'{OUTDIR}/polynomial_coefficients.json', 'w') as f:
    json.dump({"constant": a0, "T": a1, "T2": a2, "T3": a3}, f)
"""
with open('/solution/compute.py', 'w') as f:
    f.write(script)
PYEOF

# === solve block: polynomial_coefficients.json ===
python3 /solution/compute.py
