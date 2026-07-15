#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: temperature_field.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.special import jn_zeros, j0, j1
from scipy.integrate import quad
import csv, os, sys

# All parameters in mm, W, K
R = 3.0                # mm
L = 2.0                # mm
omega = 0.32           # mm pump radius
beta_cm = 20.7         # cm⁻¹
beta = beta_cm / 10.0  # 2.07 mm⁻¹
P = 20.0               # W
lam_m_K = 13.0         # W/(m·K) → 0.013 W/(mm·K)
lam = lam_m_K / 1000.0
eta = 1.0 - 808.0/1064.0
I0 = 2.0 * P / (np.pi * omega**2)   # W/mm²
T_air = 5.0            # °C
sigma_vals = [0.0, 0.6, 100.0]      # large σ approximates ∞

N_terms = 25
alpha = jn_zeros(0, N_terms)        # zeros of J₀
J1a = j1(alpha)
J0prime = -J1a                       # J₀'(αₙ) = -J₁(αₙ)

# Pre‑compute radial integrals Iₙ = ∫₀ᴿ r J₀(αₙ r/R) exp(-2r²/ω²) dr
def radial_integral_n(n):
    a_val = alpha[n]
    f = lambda r: r * j0(a_val * r / R) * np.exp(-2.0 * r**2 / omega**2)
    val, _ = quad(f, 0.0, R, limit=200)
    return val

Irad = np.array([radial_integral_n(n) for n in range(N_terms)])

nr = 101
nz = 101
r_vals = np.linspace(0.0, R, nr)
z_vals = np.linspace(0.0, L, nz)

def field_for_sigma(sigma):
    U = np.zeros((nr, nz))
    for n in range(N_terms):
        a_val = alpha[n]
        c = a_val / R                      # α/R
        J0p = J0prime[n]
        I_n = Irad[n]

        # fₙ(z) = Cₙ exp(-β z)
        C_n = (2.0 * eta * beta * I0 / (lam * R**2 * J0p**2)) * I_n

        # φₙ(z) = (R/α) ∫₀ᶻ sinh(c (z-τ)) fₙ(τ) dτ   (analytical)
        a_val_ = c
        b = beta
        apb = a_val_ + b
        amb = a_val_ - b
        ez = np.exp(a_val_ * z_vals)
        emz = np.exp(-a_val_ * z_vals)
        ebz = np.exp(-b * z_vals)
        I_int = 0.5 * (ez/apb + emz/amb + ebz*(1.0/(b - a_val_) - 1.0/apb))
        phi = (R / a_val) * C_n * I_int

        # φ'(L) via central diff
        dphi = np.gradient(phi, z_vals)
        phi_prime_L = dphi[-1]

        # Boundary condition constants
        rhs_common = -2.0 * sigma * T_air / (a_val * J0p)
        S = np.sinh(c * L)
        C = np.cosh(c * L)

        # Eq1:  -c B + σ A = rhs_common
        # Eq2:  (c S + σ C) A + (c C + σ S) B + (φ'(L)+σ φ(L)) = rhs_common
        mat = [[sigma, -c], [c*S + sigma*C, c*C + sigma*S]]
        rhs1 = rhs_common
        rhs2 = rhs_common - (phi_prime_L + sigma * phi[-1])

        det = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        if abs(det) > 1e-30:
            A_n = (rhs1*mat[1][1] - mat[0][1]*rhs2) / det
            B_n = (mat[0][0]*rhs2 - mat[1][0]*rhs1) / det
        else:
            A_n = B_n = 0.0

        cosh_cz = np.cosh(c * z_vals)
        sinh_cz = np.sinh(c * z_vals)
        u_n_z = A_n * cosh_cz + B_n * sinh_cz + phi

        radial = j0(a_val * r_vals / R)
        U += np.outer(radial, u_n_z)
    return U

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'temperature_field.csv')
with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sigma', 'r_mm', 'z_mm', 'u_degC'])
    for sig in sigma_vals:
        U = field_for_sigma(sig)
        for i in range(nr):
            for j in range(nz):
                w.writerow([sig, r_vals[i], z_vals[j], U[i, j]])
print('temperature_field.csv written')
PYEOF
