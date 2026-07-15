#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dissociation_degrees.csv ===
cat > /tmp/gen.py << 'PYEOF'
import csv, math, sys

# Hardcoded equilibrium constants from Table 4
# T(K) -> (KpCO2, Kpw, KpOH)
K_DATA = {
    2000: (1.867e-6, 4.595, 3.986),
    2250: (7.255e-5, 5.430, 2.368),
    2500: (1.431e-3, 6.088, 1.571),
    2750: (1.418e-2, 6.650, 1.123),
    3000: (1.143e-1, 7.090, 1.123),
    3500: (2.385, 7.420, 0.8522),
}

# Fuel parameters
H_C_fuel = 0.155
N_C_fuel = 0.001
M_C = 12.011
M_H2 = 2.01594
M_N2 = 28.016
M_O2 = 32.0
M_Ar = 39.948
N2_O2_air = 3.3103
Ar_O2_air = 0.0552

a_H2 = H_C_fuel * M_C / M_H2
P_On = 1.0 + N2_O2_air * M_O2 / M_N2 + Ar_O2_air * M_O2 / M_Ar
k_NC = (M_C / M_N2) * N_C_fuel

# Helper functions
def compute_n(alpha_k, KpCO2, Kpw, KpOH, p):
    if alpha_k <= 0.0 or alpha_k >= 1.0:
        return None
    beta_k = alpha_k / (1.0 - alpha_k)
    KpCO2_p = KpCO2 / p
    denom_h1 = (a_H2/2.0) * (beta_k**2 - KpCO2_p)
    if abs(denom_h1) < 1e-16:
        return None
    h1 = (KpCO2_p * P_On - beta_k**2) / denom_h1
    denom_h2 = beta_k**2 - KpCO2_p
    if abs(denom_h2) < 1e-16:
        return None
    h2 = (beta_k**2 + KpCO2_p) / denom_h2
    h3 = -alpha_k / a_H2 + h2 + (beta_k**2 + KpCO2_p * k_NC) / ((a_H2/2.0)*denom_h2)
    Kpw_beta = Kpw / beta_k
    common_denom_h4 = 1.0 + h2 * (Kpw_beta + 1.0)
    if abs(common_denom_h4) < 1e-16:
        return None
    h4 = -h1 * (Kpw_beta + 1.0) / common_denom_h4
    h5 = (1.0 - h3 * (Kpw_beta + 1.0)) / common_denom_h4
    h6 = h1 / common_denom_h4
    h7 = (h2 + h3) / common_denom_h4
    h8 = 1.0 + (a_H2/2.0) * (h6 - h4)
    h9 = (a_H2/2.0) * (h7 - h5) + alpha_k/2.0 - a_H2/2.0 - 1.0
    h10 = 8.0 * a_H2 * KpOH * h4 * h5
    h11 = h7*h8 + h6*h9
    h12 = h7*h8 - h6*h9
    h13 = 16.0 * a_H2 * KpOH * h6 * ((Kpw_beta + 1.0)*h6*h9 + h5*h8)
    h14 = 2.0 * (1.0 + a_H2/2.0) * (h6*h8 - 4.0*a_H2*KpOH*h4**2)
    if h14 == 0:
        return None
    disc = h12**2 + h13
    if disc < 0:
        return None
    n_val = (h10 - h11 - math.sqrt(disc)) / h14
    return n_val

def compute_aw_ah(alpha_k, n, KpCO2, Kpw, KpOH, p):
    if alpha_k <= 0.0 or alpha_k >= 1.0:
        return None, None
    beta_k = alpha_k / (1.0 - alpha_k)
    KpCO2_p = KpCO2 / p
    denom_h1 = (a_H2/2.0) * (beta_k**2 - KpCO2_p)
    if abs(denom_h1) < 1e-16:
        return None, None
    h1 = (KpCO2_p * P_On - beta_k**2) / denom_h1
    denom_h2 = beta_k**2 - KpCO2_p
    if abs(denom_h2) < 1e-16:
        return None, None
    h2 = (beta_k**2 + KpCO2_p) / denom_h2
    h3 = -alpha_k / a_H2 + h2 + (beta_k**2 + KpCO2_p * k_NC) / ((a_H2/2.0)*denom_h2)
    Kpw_beta = Kpw / beta_k
    common_denom_h4 = 1.0 + h2 * (Kpw_beta + 1.0)
    if abs(common_denom_h4) < 1e-16:
        return None, None
    h4 = -h1 * (Kpw_beta + 1.0) / common_denom_h4
    h5 = (1.0 - h3 * (Kpw_beta + 1.0)) / common_denom_h4
    h6 = h1 / common_denom_h4
    h7 = (h2 + h3) / common_denom_h4
    # Eq (13)
    aw = n * (1.0 + a_H2/2.0) * h6 + h7
    ah = n * (1.0 + a_H2/2.0) * h4 + h5
    return aw, ah

def solve_alpha_for_n(n_target, KpCO2, Kpw, KpOH, p):
    lo = 1e-12
    hi = 0.9999
    for _ in range(100):
        mid = (lo+hi)/2.0
        n_val = compute_n(mid, KpCO2, Kpw, KpOH, p)
        if n_val is None:
            if mid < 0.5: lo = mid
            else: hi = mid
            continue
        if abs(n_val - n_target) < 1e-10:
            return mid
        if n_val < n_target:
            hi = mid
        else:
            lo = mid
        if hi-lo < 1e-14:
            break
    return (lo+hi)/2.0

# Conditions
T_vals = [2000, 2250, 2500, 2750, 3000, 3500]
p_dict = {
    2000: [0.05, 0.1, 0.5, 1, 5, 10, 20],
    2250: [0.05, 0.1, 0.5, 1, 5, 10, 20, 50],
    2500: [0.05, 0.1, 0.5, 1, 5, 10, 20, 50, 100],
    2750: [0.1, 0.5, 1, 5, 10, 20, 50, 100],
    3000: [0.1, 0.5, 1, 5, 10, 20, 50, 100, 200],
    3500: [0.1, 0.5, 1, 5, 10, 20, 50, 100, 200],
}
n_vals = [1, 1.2, 1.5, 2, 3, 5, 10, float('inf')]

rows = []
for T in T_vals:
    KpCO2, Kpw, KpOH = K_DATA[T]
    for p in p_dict[T]:
        for n in n_vals:
            if n == float('inf'):
                # Eq (14)-(15)
                tmp = math.sqrt((KpCO2/p)*P_On)
                alpha_k = tmp / (1.0 + tmp)
                alpha_w = 0.0
                alpha_h = 1.0
            else:
                alpha_k = solve_alpha_for_n(n, KpCO2, Kpw, KpOH, p)
                alpha_w, alpha_h = compute_aw_ah(alpha_k, n, KpCO2, Kpw, KpOH, p)
                if alpha_w is None:
                    alpha_w = 0.0
                    alpha_h = 1.0  # fallback
            rows.append([T, p, 'inf' if n == float('inf') else n, alpha_k, alpha_w, alpha_h])

with open('/app/outputs/dissociation_degrees.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T_K', 'p_kgcm2', 'n', 'alpha_k', 'alpha_w', 'alpha_h'])
    writer.writerows(rows)
PYEOF
python3 /tmp/gen.py
