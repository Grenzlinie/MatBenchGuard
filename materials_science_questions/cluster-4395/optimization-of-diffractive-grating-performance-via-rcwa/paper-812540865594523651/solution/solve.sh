#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: frequency_response.csv ===
python3 << 'PYEOF' > /app/outputs/frequency_response.csv
import numpy as np
from scipy.integrate import dblquad

# Constants
mu0 = 4e-7 * np.pi
eps0 = 8.854187817e-12
c = 299792458.0
Z0 = np.sqrt(mu0 / eps0)

# Given parameters
T = 3.0e-3
h = 1.29e-3
eps_r = 11.2
tan_delta = 0.0022
eps_diel_real = eps_r
eps_diel_complex = eps_r * (1 - 1j * tan_delta)

s_L1 = 2.846e-3
s_L2 = 1.570e-3
w_C1 = 1.770e-3
w_C2 = 2.205e-3

# Inductive admittance
def Y_inductive(s, eps1, eps2, omega):
    theta = np.pi * s / (2 * T)
    term1 = (2 * np.pi * 1j) / (omega * mu0 * s * np.log(1 / np.cos(theta)))
    term2 = -1j * omega * eps0 * T * (eps1 + eps2) / np.pi * np.log(1 / np.sin(theta))
    return term1 + term2

# Double integral X(a)
def X_val(a):
    f = lambda y, x: np.arcsin(np.sin(y) / np.sin(a))
    res, _ = dblquad(f, 0, a, lambda x: x, lambda x: a, epsabs=1e-12, epsrel=1e-12)
    return res

# Capacitive inductance and capacitance
def capacitive_L(w):
    theta = np.pi * w / (2 * T)
    ln_cosec = np.log(1 / np.sin(theta))
    ln_sec = np.log(1 / np.cos(theta))
    Xa = X_val(theta)
    L = (mu0 * T / (4 * np.pi)) * (ln_cosec + (np.pi**2 * w**2 / (12 * T**2) - (2 / np.pi) * Xa) / ln_sec)
    return L

def capacitive_C(w, eps1, eps2):
    theta = np.pi * w / (2 * T)
    C = eps0 * (eps1 + eps2) / np.pi * T * np.log(1 / np.cos(theta))
    return C

def Y_capacitive(w, eps1, eps2, omega):
    L = capacitive_L(w)
    C = capacitive_C(w, eps1, eps2)
    return 1j / (omega * L) - 1j * omega * C

# Grating S matrix
def grating_S(Y, eps1, eps2):
    sqrt_e1 = np.sqrt(eps1)
    sqrt_e2 = np.sqrt(eps2)
    denom = sqrt_e1 + sqrt_e2 + Z0 * Y
    S11 = (sqrt_e1 - sqrt_e2 - Z0 * Y) / denom
    S12 = 2 * (eps1 * eps2)**0.25 / denom
    S21 = S12
    S22 = (sqrt_e2 - sqrt_e1 - Z0 * Y) / denom
    return np.array([[S11, S12], [S21, S22]])

# S to ABCD
def S_to_ABCD(S, Z1, Z2):
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    Delta = S11*S22 - S21*S12
    A = (1 + S11 - S22 - Delta) * np.sqrt(Z1/Z2) / (2*S21)
    B = (1 + S11 + S22 + Delta) * np.sqrt(Z1*Z2) / (2*S21)
    C = (1 - S11 - S22 + Delta) / (2*S21 * np.sqrt(Z1*Z2))
    D = (1 - S11 + S22 - Delta) * np.sqrt(Z2/Z1) / (2*S21)
    return np.array([[A, B], [C, D]])

# Dielectric ABCD
def dielectric_ABCD(h, eps_complex, omega):
    eps_sqrt = np.sqrt(eps_complex)
    theta = omega * eps_sqrt * h / c
    cosT = np.cos(theta)
    sinT = np.sin(theta)
    A = cosT
    B = -1j * (Z0 / eps_sqrt) * sinT
    C = -1j * (eps_sqrt / Z0) * sinT
    D = cosT
    return np.array([[A, B], [C, D]])

