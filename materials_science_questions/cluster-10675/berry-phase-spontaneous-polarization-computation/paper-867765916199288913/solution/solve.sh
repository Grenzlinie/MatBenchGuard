#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy
mkdir -p /app/outputs

# === solve block: polarization_tetragonality.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import minimize

# Physical constants
eV_J = 1.602176634e-19
a_inplane = 3.846e-10          # in-plane lattice constant (m)
A_cell = a_inplane**2         # area per unit cell (m^2)
epsilon0 = 8.8541878128e-12

# Bulk out-of-plane lattice parameters (constrained)
c_p0 = 4.009e-10   # m  (PbTiO3 bulk under a=3.846 A)
c_s0 = 3.846e-10   # m  (SrTiO3 cubic)

# Landau coefficients for U(P) = B P^2 + C P^4  (eV per cell)
B_p = -0.17175279
C_p =  0.16068441
B_s =  0.21046331
C_s =  0.30913420

# Tetragonality expansion c/a = alpha + beta P^2 + gamma P^4
# PbTiO3
alpha_p = 1.01566146
beta_p  = 0.03609915
gamma_p = 0.02209009
# SrTiO3
alpha_s = 1.0
beta_s  = 0.06076952
gamma_s = 0.04820368

def U_p(P):
    return B_p * P**2 + C_p * P**4

def U_s(P):
    return B_s * P**2 + C_s * P**4

def E_elec(P_p, P_s, l_p, l_s):
    return (l_p * l_s / (epsilon0 * (l_p + l_s))) * (P_s - P_p)**2

def total_energy(P_vec, n_p, n_s):
    P_p, P_s = P_vec
    l_p = n_p * c_p0
    l_s = n_s * c_s0
    E_bulk = (n_p * U_p(P_p) + n_s * U_s(P_s)) * eV_J / A_cell   # J/m^2
    E_el = E_elec(P_p, P_s, l_p, l_s)
    return E_bulk + E_el

def c_over_a(P, alpha, beta, gamma):
    return alpha + beta * P**2 + gamma * P**4

# Run for n_s = 3, n_p = 1..7
n_s = 3
results = []
for n_p in range(1, 8):
    # initial guess: PbTiO3 polarized near its bulk value, SrTiO3 near zero
    x0 = np.array([0.7, 0.0])
    res = minimize(lambda x: total_energy(x, n_p, n_s),
                   x0, method='L-BFGS-B',
                   bounds=[(0.0, 5.0), (0.0, 5.0)])
    P_p_opt, P_s_opt = res.x
    # Tetragonality
    tetra_p = c_over_a(P_p_opt, alpha_p, beta_p, gamma_p)
    tetra_s = c_over_a(P_s_opt, alpha_s, beta_s, gamma_s)
    results.append((n_p, P_p_opt, P_s_opt, tetra_p, tetra_s))

# Write CSV
header = "n_p,P_p0,P_s0,tetragonality_Pb,tetragonality_Sr"
with open('/app/outputs/polarization_tetragonality.csv', 'w') as f:
    f.write(header + '\n')
    for row in results:
        f.write(f"{row[0]},{row[1]:.8f},{row[2]:.8f},{row[3]:.8f},{row[4]:.8f}\n")
PYEOF
