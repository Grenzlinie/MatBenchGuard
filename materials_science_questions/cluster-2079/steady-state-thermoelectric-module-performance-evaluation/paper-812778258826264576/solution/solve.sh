#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/compute.py /app/outputs

# === solve block: efficiency_vs_a.csv ===
python3 << 'EOF' "$OUTDIR"
import csv, math, os, sys

outdir = os.environ['OUTDIR']

# Constants
L = 4.0e-3          # m
A0 = 16.0e-6        # m^2
Tlow = 300.0        # K

# Temperature-dependent material property functions (T in K)
# n-type material-1
def kn1(T): return 0.6586 + 329.63/T + 22145.0/(T*T)
def alphan1_abs(T): return 173.26 - 3.8229*T + 0.011679*T*T - 1.5584e-5*T**3 + 7.6695e-9*T**4
def sigman1(T): return 1462.0 - 10.419*T + 0.031315*T*T - 4.029e-5*T**3 + 1.9034e-8*T**4

# p-type material-1
def kp1(T): return 0.56959 + 550.66/T - 47483.0/(T*T)
def alphap1(T): return 1450.0 - 10.36*T + 0.03123*T*T - 4.038e-5*T**3 + 1.903e-8*T**4
def sigmap1(T): return 179.02 + 12.336*T - 0.042167*T*T + 5.129e-5*T**3 - 2.1435e-8*T**4

# n-type material-2
def kn2(T): return -4.6205 + 9.9277e-3*T + 833.7/T + 235636.0/(T*T)
def alphan2_abs(T): return 443.49 - 4.5121*T + 9.4424e-3*T*T - 5.8362e-6*T**3
def sigman2(T): return -2139.4 + 2.5778*T + math.exp(12.795 - 0.89098*math.log(T))

# p-type material-2
def kp2(T): return -1.8067 + 5.729e-3*T - 64.639/T + 1.3395e5/(T*T)
def alphap2(T): return -188.2 + 2.2411*T - 3.0075e-3*T*T + 2.4914e-7*T**3
def sigmap2(T): return -473.1 + 0.86507*T + math.exp(16.637 - 1.6942*math.log(T))

# Reference values at 273 K
Tref = 273.15
K0 = kn1(Tref) * A0 / L
R0 = L / (sigman1(Tref) * A0)

mu_n = 0.5
mu_p = 0.5

