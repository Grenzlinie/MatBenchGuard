#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: q_es_values.csv ===
python3 << 'PYEOF'
import csv, math
import numpy as np
from scipy.special import spherical_jn, spherical_yn, sici

euler = 0.57721566490153286060651209
n = 1.33
alphas = [2, 4, 6, 8, 10]

def jn_scalar(order, z):
    return spherical_jn(order, z, derivative=False)

def yn_scalar(order, z):
    return spherical_yn(order, z, derivative=False)

def psi1(z):
    return z * jn_scalar(1, z)

def psi1_deriv(z):
    j0 = jn_scalar(0, z)
    j1 = jn_scalar(1, z)
    d_j1 = j0 - 2.0 / z * j1
    return j1 + z * d_j1

def chi1(z):
    return -z * yn_scalar(1, z)

def chi1_deriv(z):
    y0 = yn_scalar(0, z)
    y1 = yn_scalar(1, z)
    d_y1 = y0 - 2.0 / z * y1
    return -(y1 + z * d_y1)

def mie_cd_internal(m, x):
    rho = x
    rho_s = m * x
    psi_rho = psi1(rho)
    psi_rho_p = psi1_deriv(rho)
    psi_s = psi1(rho_s)
    psi_s_p = psi1_deriv(rho_s)
    chi_rho = chi1(rho)
    chi_rho_p = chi1_deriv(rho)
    xi_rho = psi_rho - 1j * chi_rho
    xi_rho_p = psi_rho_p - 1j * chi_rho_p

    # c_n (TE internal)
    numerator_c = m * (psi_rho * psi_s_p - psi_rho_p * psi_s)
    denominator_c = xi_rho * psi_s_p - xi_rho_p * psi_s
    c = numerator_c / denominator_c

    # d_n (TM internal)
    numerator_d = m * (psi_rho_p * psi_s - psi_rho * psi_s_p)
    denominator_d = xi_rho_p * psi_s - xi_rho * psi_s_p
    d = numerator_d / denominator_d

    return c, d

mie_rows = []
qes_rows = []

for alpha in alphas:
    x = alpha / n
    c1, d1 = mie_cd_internal(n, x)
    c1_mag2 = abs(c1)**2
    d1_mag2 = abs(d1)**2

    xarg = n * alpha
    I1 = (2*xarg**4 - 2*xarg**2 - 1 + math.cos(2*xarg) + 2*xarg*math.sin(2*xarg)) / (8 * xarg**4)
    si, ci = sici(2*xarg)
    term = euler - 1 - ci + math.log(2*xarg) + (2*xarg*math.cos(xarg) - math.sin(xarg))*math.sin(xarg) / (xarg**2)
    I2 = 0.5 * term
    I3 = I1 + I2 - (xarg**2 - 3*math.sin(xarg)**2 + xarg*math.sin(2*xarg)) / (2*xarg**2)

    prefactor = 2*(n**2 - 1)*(n**2 + 2) / (8*alpha**2)
    Q_ES = prefactor * (c1_mag2 * (4*I1 + I2) + d1_mag2 * I3)

    mie_rows.append([alpha, c1.real, c1.imag, d1.real, d1.imag, I1, I2, I3])
    qes_rows.append([alpha, Q_ES])

with open('/app/outputs/mie_internal_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'c1_real', 'c1_imag', 'd1_real', 'd1_imag', 'I1', 'I2', 'I3'])
    writer.writerows(mie_rows)

with open('/app/outputs/q_es_values.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'Q_ES'])
    writer.writerows(qes_rows)
PYEOF
