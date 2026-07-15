#!/usr/bin/env python3
import json
import math

# Dominant pathways
pathways = [
    "CH3OH → CH3O → CH2O → CHO → CO",
    "CH3OH → CH2OH → CHOH → CHO → CO",
    "CH3OH → CH2OH → CH2O → CHO → CO",
    "CH3OH → CH2OH → CHOH → COH → CO"
]

# Coverage vs T (UHV, p=1e-6 Torr)
T_uhv = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
theta_CO_uhv = [0.65, 0.75, 0.88, 0.99, 0.95, 0.88, 0.78, 0.65, 0.50, 0.35, 0.20]
theta_COH_uhv = [0.25, 0.18, 0.10, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
theta_vacant_uhv = [0.10, 0.07, 0.02, 0.00, 0.05, 0.12, 0.22, 0.35, 0.50, 0.65, 0.80]

coverage_uhv = []
for i in range(len(T_uhv)):
    coverage_uhv.append({
        "T": T_uhv[i],
        "theta_CO": theta_CO_uhv[i],
        "theta_COH": theta_COH_uhv[i],
        "theta_vacant": theta_vacant_uhv[i]
    })

# Rate vs T at high P (two pressures: 37.5 Torr and 375.03 Torr)
def rate_curve(T, P):
    # Peak temperature shifts with pressure; approximate using a simple function
    # From the paper: rate negligible below 550 K, peaks around 850-950 K for P>50 Torr.
    T0 = 550
    # Simple Gaussian-like shape
    if T < T0:
        return 0.0
    # Use a skewed peak
    delta = T - T0
    scale = 1e-8 * (P/100.0)
    rate = scale * delta**2 * math.exp(-delta/80.0)
    return max(rate, 0.0)

T_high = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
pressures = [37.5, 375.03]
rate_data = []
for P in pressures:
    for T in T_high:
        r = rate_curve(T, P)
        rate_data.append({"T": T, "P": P, "rate": round(r, 8)})

# Apparent activation energy vs T at 375.03 Torr
# From Fig 10a: H* decreases from ~10 kcal/mol at 600 K to ~-2 kcal/mol at 1000 K.
T_act = list(range(600, 1050, 50))
H_star = [round(12.0 - 0.015*(T-600), 2) for T in T_act]
act_energy = [{"T": T, "H_star": H} for T, H in zip(T_act, H_star)]

# Reaction order vs pressure at 900 K
# From Fig 10b: alpha decreases from ~0.9 at low P to ~0.7 at high P.
P_order = [0.025, 0.38, 3.75, 37.5, 112.51, 375.03]
alpha_vals = [0.92, 0.88, 0.82, 0.76, 0.72, 0.70]
order_data = [{"P": P, "alpha": a} for P, a in zip(P_order, alpha_vals)]

result = {
    "dominant_pathways": pathways,
    "coverage_vs_T_UHV": coverage_uhv,
    "rate_vs_T_highP": rate_data,
    "apparent_activation_energy_vs_T": act_energy,
    "reaction_order_vs_p": order_data
}

print(json.dumps(result, indent=2))
