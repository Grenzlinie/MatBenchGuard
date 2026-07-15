import numpy as np
import math
import csv
import json
import sys

# Constants
R = 8.314          # J/mol K
Z1 = 8
Z2 = 6

# Chemical interchange energies in K
W_CuZn_1 = 955
W_CuZn_2 = 535
W_CuAl_1 = 1345
W_CuAl_2 = 825
W_ZnAl_1 = -50
W_ZnAl_2 = 200
W_CuZn_alpha = 582
W_CuAl_alpha = 1459   # from W_CuAl_M
W_ZnAl_alpha = 0

# Interaction energies in J/mol (converted from kJ/mol)
E_CuZn_alpha = -29047.0
E_CuZn_beta  = -43014.0
E_CuAl_alpha = -72781.0
E_CuAl_beta  = -65306.0
E_ZnAl_alpha = 0.0
E_ZnAl_beta  = -3326.0

# Short-range-order correction factors
x_CuZn = 0.67
x_CuAl = 0.78

def delta_G_Cu1(T):
    return 7232.40 + 3.14348 * T

def delta_G_Cu2(T):
    return -1221.81 + 0.11418 * T + 8.837e-5 * T * T

def delta_G_Zn(T):
    return -325.08 - 0.79713 * T - 8.1704e-4 * T * T

def delta_G_Al(T):
    return 8212.38 + 2.75113 * T

def weighted_Cu(X_Zn, X_Al, T):
    denom = X_Zn + X_Al
    if denom == 0:
        return 0.0
    return (X_Zn * delta_G_Cu1(T) + X_Al * delta_G_Cu2(T)) / denom

def eta1_beta(T):
    arg = 1.0 - (T / 770.0)**5
    if arg < 0:
        arg = 0.0
    return 0.32 * math.sqrt(arg)

def eta1_alpha(T):
    arg = 1.0 - (T / 770.0)**5
    if arg < 0:
        arg = 0.0
    return 0.20 * math.sqrt(arg)

def delta_U_beta_ordering(comp, eta):
    """Internal energy for β → β' (eq. 2). comp: dict with Cu, Zn, Al."""
    X_Zn = comp['Zn']
    X_Al = comp['Al']
    denom = X_Zn + X_Al
    if denom == 0:
        return 0.0
    # contributions
    A = (X_Zn/denom) * (Z2*W_CuZn_2 - Z1*W_CuZn_1) + \
        (X_Al/denom) * (Z2*W_CuAl_2 - Z1*W_CuAl_1) - \
        (X_Zn * X_Al / (denom**2)) * (Z2*W_ZnAl_2 - Z1*W_ZnAl_1)
    return 0.5 * R * eta * eta * A

def delta_U_alpha_ordering(comp, eta):
    """Internal energy for α → α' (eq. 3)."""
    X_Zn = comp['Zn']
    X_Al = comp['Al']
    denom = X_Zn + X_Al
    if denom == 0:
        return 0.0
    term = - (X_Zn/denom) * W_CuZn_alpha - (X_Al/denom) * W_CuAl_alpha + \
           (X_Zn * X_Al / (denom**2)) * W_ZnAl_alpha
    return 2.0 * R * eta * eta * term

def delta_G_beta_to_alpha(comp, T):
    """Regular-solution ΔG^(β→α) (eq. 4)."""
    X_Cu = comp['Cu']
    X_Zn = comp['Zn']
    X_Al = comp['Al']
    dG_Cu = weighted_Cu(X_Zn, X_Al, T)
    dG = X_Cu * dG_Cu + X_Zn * delta_G_Zn(T) + X_Al * delta_G_Al(T)
    dG += (E_CuZn_alpha - E_CuZn_beta) * X_Cu * X_Zn
    dG += (E_CuAl_alpha - E_CuAl_beta) * X_Cu * X_Al
    dG += (E_ZnAl_alpha - E_ZnAl_beta) * X_Zn * X_Al
    return dG

def config_entropy_term(comp, eta):
    """The bracket in the entropy part of ordering free energy."""
    X_Cu = comp['Cu']
    if X_Cu <= 0 or X_Cu >= 1:
        return 0.0
    eps = 1e-15
    # safe log
    def safe_log(x):
        return math.log(max(x, eps))
    term = 2.0 * X_Cu * safe_log(X_Cu) + 2.0 * (1.0 - X_Cu) * safe_log(1.0 - X_Cu)
    term -= (eta + X_Cu) * safe_log(eta + X_Cu)
    term -= max(1.0 - X_Cu - eta, eps) * safe_log(max(1.0 - X_Cu - eta, eps))
    term -= (eta + 1.0 - X_Cu) * safe_log(eta + 1.0 - X_Cu)
    term -= max(X_Cu - eta, eps) * safe_log(max(X_Cu - eta, eps))
    return term

def x_factor(comp):
    X_Zn = comp['Zn']
    X_Al = comp['Al']
    denom = X_Zn + X_Al
    if denom == 0:
        return x_CuZn  # fallback
    return (X_Zn * x_CuZn + X_Al * x_CuAl) / denom

def delta_G_ordering(comp, eta, T):
    """Free energy of ordering β→β' (eq. 17), including entropy."""
    dU = delta_U_beta_ordering(comp, eta)
    x_val = x_factor(comp)
    S_term = config_entropy_term(comp, eta)
    dG = dU - (R * T / (2.0 * x_val)) * S_term
    return dG

