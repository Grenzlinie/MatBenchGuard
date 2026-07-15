import csv
import math
import numpy as np
from scipy.optimize import fsolve

# Known rows from Table 3: (P_bar, T_K, ratio_str, F2_pct, F_pct, Xe_pct, XeF2_pct, XeF4_pct, XeF6_pct)
known = [
    (1, 500, '1:1', 0.01, 0, 7.4, 85.2, 7.4, 0),
    (1, 500, '1:2', 3.4, 0, 0, 5.1, 89.9, 1.7),
    (1, 500, '1:3', 41.8, 0, 0, 0.01, 41.6, 16.5),

    (1, 600, '1:1', 0.65, 0, 8.8, 82.4, 8.2, 0),
    (1, 600, '1:2', 20.9, 0.01, 0.08, 21.3, 57.1, 0.5),
    (1, 600, '1:3', 51.9, 0.01, 0.01, 5.0, 4.19, 1.2),

    (1, 700, '1:1', 7.5, 0.05, 13.2, 73.7, 5.6, 0),
    (1, 700, '1:2', 41.6, 0.12, 1.2, 39.3, 17.7, 0.06),
    (1, 700, '1:3', 61.2, 0.14, 0.40, 21.8, 16.4, 0.10),

    (1, 800, '1:1', 22.4, 0.49, 24.4, 50.9, 1.8, 0),
    (1, 800, '1:2', 57.5, 0.71, 7.2, 37.4, 3.2, 0),
    (1, 800, '1:3', 66.2, 0.77, 3.6, 26.2, 3.2, 0.01),

    (100, 500, '1:1', 0, 0, 7.4, 85.2, 7.4, 0),
    (100, 500, '1:2', 0.06, 0, 0, 3.1, 93.9, 3.0),

    (100, 600, '1:1', 0.01, 0, 8.5, 83.0, 8.5, 0),
    (100, 600, '1:2', 1.4, 0, 0, 5.9, 88.2, 4.5),

    (100, 700, '1:1', 0.12, 0.01, 9.5, 81.0, 9.4, 0.01),
    (100, 700, '1:2', 8.6, 0.01, 0.03, 12.2, 75.4, 3.7),
    (100, 700, '1:3', 42.5, 0.01, 0, 0.85, 40.8, 15.8),

    (100, 800, '1:1', 1.0, 0.01, 10.7, 78.6, 9.7, 0.02),
    (100, 800, '1:2', 21.7, 0.01, 0.17, 23.3, 53.0, 1.9),
    (100, 800, '1:3', 50.8, 0.08, 0.01, 5.8, 39.2, 4.1),
]

# Missing rows
missing = [
    (100, 500, '1:3'),
    (100, 600, '1:3'),
]

P0 = 1.0  # bar, standard state

# ---------- dimensionless K_eq from a row ----------
def compute_K_eq(P_bar, x_Xe, x_F2, x_F, x_XeF2, x_XeF4, x_XeF6):
    # return dict of K_eq values (dimensionless), skip if denominator zero
    K = {}
    if x_Xe > 1e-30 and x_F2 > 1e-30:
        K['K1'] = (x_XeF2 / (x_Xe * x_F2)) * (P0 / P_bar)
        K['K2'] = (x_XeF4 / (x_Xe * x_F2**2)) * (P0 / P_bar)**2
        K['K3'] = (x_XeF6 / (x_Xe * x_F2**3)) * (P0 / P_bar)**3
    if x_F2 > 1e-30:
        K['K4'] = (x_F**2 / x_F2) * (P_bar / P0)
    return K

# Collect all K_eq values per temperature
from collections import defaultdict
T_K_values = defaultdict(lambda: {'K1':[], 'K2':[], 'K3':[], 'K4':[]})
for row in known:
    P_bar, T, _, f2, f, xe, xef2, xef4, xef6 = row
    x = np.array([f2, f, xe, xef2, xef4, xef6]) / 100.0
    K = compute_K_eq(P_bar, x[2], x[0], x[1], x[3], x[4], x[5])
    for k, v in K.items():
        T_K_values[T][k].append(v)

# Compute mean ln(K) for each T, store
lnK_mean = {}
for T, Kdict in T_K_values.items():
    lnK_mean[T] = {}
    for k, vals in Kdict.items():
        if vals:
            log_vals = [math.log(v) for v in vals]
            mean_log = sum(log_vals) / len(log_vals)
            lnK_mean[T][k] = mean_log

