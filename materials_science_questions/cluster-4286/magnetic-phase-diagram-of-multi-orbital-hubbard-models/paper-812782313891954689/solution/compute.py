import csv
import math
import numpy as np
from scipy.optimize import brentq

# Parameters
I = 1.0
Delta = 0.2

# Helper functions for root solving

def mu_sdw_eq(mu, beta):
    if mu <= 0:
        return -1.0  # force positive
    d = math.sqrt(Delta**2 + (0.5 * I * mu)**2)
    lhs = (I / (2 * d)) * math.tanh(0.5 * beta * d)
    return lhs - 1.0

def mu_fm_eq(mu, beta):
    if mu <= 0:
        return -1.0
    term1 = math.tanh(beta * (Delta + 0.5 * I * mu))
    term2 = math.tanh(beta * (Delta - 0.5 * I * mu))
    return mu - 0.5 * (term1 - term2)

def compute_d(mu):
    return math.sqrt(Delta**2 + (0.5 * I * mu)**2)

# Zero-temperature limits
mu_sdw_T0 = math.sqrt(1 - (2*Delta/I)**2)  # ~0.9165
mu_fm_T0 = 1.0
E_sdw_T0 = -Delta**2 / I  # -0.04
E_fm_T0 = 0.0
E_p_T0 = -Delta + 0.25*I  # 0.05

# Nel temperature from lambda=1: solves tanh(beta*Delta/2)=2*Delta/I
arg = 2*Delta/I  # 0.4
beta_N1 = 2.0 * math.atanh(arg) / Delta  # arctanh(0.4) / 0.1 ≈ 4.2365
TN = 1.0 / beta_N1
print(f"Nel temperature TN = {TN:.6f}")

# Curie temperature for FM (lambda=0): solve beta = 4 cosh^2(beta*Delta/2)
def fm_critical_eq(beta):
    return beta - 4.0 * (math.cosh(0.5 * beta * Delta))**2
# Lower bound: beta small, upper bound: large. beta0(0) ~ 4? Let's bracket.
beta_C = brentq(fm_critical_eq, 1e-6, 20.0)
TC = 1.0 / beta_C
print(f"Curie temperature TC = {TC:.6f}")

T_max = 1.5 * max(TN, TC)  # ensure at least 1.5*TN
print(f"T_max = {T_max:.6f}")

# Define temperature grid: from 0 to T_max with many points, plus explicit T=0
N = 500
T_grid = np.linspace(T_max/N, T_max, N)   # skip exactly 0 for now
T_grid = np.insert(T_grid, 0, 0.0)       # add T=0

# Initialize arrays
E_P = np.empty_like(T_grid)
E_F = np.empty_like(T_grid)
E_SDW = np.empty_like(T_grid)
mu_F = np.empty_like(T_grid)
mu_SDW = np.empty_like(T_grid)
S_P = np.empty_like(T_grid)
S_SDW = np.empty_like(T_grid)