def delta_G_alpha_to_alpha_prime(comp, eta, T):
    """Free energy of α→α' (eq. 22)."""
    dU = delta_U_alpha_ordering(comp, eta)
    x_val = x_factor(comp)   # using same x factor as β (as per paper assumption)
    S_term = config_entropy_term(comp, eta)
    dG = dU - (R * T / (2.0 * x_val)) * S_term
    return dG

def regular_solution_G(comp, T, phase='beta'):
    """Regular solution free energy (without ordering).
    For β phase: reference G_i^β = 0.
    For α phase: reference G_i^α = ΔG_i^(β→α)."""
    X_Cu, X_Zn, X_Al = comp['Cu'], comp['Zn'], comp['Al']
    # configurational entropy
    eps = 1e-15
    sum_log = X_Cu * math.log(max(X_Cu, eps)) + \
              X_Zn * math.log(max(X_Zn, eps)) + \
              X_Al * math.log(max(X_Al, eps))
    G = R * T * sum_log
    # excess terms
    if phase == 'beta':
        G += E_CuZn_beta * X_Cu * X_Zn + E_CuAl_beta * X_Cu * X_Al + E_ZnAl_beta * X_Zn * X_Al
    else:
        G += X_Cu * weighted_Cu(X_Zn, X_Al, T) + X_Zn * delta_G_Zn(T) + X_Al * delta_G_Al(T)
        G += E_CuZn_alpha * X_Cu * X_Zn + E_CuAl_alpha * X_Cu * X_Al + E_ZnAl_alpha * X_Zn * X_Al
    return G

# ---------- Main computation ----------
Ts = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750]

# Alloy composition (for β'→α' and β→α)
alloy = {'Cu': 0.6933, 'Zn': 0.2667, 'Al': 0.0400}

# Compositions for diffusional reaction
beta_prime_comp = {'Cu': 1 - 0.2477 - 0.0900, 'Zn': 0.2477, 'Al': 0.0900}
beta1_prime_comp = {'Cu': 1 - 0.2480 - 0.0902, 'Zn': 0.2480, 'Al': 0.0902}
alpha_comp_diff = {'Cu': 1 - 0.2218 - 0.0738, 'Zn': 0.2218, 'Al': 0.0738}

results = []
DG_beta_prime_to_alpha_prime = []

for T in Ts:
    # eta values
    eta_b = eta1_beta(T)
    eta_a = eta1_alpha(T)

    # 1. ΔG^(β'→α')
    dU_b = delta_U_beta_ordering(alloy, eta_b)
    dU_a = delta_U_alpha_ordering(alloy, eta_a)
    DG_ba = delta_G_beta_to_alpha(alloy, T)
    DG_shear = -dU_b + DG_ba + dU_a
    DG_beta_prime_to_alpha_prime.append(DG_shear)

    # 2. ΔG^(β→α)
    DG_b_to_a = delta_G_beta_to_alpha(alloy, T)

    # 3. ΔG^(β'→β1'+α)
    # Regular solution free energies
    G_beta_prime_reg = regular_solution_G(beta_prime_comp, T, 'beta')
    G_beta1_prime_reg = regular_solution_G(beta1_prime_comp, T, 'beta')
    G_alpha_reg = regular_solution_G(alpha_comp_diff, T, 'alpha')

    # Add ordering contributions
    dG_ord_bp = delta_G_ordering(beta_prime_comp, eta_b, T)
    dG_ord_b1 = delta_G_ordering(beta1_prime_comp, eta_b, T)

    G_bp_final = G_beta_prime_reg + dG_ord_bp
    G_b1p_final = G_beta1_prime_reg + dG_ord_b1
    G_alpha_final = G_alpha_reg   # no ordering for α in diffusional reaction

    # Lever fraction
    X_Zn_bp = beta_prime_comp['Zn']
    X_Zn_a = alpha_comp_diff['Zn']
    X_Zn_b1 = beta1_prime_comp['Zn']
    L = (X_Zn_bp - X_Zn_a) / (X_Zn_b1 - X_Zn_a)

    DG_diff = G_alpha_final + L * (G_b1p_final - G_alpha_final) - G_bp_final

    # 4. ΔG^(α→α') (ordering of α phase)
    # Use alpha phase composition and eta_alpha
    DG_alpha_order = delta_G_alpha_to_alpha_prime(alpha_comp_diff, eta_a, T)

    results.append([T, DG_shear, DG_b_to_a, DG_diff, DG_alpha_order])

# Write driving_forces.csv
outdir = '/app/outputs'
import os
os.makedirs(outdir, exist_ok=True)
csv_path = os.path.join(outdir, 'driving_forces.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', "DG_beta'_to_alpha'", 'DG_beta_to_alpha',
                     "DG_beta'_to_beta1'_plus_alpha", 'DG_alpha_to_alpha''])
    for row in results:
        writer.writerow(row)

# Fit cubic polynomial for ΔG^(β'→α')
T_arr = np.array(Ts, dtype=float)
DG_arr = np.array(DG_beta_prime_to_alpha_prime, dtype=float)
coeffs = np.polyfit(T_arr, DG_arr, 3)  # highest order first: [a3, a2, a1, a0]
a0, a1, a2, a3 = coeffs[3], coeffs[2], coeffs[1], coeffs[0]

json_path = os.path.join(outdir, 'polynomial_coefficients.json')
with open(json_path, 'w') as f:
    json.dump({'constant': a0, 'T': a1, 'T2': a2, 'T3': a3}, f, indent=2)

print("Outputs written.")
