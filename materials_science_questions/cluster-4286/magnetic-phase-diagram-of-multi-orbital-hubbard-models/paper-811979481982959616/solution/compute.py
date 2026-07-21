#!/usr/bin/env python3
"""Solve two-band Hartree-Fock equations for all required (U,J) points
and write occupation_numbers.npz and self_consistent_results.csv."""
import numpy as np
from scipy.optimize import fsolve
import csv
import os

A1, A2, n = 1.00, 1.01, 2.0

# Helper: safe power 1.5
def safe_pow1_5(x):
    x = np.maximum(x, 0.0)  # clamp negative arguments
    return x ** 1.5

# Self-consistency equations for magnetized solution (variables: n1p, n1m, n2p, n2m, v)
def equations_mag(vars, U, J):
    n1p, n1m, n2p, n2m, v = vars
    eq1 = n1p - A1 * safe_pow1_5(v + U * n1p + 2 * J * (n2p - n2m))
    eq2 = n1m - A1 * safe_pow1_5(v + U * n1m + 2 * J * (n2m - n2p))
    eq3 = n2p - A2 * safe_pow1_5(v + U * n2p + 2 * J * (n1p - n1m))
    eq4 = n2m - A2 * safe_pow1_5(v + U * n2m + 2 * J * (n1m - n1p))
    eq5 = (n1p + n1m + n2p + n2m) - n
    return [eq1, eq2, eq3, eq4, eq5]

# Self-consistency equations for paramagnetic solution (variables: n1, n2, v)
def equations_para(vars, U):
    n1o, n2o, v = vars
    eq1 = n1o - A1 * safe_pow1_5(v + U * n1o)
    eq2 = n2o - A2 * safe_pow1_5(v + U * n2o)
    eq3 = 2 * n1o + 2 * n2o - n   # n1p=n1m=n1o, n2p=n2m=n2o, total 2*n1o+2*n2o = n
    return [eq1, eq2, eq3]

# Energy per site
def energy(n1p, n1m, n2p, n2m, v, U, J):
    n2 = n * n
    term1 = 0.5 * U * n2
    term2 = 0.6 * v * n   # 3/5 = 0.6
    term3 = 0.1 * U * (n1p**2 + n1m**2 + n2p**2 + n2m**2)  # U/10 = 0.1*U
    term4 = 0.4 * J * (n1p - n1m) * (n2p - n2m)  # 2J/5 = 0.4*J
    return term1 + term2 + term3 + term4

# Compute one (U,J) point
def solve_one(U, J):
    # -- paramagnetic --
    para_guess = [0.5, 0.5, -0.5]  # n1o, n2o, v initial
    sol_para, infodict, ier, msg = fsolve(equations_para, para_guess, args=(U,), full_output=True, xtol=1e-12, maxfev=1000)
    if ier != 1:
        print(f"Warning: paramagnetic solver did not converge for U={U}, J={J}")
        return None
    n1o, n2o, v_para = sol_para
    n1p_para = n1m_para = n1o
    n2p_para = n2m_para = n2o
    u_para = energy(n1p_para, n1m_para, n2p_para, n2m_para, v_para, U, J)
    # -- magnetized --
    # initial guess: slightly magnetized
    mag_guess = [0.8, 0.2, 0.8, 0.2, 0.1]
    sol_mag, infodict_m, ier_m, msg_m = fsolve(equations_mag, mag_guess, args=(U,J), full_output=True, xtol=1e-12, maxfev=2000)
    if ier_m != 1:
        # maybe no magnetized solution; treat as same as paramagnetic
        n1p_mag, n1m_mag, n2p_mag, n2m_mag = n1o, n1o, n2o, n2o
        v_mag = v_para
        u_mag = u_para
    else:
        n1p_mag, n1m_mag, n2p_mag, n2m_mag, v_mag = sol_mag
        u_mag = energy(n1p_mag, n1m_mag, n2p_mag, n2m_mag, v_mag, U, J)

    M = n1p_mag - n1m_mag + n2p_mag - n2m_mag
    M_over_2muB = M / 2.0
    return {
        'U': U, 'J': J,
        'M_over_2muB': M_over_2muB,
        'u_magnetized': u_mag,
        'u_unmagnetized': u_para,
        'occ': (n1p_mag, n1m_mag, n2p_mag, n2m_mag, v_mag)
    }

# Sweep definitions
sweeps = []
# Sweep 1: J=0.1, U from 0.2 to 0.8 step 0.1
for uval in np.arange(0.2, 0.81, 0.1):
    sweeps.append((round(uval,2), 0.1))
# Sweep 2: U=0.3, J from 0.0 to 0.5 step 0.1
for jval in np.arange(0.0, 0.51, 0.1):
    sweeps.append((0.3, round(jval,2)))

results = []
occ_dict = {}
for U, J in sweeps:
    res = solve_one(U, J)
    if res is None:
        print(f"Skipping U={U}, J={J}")
        continue
    results.append(res)
    key = f"U_{U:.2f}_J_{J:.2f}"
    occ_dict[key] = np.array(res['occ'])

# Write occupation numbers npz file
os.makedirs("/app/outputs", exist_ok=True)
np.savez("/app/outputs/occupation_numbers.npz", **occ_dict)
print("Saved occupation_numbers.npz")

# Write CSV
csv_path = "/app/outputs/self_consistent_results.csv"
with open(csv_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["U", "J", "M_over_2muB", "u_magnetized", "u_unmagnetized"])
    for r in results:
        writer.writerow([
            f"{r['U']:.2f}",
            f"{r['J']:.2f}",
            f"{r['M_over_2muB']:.8f}",
            f"{r['u_magnetized']:.8f}",
            f"{r['u_unmagnetized']:.8f}"
        ])
print("Saved self_consistent_results.csv")
