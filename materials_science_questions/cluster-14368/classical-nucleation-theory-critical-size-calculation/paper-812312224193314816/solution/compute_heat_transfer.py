#!/usr/bin/env python3
import math

T = 373.15          # K
P = 101325.0        # Pa
R = 461.5           # J/(kg·K) for steam
s = 2.256e6         # J/kg latent heat
f = 0.045           # condensation coefficient
K_param = 5.0e-6    # m·h/kcal
H = 0.019           # m
f_one_minus_phi = 0.016   # from paper

# phase-transition alpha_p in W/(m²·K)
alpha_p = f * s**2 * P / (math.sqrt(2*math.pi) * (R * T)**1.5 * T)

# (1 - phi) factor
one_minus_phi = f_one_minus_phi / f

# undercooling threshold (K)
Delta_T_nucl = 3.0

# conversion factor K_param term: need alpha_p in kcal/(m²·h·°C) for the bracket
W_to_kcal = 0.859845       # 1 W/(m²·K) = 0.859845 kcal/(m²·h·°C)
alpha_p_kcal = alpha_p * W_to_kcal

print("Delta_T_K,alpha_m_W_m2K")
for i in range(1, 21):
    dT = i * 0.5
    if dT < Delta_T_nucl:
        alpha_m_W = 0.0
    else:
        # alpha_m in kcal / (m²·h·°C)
        alpha_m_kcal = alpha_p_kcal * one_minus_phi * (1.0 - K_param * H * alpha_p_kcal * dT)
        if alpha_m_kcal < 0:
            alpha_m_kcal = 0.0
        # convert to W/(m²·K)
        alpha_m_W = alpha_m_kcal / W_to_kcal
    print(f"{dT},{alpha_m_W:.6f}")
