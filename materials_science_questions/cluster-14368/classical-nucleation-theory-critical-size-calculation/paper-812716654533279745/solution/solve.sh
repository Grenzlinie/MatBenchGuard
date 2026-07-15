#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
python3 << 'PYEOF'
import math, csv

# Constants
T = 279.15  # K
P = 90000.0 # Pa
g = 9.81
R_d = 287.058
R_v = 461.5
c_p = 1005.0
rho_w = 1000.0
sigma_w = 0.073
L_w = 2.501e6

# air density
rho_a = P / (R_d * T)

# saturation vapor pressure (Pa)
T_C = T - 273.15
e_s_hPa = 6.112 * math.exp(17.67 * T_C / (T_C + 243.5))
e_s = e_s_hPa * 100.0
q_vs = 0.622 * e_s / (P - e_s)

# A1
A1 = g/(R_d*T) * (L_w * R_d / (c_p * R_v * T) - 1.0)

# D (diffusivity) in m2/s
D = 2.11e-5 * (T/273.15)**1.94 * (101325.0/P)

# k_a (thermal conductivity of air) J/(m s K)
k_a = 2.38e-2 * (T/273.15)**0.71

# F
F = (rho_w * L_w**2) / (k_a * R_v * T**2) + (rho_w * R_v * T) / (e_s * D)

# A2
A2 = 1.0/q_vs + L_w**2 / (c_p * R_v * T**2)

# Koehler A and B
A = 2.0 * sigma_w / (rho_w * R_v * T)  # in meters
B = (3 * 1.0 * 1.0 * 0.018 * 1769.0) / (0.132 * 1000.0)  # dimensionless (ammonium sulfate)

# Table S_max* vs Q0 (from instruction)
smax_star_data = [
    (0.0, 1.0540), (0.1, 0.9589), (0.2, 0.9147), (0.3, 0.8821), (0.4, 0.8557),
    (0.5, 0.8333), (0.6, 0.8139), (0.7, 0.7967), (0.8, 0.7812), (0.9, 0.7672),
    (1.0, 0.7543), (1.1, 0.7425), (1.2, 0.7315), (1.3, 0.7214), (1.4, 0.7120),
    (1.5, 0.7032), (1.6, 0.6931), (1.7, 0.6850), (1.8, 0.6772), (1.9, 0.6698),
    (2.0, 0.6628), (2.1, 0.6561), (2.2, 0.6497)
]

def interpolate_Smax_star(Q0):
    if Q0 <= 0.0:
        return smax_star_data[0][1]
    if Q0 >= 2.2:
        return smax_star_data[-1][1]
    for i in range(len(smax_star_data)-1):
        q0_i, sm_i = smax_star_data[i]
        q0_next, sm_next = smax_star_data[i+1]
        if q0_i <= Q0 <= q0_next:
            return sm_i + (sm_next - sm_i) * (Q0 - q0_i) / (q0_next - q0_i)
    return smax_star_data[-1][1]

# Aerosol types data (R in µm, sigma, N in cm^-3)
aerosol_data = {
    'marine': [
        (0.005, 1.6, 340),
        (0.035, 2.0, 60),
        (0.31, 2.7, 3.1)
    ],
    'clean_continental': [
        (0.008, 1.6, 1000),
        (0.034, 2.1, 800),
        (0.46, 2.2, 0.72)
    ],
    'background': [
        (0.008, 1.7, 6400),
        (0.038, 2.0, 2300),
        (0.51, 2.16, 3.2)
    ],
    'urban': [
        (0.007, 1.8, 106000),
        (0.027, 2.16, 32000),
        (0.43, 2.21, 5.4)
    ]
}

def compute_N_and_r0(aer_type, r_n_cr):
    modes = aerosol_data[aer_type]
    N_total = 0.0
    sum_r0_term = 0.0
    for R_um, sigma, N_cm3 in modes:
        R_m = R_um * 1e-6
        N_m3 = N_cm3 * 1e6
        ln_sigma = math.log(sigma)
        arg = math.log(r_n_cr / R_m) / (math.sqrt(2.0) * ln_sigma)
        N_i = N_m3 * 0.5 * (1.0 - math.erf(arg))
        N_total += N_i
        alpha_i = 1.5 * ln_sigma
        R_i_star = math.sqrt(B * R_m**3 / A)
        r_star = math.sqrt(B/A) * r_n_cr**1.5
        term = 0.5 * N_m3 * R_i_star * math.exp(0.5 * alpha_i**2)
        if alpha_i > 0:
            arg2 = (math.log(R_i_star) + alpha_i**2 - math.log(r_star)) / (math.sqrt(2.0) * alpha_i)
            factor = 1.0 + math.erf(arg2)
        else:
            factor = 1.0
        sum_r0_term += term * factor
    if N_total == 0.0:
        r0 = 0.0
    else:
        r0 = sum_r0_term / N_total
    return N_total, r0

def iterate(aer_type, w, q2):
    S_max_old = 0.01
    for _ in range(1000):
        r_n_cr = A/3.0 * (4.0/(B * S_max_old**2))**(1.0/3.0)
        N, r0 = compute_N_and_r0(aer_type, r_n_cr)
        if N == 0.0:
            return 0.0, 0.0
        R_val = (3.0/(F * A1 * w)) * (4.0 * math.pi * rho_w * A2 * N / (3.0 * rho_a))**(2.0/3.0)
        q1_liquid = (4.0/3.0 * math.pi * rho_w * N * r0**3) / rho_a
        Q0 = R_val**0.75 * A2 * (q1_liquid + q2)
        S_max_star = interpolate_Smax_star(Q0)
        S_max_new = R_val**(-0.75) * S_max_star
        if abs(S_max_new - S_max_old) / S_max_old < 1e-6:
            return S_max_new, N
        S_max_old = S_max_new
    return S_max_new, N

# Build conditions
conditions = []
for aer in aerosol_data.keys():
    w_list = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    q2_list = [0.0]
    if aer in ('marine', 'clean_continental'):
        q2_list.extend([1e-5, 1e-4])
    for w_val in w_list:
        for q2_val in q2_list:
            conditions.append((aer, w_val, q2_val))

rows = []
for aer, w_val, q2_val in conditions:
    S_max, N_val = iterate(aer, w_val, q2_val)
    rows.append([aer, w_val, q2_val, S_max, N_val])

with open('/app/outputs/results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['aerosol_type', 'w', 'q2', 'S_max', 'N'])
    writer.writerows(rows)
PYEOF