for i, T in enumerate(T_grid):
    if T == 0.0:
        beta = 1e12  # effectively infinite, use limits
        E_P[i] = E_p_T0
        E_F[i] = E_fm_T0
        E_SDW[i] = E_sdw_T0
        mu_F[i] = mu_fm_T0
        mu_SDW[i] = mu_sdw_T0
        # Entropy at T=0 is zero for all ordered states, paramagnetic also zero (n=1, gapped? P entropy zero at T=0 because Delta>0)
        S_P[i] = 0.0
        S_SDW[i] = 0.0
        continue

    beta = 1.0 / T

    # Paramagnetic energy and entropy
    E_P[i] = -Delta * math.tanh(0.5 * beta * Delta) + 0.25 * I
    S_P[i] = 2.0 * math.log(2.0) - Delta * beta * math.tanh(0.5 * beta * Delta) + 2.0 * math.log(math.cosh(0.5 * beta * Delta))

    # SDW (lambda=1)
    if beta >= beta_N1:  # T <= TN, mu > 0
        # solve for mu
        mu_max = mu_sdw_T0
        try:
            mu_sol = brentq(mu_sdw_eq, 1e-12, mu_max, args=(beta,))
        except ValueError:
            # fallback if no root (should not happen)
            mu_sol = 0.0
        mu_SDW[i] = mu_sol
        if mu_sol <= 0:
            E_SDW[i] = E_P[i]  # revert to paramagnetic?
            S_SDW[i] = S_P[i]
        else:
            d = compute_d(mu_sol)
            # Energy from eq (24) with lambda=1
            E_SDW[i] = -Delta**2 / d * math.tanh(0.5 * beta * d) + 0.25 * I * (1.0 - mu_sol**2)
            # Entropy for SDW from eq (29) (first case)
            term = 2.0 * d / I
            if term < 1.0:
                S_SDW[i] = 2.0 * math.log(2.0) - (1.0 + term) * math.log(1.0 + term) - (1.0 - term) * math.log(1.0 - term)
            else:
                # term>=1: the formula would involve log(negative), should not happen for d<I/2? d<=sqrt(Delta^2+(I/2)^2) = sqrt(0.04+0.25)=sqrt(0.29)=0.5385, so term max 1.077, but mu ensures d < I/2? Actually for mu>0, d < sqrt(0.04+0.25)=0.5385, term < 1.077, may still be >1 for very small mu? But for valid SDW, mu is large enough that d <= sqrt(Delta^2+(I mu/2)^2) < sqrt(0.04+0.25)=0.5385, term<1.077. We'll cap at 0.9999.
                term = min(term, 0.9999)
                S_SDW[i] = 2.0 * math.log(2.0) - (1.0 + term) * math.log(1.0 + term) - (1.0 - term) * math.log(1.0 - term)
    else:
        mu_SDW[i] = 0.0
        E_SDW[i] = E_P[i]
        S_SDW[i] = S_P[i]

    # FM (lambda=0)
    if beta >= beta_C:  # T <= TC, mu > 0
        try:
            mu_sol = brentq(mu_fm_eq, 1e-12, 1.0, args=(beta,))
        except ValueError:
            mu_sol = 0.0
        mu_F[i] = mu_sol
        if mu_sol <= 0:
            E_F[i] = E_P[i]
        else:
            # Energy for FM from equation after (30): E_F = -Delta * mu * sinh(beta*Delta) / sinh(beta*I*mu/2) + I/4 (1 - mu^2)
            term_num = math.sinh(beta * Delta)
            term_den = math.sinh(0.5 * beta * I * mu_sol)
            if term_den == 0:
                E_F[i] = 0.25 * I * (1.0 - mu_sol**2)  # limit? fallback
            else:
                E_F[i] = -Delta * mu_sol * term_num / term_den + 0.25 * I * (1.0 - mu_sol**2)
    else:
        mu_F[i] = 0.0
        E_F[i] = E_P[i]

# Compute specific heats via numerical derivative of energies w.r.t. T
# Use numpy gradient with temperature spacing
# Handle T=0 carefully: we have grid with T[0]=0, T[1]=very small
C_P = np.gradient(E_P, T_grid)
C_F = np.gradient(E_F, T_grid)
C_SDW = np.gradient(E_SDW, T_grid)

# Write CSV
output_path = "/app/outputs/thermodynamic_data.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T", "E_P", "E_F", "E_SDW", "mu_F", "mu_SDW", "C_P", "C_F", "C_SDW", "S_P", "S_SDW"])
    for i in range(len(T_grid)):
        writer.writerow([
            T_grid[i],
            E_P[i],
            E_F[i],
            E_SDW[i],
            mu_F[i],
            mu_SDW[i],
            C_P[i],
            C_F[i],
            C_SDW[i],
            S_P[i],
            S_SDW[i]
        ])

print("CSV written to", output_path)
