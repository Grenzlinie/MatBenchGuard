#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: simulation_results.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import csv, os, sys

# Material constants (SI units)
# b derived from h_e = a/2 = 0.176 nm -> a = 0.352 nm -> b = a/√2 ≈ 0.249 nm
b = 0.249e-9          # m
mu = 79e9             # Pa (shear modulus)
nu = 0.3              # Poisson's ratio
tau_f = 300e6         # Friction stress on leading dislocation (Pa)
tau_lat = 30e6        # Lattice friction on other dislocations (Pa)

# Mixed dislocation: assume equal edge and screw components (45° character)
b_e = b / np.sqrt(2)
b_s = b / np.sqrt(2)

def interaction_forces(x, d, n):
    """
    Compute the force per unit length (N/m) on each dislocation in the first
    pile-up (positive side) due to all other dislocations.
    x: positions (m), d: glide-plane separation (m).
    """
    F = np.zeros(n)
    for i in range(n):
        fi = 0.0
        # Interactions with dislocations in the same pile-up
        for j in range(n):
            if i == j:
                continue
            dr = x[i] - x[j]               # signed distance along x
            # edge-edge (repulsive if dr>0, attractive if dr<0)
            fi += (mu * b_e**2) / (2.0 * np.pi * (1.0 - nu)) / dr
            # screw-screw: standard interaction uses 1/(x_i - x_j), not x_i+x_j
            fi += (mu * b_s**2) / (2.0 * np.pi) / dr
        # Interactions with dislocations in the opposite pile-up (at -x[j])
        for j in range(n):
            r = x[i] + x[j]               # distance along x (positive)
            # edge between different pile-ups
            fi += - (mu * b_e**2) / (2.0 * np.pi * (1.0 - nu)) * r * (r**2 - d**2) / (r**2 + d**2)**2
            # screw between different pile-ups
            fi += - (mu * b_s**2) / (2.0 * np.pi) * r / (r**2 - d**2)
        F[i] = fi
    return F

def residual(x, tau_a, d, n):
    """Return the force-balance residual for each dislocation."""
    F = interaction_forces(x, d, n)
    res = np.zeros(n)
    for i in range(n):
        tf = tau_f if i == 0 else tau_lat
        # Equilibrium: tau_a * b + F_i - tf * b = 0
        res[i] = tau_a * b + F[i] - tf * b
    return res

def has_solution(x0, tau_a, d, n):
    """Check if a physically acceptable static equilibrium exists."""
    try:
        sol = fsolve(residual, x0, args=(tau_a, d, n),
                     maxfev=2000, xtol=1e-12, ftol=1e-12)
        # Accept only positive, strictly increasing positions
        if np.all(sol > 0) and np.all(np.diff(sol) > 0):
            return True, sol
        else:
            return False, None
    except Exception:
        return False, None

def critical_tau(d, n):
    """Binary search for the minimum tau_a (Pa) that allows a static solution."""
    # Initial guess scaled with d
    x0_guess = np.linspace(d * 0.2, d * 1.5, n)
    # Ensure a feasible upper bound
    high = 5000e6
    ok, _ = has_solution(x0_guess, high, d, n)
    if not ok:
        high = 10000e6
        ok, _ = has_solution(x0_guess, high, d, n)
        if not ok:
            sys.stderr.write(f"No solution at 10 GPa for d={d*1e9:.1f} nm, n={n}\n")
            return None
    best = high
    low = 0.0               # lower bound for bisection (must not be negative)
    # Refine by bisection
    for _ in range(40):
        mid = (high + low) / 2.0
        ok, sol = has_solution(x0_guess, mid, d, n)
        if ok:
            best = mid
            high = mid
            x0_guess = sol        # continuation
        else:
            low = mid
    return best

# Output CSV
outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'simulation_results.csv')

# Parameter ranges
d_nm_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
             120, 140, 160, 180, 200, 250, 300, 350, 400, 450, 500]
n_list = [5, 10, 15, 20]

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['d_nm', 'n', 'tau_a_MPa'])
    for n in n_list:
        for d_nm in d_nm_list:
            d = d_nm * 1e-9
            tau_c = critical_tau(d, n)
            if tau_c is not None:
                tau_MPa = tau_c / 1e6
                writer.writerow([d_nm, n, round(tau_MPa, 2)])
                sys.stderr.write(f"d={d_nm} nm, n={n} -> tau_a={tau_MPa:.2f} MPa\n")
            else:
                sys.stderr.write(f"Skipping d={d_nm} nm, n={n} (no converged solution)\n")
PYEOF
