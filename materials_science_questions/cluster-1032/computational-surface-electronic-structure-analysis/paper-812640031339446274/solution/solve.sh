#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy
export OUTDIR=/app/outputs

# === solve block: step_01_eigenenergies.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.special import jv
from scipy.optimize import minimize_scalar
from scipy.integrate import trapezoid
import csv

# Bi2Se3 material parameters (eV, A)
m0 = -0.169
m1 = 3.353
m2 = 29.375
A  = 2.513
B  = 1.836
R0 = 1.49  # nm

radii_nm = [2*R0, 4*R0, 6*R0, 8*R0, 10*R0]
radii_A  = [r * 10.0 for r in radii_nm]

def kappa(E):
    # Eq. (8) with kz=0
    inner = A**4/(4*m2**4) + E**2/m2**2 + A**2*m0/m2**3
    s = np.sqrt(complex(inner))
    base = -(m0/m2 + A**2/(2*m2**2))
    kp = np.sqrt(complex(base + s))
    km = np.sqrt(complex(base - s))
    return kp, km

def Delta(k, E):
    return m2*k**2 + m0 - E

def T(j, z):
    return jv(j+0.5, z) / jv(j-0.5, z)

def secular_a(E, j, R):
    """Secular equation (12a) for parity (-1)^{j-1/2}"""
    kp, km = kappa(E)
    dp = Delta(kp, E)
    dm = Delta(km, E)
    lhs = (kp * dm) / (km * dp)
    rhs = T(j, kp * R) / T(j, km * R)
    return abs(lhs - rhs)

# ---- Step 1: eigenenergies ----
with open('/app/outputs/step_01_eigenenergies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['j', 'R', 'energy'])
    for jval in [0.5, 1.5]:
        for R_nm, R_A in zip(radii_nm, radii_A):
            # lowest positive-energy surface state from eq (12a)
            res = minimize_scalar(lambda x: secular_a(x, jval, R_A),
                                  bounds=(1e-6, 2.0), method='bounded',
                                  options={'xatol': 1e-12, 'maxiter': 200})
            E = res.x
            w.writerow([jval, R_nm, E])

# ---- Step 2: overlap integrals ----
def find_root_any(E_low, E_high, j, R):
    """Find a root of either secular equation in [E_low, E_high]; used for negative energies."""
    best_E = None
    best_val = np.inf
    for func in (secular_a, lambda E,j,R: abs(secular_a(-E,j,R))):  # search both parities
        try:
            res = minimize_scalar(lambda x: func(x, j, R),
                                  bounds=(E_low, E_high), method='bounded',
                                  options={'xatol': 1e-12, 'maxiter': 200})
            if res.fun < best_val and abs(res.x) > 1e-8:
                best_val = res.fun
                best_E = res.x
        except Exception:
            pass
    return best_E

def wavefunction_alpha(j, E, R, num_radial_points=500):
    """Return radial grid and normalised Phi1, Phi4 for a pure-alpha state (beta_eta=0)."""
    kp, km = kappa(E)
    dp = Delta(kp, E)
    dm = Delta(km, E)
    # enforce hard-wall: alpha_- / alpha_+ from boundary condition
    Jp = jv(j+0.5, kp*R)
    Jm = jv(j+0.5, km*R)
    alpha_plus = 1.0
    alpha_minus = - (Jp / Jm) * alpha_plus
    rho = np.linspace(0, R, num_radial_points)
    Phi1 = (alpha_plus * (1j*A*kp/dp) * jv(j-0.5, kp*rho) +
            alpha_minus * (1j*A*km/dm) * jv(j-0.5, km*rho))
    Phi4 = (alpha_plus * jv(j+0.5, kp*rho) +
            alpha_minus * jv(j+0.5, km*rho))
    # normalise
    norm = trapezoid(rho * (np.abs(Phi1)**2 + np.abs(Phi4)**2), rho)
    Phi1 /= np.sqrt(norm)
    Phi4 /= np.sqrt(norm)
    return rho, Phi1, Phi4

with open('/app/outputs/step_02_overlap_integrals.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['j', 'R', 'S_14', 'S_23'])
    for R_nm, R_A in zip(radii_nm, radii_A):
        # energies for s=-, j=-0.5 and s=+, j=+0.5
        E_neg = find_root_any(-2.0, -1e-6, -0.5, R_A)
        E_pos = find_root_any(1e-6, 2.0, 0.5, R_A)
        rho_neg, Phi1_neg, Phi4_neg = wavefunction_alpha(-0.5, E_neg, R_A)
        rho_pos, Phi1_pos, Phi4_pos = wavefunction_alpha( 0.5, E_pos, R_A)
        S14 = trapezoid(rho_pos * np.conj(Phi1_pos) * Phi4_neg, rho_pos)
        S23 = 0.0   # pure alpha states have zero Phi2, Phi3
        w.writerow([0.5, R_nm, float(np.real(S14)), S23])
PYEOF

# === solve block: step_02_overlap_integrals.csv ===
true  # already produced by compute.py
