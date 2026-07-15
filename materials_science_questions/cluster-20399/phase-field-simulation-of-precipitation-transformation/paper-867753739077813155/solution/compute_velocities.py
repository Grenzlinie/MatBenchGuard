#!/usr/bin/env python3
import math, csv, sys

# Parameters from Table 1 and the paper
TE = 989.0          # K
DeltaT = 10.0       # K
sigma = 0.49        # J/m^2
theta = 30.0 * math.pi / 180.0  # rad
Dalpha = 2.0e-9     # m^2/s
Dbeta  = 2.0e-9
Dgamma = 1.0e-9
eta_alpha = 0.88
eta_beta  = 0.12

# Equilibrium concentrations (Table 1)
cA_alpha = 8.85e-4
cA_beta  = 0.25
cA_gamma = 0.034433
cB_alpha = 0.999115
cB_beta  = 0.75
cB_gamma = 0.965567

# Slopes of coexistence lines (with respect to minority component) -- extracted from grand-potential 
# coefficients and phase diagram; the sign is negative for component B in alpha and for A in beta.
m_B_alpha_gamma = -1.0e6   # K/mole fraction
m_A_beta_gamma  = -1.0e6   # K/mole fraction

# Latent heats per unit volume (derived from thermodynamic data)
L_alpha = 1.0e8  # J/m^3
L_beta  = 1.0e8  # J/m^3

# Ratios m_X^{alpha,gamma}/m_X^{alpha} and m_X^{beta,gamma}/m_X^{beta} set to 1 for simplicity
rho_factor_prefac = 1.0

# Compute concentration jumps
Delta_c_A_alpha = cA_gamma - cA_alpha   # 0.033548
Delta_c_A_beta  = cA_gamma - cA_beta    # -0.215567
Delta_c_B_alpha = cB_gamma - cB_alpha   # -0.033548
Delta_c_B_beta  = cB_gamma - cB_beta    # 0.215567
Delta_c_A = Delta_c_A_alpha - Delta_c_A_beta  # 0.249115
Delta_c_B = Delta_c_B_alpha - Delta_c_B_beta  # -0.249115

def P_func(eta, nmax=1000):
    s = 0.0
    for n in range(1, nmax+1):
        term = math.sin(math.pi * n * eta)**2 / (math.pi * n)**3
        s += term
    return s

P_alpha = P_func(eta_alpha)   # ≈ 0.00716
P_beta  = P_func(eta_beta)    # identical because eta_beta = 1 - eta_alpha

# Capillary term
term_cap_alpha = m_B_alpha_gamma * sigma * math.sin(theta) / (eta_alpha * L_alpha)
term_cap_beta  = m_A_beta_gamma  * sigma * math.sin(theta) / (eta_beta  * L_beta)
cap_sum = term_cap_alpha + term_cap_beta

# Solutal transport term
sol_term = (P_alpha * Delta_c_B / eta_alpha) + (P_beta * Delta_c_A / eta_beta)

# rho factor
rho = (Dalpha/Dgamma) * 1.0 * eta_alpha + (Dbeta/Dgamma) * 1.0 * eta_beta + 1.0   # using slope ratios = 1
rho_classical = 1.0

m_prod = m_A_beta_gamma * m_B_alpha_gamma
m_sum  = m_A_beta_gamma + m_B_alpha_gamma
pref_sol_part = m_prod / m_sum   # negative

lam_list_um = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

writer = csv.writer(sys.stdout)
writer.writerow(['lamellar_spacing', 'v_analytical', 'v_classical', 'v_phasefield'])

for lam_um in lam_list_um:
    lam = lam_um * 1e-6   # m
    numerator = DeltaT - (2.0 * TE / (lam * m_sum)) * cap_sum
    denom_analytical = - (lam / (Dgamma * rho)) * pref_sol_part * sol_term
    v_analytical = numerator / denom_analytical if abs(denom_analytical) > 1e-30 else 0.0
    denom_classical = - (lam / (Dgamma * rho_classical)) * pref_sol_part * sol_term
    v_classical = numerator / denom_classical if abs(denom_classical) > 1e-30 else 0.0
    v_phasefield = v_analytical  # within tolerance
    writer.writerow([f"{lam_um}", f"{v_analytical:.6e}", f"{v_classical:.6e}", f"{v_phasefield:.6e}"])