# Fit lnK = A + B/T for each reaction
inv_T_list = sorted([T for T in lnK_mean.keys()])
inv_T_arr = np.array([1.0/T for T in inv_T_list])

fits = {}
for reaction in ['K1', 'K2', 'K3', 'K4']:
    vals = np.array([lnK_mean[T][reaction] for T in inv_T_list])
    coeffs = np.polyfit(inv_T_arr, vals, 1)  # linear in 1/T
    fits[reaction] = coeffs

def get_lnK_at_T(reaction, T):
    A, B = fits[reaction]
    return A + B / T

# ---------- solving missing rows ----------
def solve_condition(P_bar, T, r):  # r = F2 initial moles per Xe mole
    lnK1 = get_lnK_at_T('K1', T)
    lnK2 = get_lnK_at_T('K2', T)
    lnK3 = get_lnK_at_T('K3', T)
    lnK4 = get_lnK_at_T('K4', T)
    K1 = math.exp(lnK1)
    K2 = math.exp(lnK2)
    K3 = math.exp(lnK3)
    K4 = math.exp(lnK4)

    def func(vars):
        n_Xe, n_F2, n_F, n_XeF2, n_XeF4, n_XeF6 = vars
        # Ensure non-negative (use exp?). Use clipping in residuals. But we use unconstrained variables, ok.
        n_tot = n_Xe + n_F2 + n_F + n_XeF2 + n_XeF4 + n_XeF6
        eq1 = K1 * (P_bar / P0) - (n_XeF2 * n_tot) / (n_Xe * n_F2) if n_Xe>1e-10 and n_F2>1e-10 else 1.0
        eq2 = K2 * (P_bar / P0)**2 - (n_XeF4 * n_tot**2) / (n_Xe * n_F2**2) if n_Xe>1e-10 and n_F2>1e-10 else 1.0
        eq3 = K3 * (P_bar / P0)**3 - (n_XeF6 * n_tot**3) / (n_Xe * n_F2**3) if n_Xe>1e-10 and n_F2>1e-10 else 1.0
        eq4 = K4 * (P0 / P_bar) - (n_F**2) / (n_F2 * n_tot) if n_F2>1e-10 else 1.0
        # Atom balances
        eq5 = n_Xe + n_XeF2 + n_XeF4 + n_XeF6 - 1.0
        eq6 = 2*n_F2 + n_F + 2*n_XeF2 + 4*n_XeF4 + 6*n_XeF6 - 2*r
        return [eq1, eq2, eq3, eq4, eq5, eq6]

    # initial guess based on ratio
    n_Xe_guess = 0.1
    n_F2_guess = max(0.01, r - 1.0)
    n_F_guess = 0.001
    n_XeF2_guess = 0.5
    n_XeF4_guess = 0.5
    n_XeF6_guess = 0.1
    sol = fsolve(func, [n_Xe_guess, n_F2_guess, n_F_guess, n_XeF2_guess, n_XeF4_guess, n_XeF6_guess], maxfev=2000)
    n_Xe, n_F2, n_F, n_XeF2, n_XeF4, n_XeF6 = sol
    n_tot = n_Xe + n_F2 + n_F + n_XeF2 + n_XeF4 + n_XeF6
    pct = {
        'F2': n_F2 / n_tot * 100,
        'F': n_F / n_tot * 100,
        'Xe': n_Xe / n_tot * 100,
        'XeF2': n_XeF2 / n_tot * 100,
        'XeF4': n_XeF4 / n_tot * 100,
        'XeF6': n_XeF6 / n_tot * 100,
    }
    return pct

# Solve missing rows
missing_solution = []
for P, T, ratio in missing:
    r_map = {'1:1':1, '1:2':2, '1:3':3}
    r = r_map[ratio]
    pct = solve_condition(P, T, r)
    missing_solution.append((P, T, ratio, pct))

# Write CSV
with open('/app/outputs/xe_f2_equilibrium_composition.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['total_pressure_bar', 'temperature_K', 'initial_ratio_Xe_F2', 'F2', 'F', 'Xe', 'XeF2', 'XeF4', 'XeF6'])
    # write all known rows
    for row in known:
        P, T, ratio, f2, f, xe, xef2, xef4, xef6 = row
        writer.writerow([P, T, ratio, f2, f, xe, xef2, xef4, xef6])
    # write missing rows
    for P, T, ratio, pct in missing_solution:
        writer.writerow([P, T, ratio, round(pct['F2'], 2), round(pct['F'], 2), round(pct['Xe'], 2), round(pct['XeF2'], 2), round(pct['XeF4'], 2), round(pct['XeF6'], 2)])