# ABCD to S
def ABCD_to_S(ABCD, Z1, Z2):
    A, B, C, D = ABCD[0,0], ABCD[0,1], ABCD[1,0], ABCD[1,1]
    denom = A*Z2 + B + C*Z1*Z2 + D*Z1
    S11 = (A*Z2 + B - C*Z1*Z2 - D*Z1) / denom
    S12 = 2*(A*D - B*C)*np.sqrt(Z1*Z2) / denom
    S21 = 2*np.sqrt(Z1*Z2) / denom
    S22 = (-A*Z2 + B - C*Z1*Z2 + D*Z1) / denom
    return np.array([[S11, S12], [S21, S22]])

freqs = np.arange(8e9, 18e9 + 1e-8, 10e6)
omega = 2 * np.pi * freqs
Z_free = Z0 / np.sqrt(1.0)
Z_diel = Z0 / np.sqrt(eps_diel_real)

out_lines = ['f,S21_dB,S11_dB']
for idx, w in enumerate(omega):
    Y_L1 = Y_inductive(s_L1, 1.0, eps_diel_real, w)
    S_L1 = grating_S(Y_L1, 1.0, eps_diel_real)
    ABCD_L1 = S_to_ABCD(S_L1, Z_free, Z_diel)
    ABCD_d1 = dielectric_ABCD(h, eps_diel_complex, w)
    Y_C1 = Y_capacitive(w_C1, eps_diel_real, eps_diel_real, w)
    S_C1 = grating_S(Y_C1, eps_diel_real, eps_diel_real)
    ABCD_C1 = S_to_ABCD(S_C1, Z_diel, Z_diel)
    ABCD_d2 = dielectric_ABCD(h, eps_diel_complex, w)
    Y_L2 = Y_inductive(s_L2, eps_diel_real, eps_diel_real, w)
    S_L2 = grating_S(Y_L2, eps_diel_real, eps_diel_real)
    ABCD_L2 = S_to_ABCD(S_L2, Z_diel, Z_diel)
    ABCD_d3 = dielectric_ABCD(h, eps_diel_complex, w)
    Y_C2 = Y_capacitive(w_C2, eps_diel_real, eps_diel_real, w)
    S_C2 = grating_S(Y_C2, eps_diel_real, eps_diel_real)
    ABCD_C2 = S_to_ABCD(S_C2, Z_diel, Z_diel)
    ABCD_d4 = dielectric_ABCD(h, eps_diel_complex, w)
    Y_L2_2 = Y_L2
    S_L2_2 = S_L2
    ABCD_L2_2 = S_to_ABCD(S_L2_2, Z_diel, Z_diel)
    ABCD_d5 = dielectric_ABCD(h, eps_diel_complex, w)
    Y_C1_2 = Y_C1
    S_C1_2 = S_C1
    ABCD_C1_2 = S_to_ABCD(S_C1_2, Z_diel, Z_diel)
    ABCD_d6 = dielectric_ABCD(h, eps_diel_complex, w)
    Y_L1_2 = Y_inductive(s_L1, eps_diel_real, 1.0, w)
    S_L1_2 = grating_S(Y_L1_2, eps_diel_real, 1.0)
    ABCD_L1_2 = S_to_ABCD(S_L1_2, Z_diel, Z_free)

    ABCD_total = ABCD_L1
    ABCD_total = ABCD_total @ ABCD_d1
    ABCD_total = ABCD_total @ ABCD_C1
    ABCD_total = ABCD_total @ ABCD_d2
    ABCD_total = ABCD_total @ ABCD_L2
    ABCD_total = ABCD_total @ ABCD_d3
    ABCD_total = ABCD_total @ ABCD_C2
    ABCD_total = ABCD_total @ ABCD_d4
    ABCD_total = ABCD_total @ ABCD_L2_2
    ABCD_total = ABCD_total @ ABCD_d5
    ABCD_total = ABCD_total @ ABCD_C1_2
    ABCD_total = ABCD_total @ ABCD_d6
    ABCD_total = ABCD_total @ ABCD_L1_2

    S_total = ABCD_to_S(ABCD_total, Z_free, Z_free)
    S21 = np.abs(S_total[1, 0])
    S11 = np.abs(S_total[0, 0])
    S21_dB = 20 * np.log10(S21 + 1e-30)
    S11_dB = 20 * np.log10(S11 + 1e-30)
    out_lines.append(f'{freqs[idx]},{S21_dB:.6f},{S11_dB:.6f}')

print('\n'.join(out_lines))
PYEOF
