#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy
mkdir -p /app/outputs

# === solve block: stability_boundaries.csv ===
python3 <<'PYEOF'
import numpy as np
from scipy.optimize import fsolve

# Hamiltonian parameters
J0 = 0.8
D = 0.4
K0 = 1.0
zeta = 1.2
eta = 0.8
xi = 1.25

# Self-consistency equations (8) as residuals
def self_cons(vars, theta):
    m, q, h = vars
    if theta <= 0:
        return [1e6]*3
    A = (h + 2*J0*m) / theta
    B = (6*K0*q - D) / theta
    expB = np.exp(B)
    coshA = np.cosh(A)
    sinhA = np.sinh(A)
    denom = 1 + 2*coshA*expB
    m_calc = 2*sinhA*expB / denom
    q_calc = 1/3 - 1/denom
    return [m - m_calc, q - q_calc]

# Branch 1: omega1 = 0  => 2h + 4*m*(J0 - zeta*K0) = 0
def eq1(vars, theta):
    m, q, h = vars
    res_m, res_q = self_cons([m, q, h], theta)
    gap = 2*h + 4*m*(J0 - zeta*K0)
    return [res_m, res_q, gap]

# Branch 2: omega2 = 0
def eq2(vars, theta):
    m, q, h = vars
    res_m, res_q = self_cons([m, q, h], theta)
    term = m**2 * (xi*J0 - eta*K0)**2 + (D - 6*q*(K0 - xi*J0))*(D - 6*q*(K0 - eta*K0))
    sqrt_term = np.sqrt(max(term, 0.0))
    gap = h + m*(2*J0 - xi*J0 - eta*K0) - sqrt_term
    return [res_m, res_q, gap]

# Write stability_boundaries.csv
with open('/app/outputs/stability_boundaries.csv', 'w') as f:
    f.write('reduced_temperature,reduced_field,boundary_type\n')
    
    # Branch 1 trace
    theta_vals = np.linspace(0.01, 2.0, 400)
    prev = None
    for theta in theta_vals:
        if prev is None:
            # low-T guess: m=1, q=1/3, h = 0.8*m = 0.8
            guess = [1.0, 1/3, 0.8]
        else:
            guess = prev
        try:
            sol = fsolve(eq1, guess, args=(theta,), xtol=1e-12, maxfev=1000)
            m_s, q_s, h_s = sol
            # Re-check gap (should be zero)
            gap = 2*h_s + 4*m_s*(J0 - zeta*K0)
            if abs(gap) < 1e-8:
                f.write(f"{theta},{h_s},1\n")
                prev = sol
            else:
                prev = None
        except Exception:
            prev = None

    # Branch 2 trace
    prev = None
    for theta in theta_vals:
        if prev is None:
            # low-T guess: m=1, q=1/3, find h0 from omega2=0
            m0, q0 = 1.0, 1/3
            term0 = m0**2 * (xi*J0 - eta*K0)**2 + (D - 6*q0*(K0 - xi*J0))*(D - 6*q0*(K0 - eta*K0))
            sqrt0 = np.sqrt(max(term0, 0.0))
            h0 = sqrt0 - m0*(2*J0 - xi*J0 - eta*K0)
            guess = [m0, q0, h0]
        else:
            guess = prev
        try:
            sol = fsolve(eq2, guess, args=(theta,), xtol=1e-12, maxfev=1000)
            m_s, q_s, h_s = sol
            term = m_s**2 * (xi*J0 - eta*K0)**2 + (D - 6*q_s*(K0 - xi*J0))*(D - 6*q_s*(K0 - eta*K0))
            sqrt_term = np.sqrt(max(term, 0.0))
            gap = h_s + m_s*(2*J0 - xi*J0 - eta*K0) - sqrt_term
            if abs(gap) < 1e-8:
                f.write(f"{theta},{h_s},2\n")
                prev = sol
            else:
                prev = None
        except Exception:
            prev = None
PYEOF

# === solve block: pt_temperature_vs_zeta.csv ===
python3 /solution/compute.py --output pt_temperature_vs_zeta
