import csv
import numpy as np
from scipy.optimize import minimize

# physical constants
k_B = 1.0  # working in energy units of k_B T
eV_to_K = 11604.518
# pair interaction between 3-fold sites (J) in eV
J_eV = 0.035
J = J_eV * eV_to_K        # ~406.158 K
V = 1.22
J_AC = V * J
J_BC = J_AC

# grid
thetas = np.arange(0.10, 0.76, 0.05)
Ts = np.arange(50, 301, 10)

def free_energy(x, T):
    # x: list of 8 probabilities for states (i,j,k) i,j,k in {0,1}
    x = np.maximum(x, 1e-12)  # avoid log(0)
    # entropy per triangle (dimensionless, negative)
    S = -np.sum(x * np.log(x))
    # energy per triangle (in K)
    # pairs: (1,1,0) -> J, (1,0,1) -> J_AC, (0,1,1) -> J_BC, (1,1,1) -> J+J_AC+J_BC
    E = (x[4] * J) + (x[5] * J_AC) + (x[6] * J_BC) + (x[7] * (J + J_AC + J_BC))
    return E + T * S  # F = U - T*S

def coverage_constr(x, theta):
    PA = x[1] + x[4] + x[5] + x[7]
    PB = x[2] + x[4] + x[6] + x[7]
    PC = x[3] + x[5] + x[6] + x[7]
    return PA + PB + PC - 3 * theta

def solve_for_theta_T(theta, T):
    # initial guess: uniform
    x0 = np.random.random(8)
    x0 /= np.sum(x0)
    bounds = [(0, 1)] * 8
    constr_sum = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    constr_cov = {'type': 'eq', 'fun': lambda x: coverage_constr(x, theta)}
    res = minimize(free_energy, x0, args=(T,), method='SLSQP', bounds=bounds,
                   constraints=[constr_sum, constr_cov],
                   options={'ftol': 1e-12, 'maxiter': 1000})
    best_x = res.x
    best_f = res.fun
    # a few restarts to avoid local minima
    for _ in range(5):
        x0 = np.random.random(8)
        x0 /= np.sum(x0)
        res2 = minimize(free_energy, x0, args=(T,), method='SLSQP', bounds=bounds,
                        constraints=[constr_sum, constr_cov],
                        options={'ftol': 1e-12, 'maxiter': 1000})
        if res2.fun < best_f:
            best_f = res2.fun
            best_x = res2.x
    x = np.maximum(best_x, 0)
    x /= np.sum(x)  # re-normalise
    PA = x[1] + x[4] + x[5] + x[7]
    PB = x[2] + x[4] + x[6] + x[7]
    PC = x[3] + x[5] + x[6] + x[7]
    I = (abs(PA - PB) / 2.0 - PC) ** 2
    return PA, PB, PC, I

rows = []
for theta in thetas:
    for T in Ts:
        PA, PB, PC, I = solve_for_theta_T(theta, T)
        rows.append([theta, T, PA, PB, PC, I])

with open('/app/outputs/occupation_and_intensity.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['theta', 'T', 'PA', 'PB', 'PC', 'I'])
    writer.writerows(rows)