def solve_TEG(a, theta, RL_R0):
    Thigh = Tlow / theta
    # Initial guess interface temperatures
    Tint_n = (Thigh + Tlow) / 2.0
    Tint_p = (Thigh + Tlow) / 2.0

    for _ in range(20):
        Tn1_avg = (Thigh + Tint_n) * 0.5
        Tn2_avg = (Tint_n + Tlow) * 0.5
        Tp1_avg = (Thigh + Tint_p) * 0.5
        Tp2_avg = (Tint_p + Tlow) * 0.5

        k_n1 = kn1(Tn1_avg)
        k_n2 = kn2(Tn2_avg)
        k_p1 = kp1(Tp1_avg)
        k_p2 = kp2(Tp2_avg)

        # Effective thermal conductivities
        if abs(a) < 1e-12:
            k_neff = 1.0 / (mu_n/k_n1 + (1-mu_n)/k_n2)
        else:
            exp_a = math.exp(a)
            exp_amu = math.exp(a*mu_n)
            denom = (1 - math.exp(-a)) * ((exp_amu - 1)/k_n1 + (exp_a - exp_amu)/k_n2)
            k_neff = a*a / denom if denom != 0 else 1e12

        k_peff = 1.0 / (mu_p/k_p1 + (1-mu_p)/k_p2)

        dT_total = Thigh - Tlow
        if abs(a) < 1e-12:
            dT_n1 = (k_neff/k_n1) * mu_n * dT_total
            dT_n2 = (k_neff/k_n2) * (1 - mu_n) * dT_total
        else:
            dT_n1 = (k_neff/k_n1) * ((1 - math.exp(-a)) * (math.exp(a*mu_n) - 1) / (a*a)) * dT_total
            dT_n2 = (k_neff/k_n2) * ((1 - math.exp(-a)) * (math.exp(a) - math.exp(a*mu_n)) / (a*a)) * dT_total

        dT_p1 = (k_peff/k_p1) * mu_p * dT_total
        dT_p2 = (k_peff/k_p2) * (1 - mu_p) * dT_total

        new_Tint_n = Thigh - dT_n1
        new_Tint_p = Thigh - dT_p1
        if abs(new_Tint_n - Tint_n) < 1e-6 and abs(new_Tint_p - Tint_p) < 1e-6:
            Tint_n = new_Tint_n
            Tint_p = new_Tint_p
            break
        Tint_n = new_Tint_n
        Tint_p = new_Tint_p

    # Final property evaluation
    Tn1_avg = (Thigh + Tint_n) * 0.5
    Tn2_avg = (Tint_n + Tlow) * 0.5
    Tp1_avg = (Thigh + Tint_p) * 0.5
    Tp2_avg = (Tint_p + Tlow) * 0.5

    k_n1 = kn1(Tn1_avg)
    k_n2 = kn2(Tn2_avg)
    alpha_n1 = -alphan1_abs(Tn1_avg)   # n-type negative
    alpha_n2 = -alphan2_abs(Tn2_avg)
    sigma_n1 = sigman1(Tn1_avg)
    sigma_n2 = sigman2(Tn2_avg)

    k_p1 = kp1(Tp1_avg)
    k_p2 = kp2(Tp2_avg)
    alpha_p1 = alphap1(Tp1_avg)
    alpha_p2 = alphap2(Tp2_avg)
    sigma_p1 = sigmap1(Tp1_avg)
    sigma_p2 = sigmap2(Tp2_avg)

    # Effective thermal conductivities (final)
    if abs(a) < 1e-12:
        k_neff = 1.0 / (mu_n/k_n1 + (1-mu_n)/k_n2)
    else:
        exp_a = math.exp(a)
        exp_amu = math.exp(a*mu_n)
        k_neff = a*a / ((1 - math.exp(-a)) * ((exp_amu - 1)/k_n1 + (exp_a - exp_amu)/k_n2))
    k_peff = 1.0 / (mu_p/k_p1 + (1-mu_p)/k_p2)

    # Effective Seebeck coefficients
    if abs(a) < 1e-12:
        alpha_neff = alpha_n1 * (k_neff/k_n1) * mu_n + alpha_n2 * (k_neff/k_n2) * (1 - mu_n)
    else:
        term1_n = (1 - math.exp(-a)) * (math.exp(a*mu_n) - 1) / (a*a)
        term2_n = (1 - math.exp(-a)) * (math.exp(a) - math.exp(a*mu_n)) / (a*a)
        alpha_neff = alpha_n1 * (k_neff/k_n1) * term1_n + alpha_n2 * (k_neff/k_n2) * term2_n

    alpha_peff = alpha_p1 * (k_peff/k_p1) * mu_p + alpha_p2 * (k_peff/k_p2) * (1 - mu_p)
    alpha_eff = alpha_peff - alpha_neff   # in μV/K

    # Electrical resistances
    if abs(a) < 1e-12:
        Rn = (L/A0) * (mu_n/sigma_n1 + (1-mu_n)/sigma_n2)
    else:
        Rn = ((1 - math.exp(-a)) * L / (a*a * A0)) * ((math.exp(a*mu_n) - 1)/sigma_n1 + (math.exp(a) - math.exp(a*mu_n))/sigma_n2)
    Rp = (1.0/A0) * (mu_p*L/sigma_p1 + (1-mu_p)*L/sigma_p2)
    R_TEG = Rn + Rp

    # Segment 1 resistances (material-1 only)
    if abs(a) < 1e-12:
        Rn1 = mu_n * L / (sigma_n1 * A0)
    else:
        Rn1 = ((1 - math.exp(-a)) * L / (a*a * A0)) * (math.exp(a*mu_n) - 1) / sigma_n1
    Rp1 = mu_p * L / (sigma_p1 * A0)

    # Effective thermal conductance
    K_eff = (k_neff + k_peff) * A0 / L

    # alpha_eff,1 for unsegmented material-1
    # For n-leg unsegmented material-1 (mu=1)
    # k_neff1: single material
    if abs(a) < 1e-12:
        k_neff1 = k_n1
        alpha_neff1 = alpha_n1
    else:
        k_neff1 = a*a * k_n1 / ((1 - math.exp(-a)) * (math.exp(a) - 1))
        term1n1 = (1 - math.exp(-a)) * (math.exp(a) - 1) / (a*a)
        alpha_neff1 = alpha_n1 * (k_neff1/k_n1) * term1n1

    alpha_peff1 = alpha_p1   # uniform
    alpha_eff1 = alpha_peff1 - alpha_neff1  # μV/K

    # ZT_avg (use alpha in V/K)
    alpha_eff_V = alpha_eff * 1e-6          # convert μV/K to V/K
    ZT_avg = (alpha_eff_V**2 * Thigh * (1+theta)) / (2 * R_TEG * K_eff)

    # Efficiency (fraction)
    numer = 2 * ZT_avg * (1-theta) * (RL_R0) * (R_TEG/R0)
    denom = (
        2 * (alpha_eff1/alpha_eff) * (R_TEG/R0 + RL_R0) * (R_TEG/R0)
        + (1+theta) * (R_TEG/R0 + RL_R0)**2
        - 2 * ZT_avg * (1-theta)
        + (R_TEG/R0) * ((Rn1 + Rp1)/R0)
    )
    eff = numer / denom if denom != 0 else 0.0
    return max(0.0, min(eff, 1.0))  # clamp to [0,1]

# Parameter grid
theta_vals = [0.45, 0.55]
RL_vals = [2, 4, 6, 8]
a_vals = [round(-3.0 + 0.5*i, 1) for i in range(13)]  # -3.0 to 3.0 step 0.5

outfile = os.path.join(outdir, 'efficiency_vs_a.csv')
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['theta', 'RL_R0', 'a', 'efficiency_percent'])
    for theta in theta_vals:
        for RL_R0 in RL_vals:
            for a in a_vals:
                eta_pct = solve_TEG(a, theta, RL_R0) * 100.0
                writer.writerow([theta, RL_R0, a, eta_pct])
EOF

# === solve block: power_vs_a.csv ===
true

# === solve block: current_vs_a.csv ===
true

# === solve block: work_ratio_vs_a.csv ===
true
