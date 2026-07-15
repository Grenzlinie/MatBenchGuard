#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/compute.py

# === solve block: thermal_conductivity.csv ===
python3 << 'PYEOF' > /dev/null
import numpy as np
import scipy.integrate as integrate
import csv, math

OUTDIR = "/app/outputs"

# Universal constants
kB = 1.380649e-23          # J/K
hbar = 1.054571817e-34     # J·s
pi = math.pi

# Material parameters (Table 2 and text)
Theta = 141.0              # K
alpha = 1.0
Theta1 = 57.0
Theta2 = 95.0
Theta3 = 145.0
Theta4 = 100.0

# Group velocities (cm/s -> m/s)
V_T1 = 1.98e5 * 1e-2       # 1980.0 m/s
V_T2 = 1.32e5 * 1e-2       # 1320.0 m/s
V_L1 = 4.07e5 * 1e-2       # 4070.0 m/s
V_L2 = 1.97e5 * 1e-2       # 1970.0 m/s

# Scattering parameters
tauB_inv = 6.17e5           # s^{-1}
A_pt = 57.0e-44             # s^3

# Three-phonon prefactors
B_T = 3.82e-5               # K^{-m}
B_L1 = 7.5e-22              # s·K^{-m}
B_L2 = 5.0e-18              # s·K^{-m}

# Temperature list for output (at least these points)
Ts = [2, 5, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 250, 300]

def m_T1(T):
    x = Theta2 / T
    return x / (np.exp(x) - 1) + 0.5*x + np.log(1 + Theta/(alpha*T)) / np.log(T)

def m_L1(T):
    x = Theta3 / T
    return x / (np.exp(x) - 1) + 0.5*x + np.log(1 + Theta/(alpha*T)) / np.log(T)

def m_L2(T):
    x = Theta3 / T
    term = 0.5 * x / (np.exp(x) - 1) * np.exp(0.5*x) + 0.5
    return term + np.log(1 + Theta/(alpha*T)) / np.log(T)

def tau_pt_inv(x, T):
    omega = (kB / hbar) * x * T
    return A_pt * omega**4

def tau3ph_T(x, T):
    omega = (kB / hbar) * x * T
    m = m_T1(T)
    return B_T * omega * (T ** m) * np.exp(-Theta / (alpha * T))

def tau3ph_L(x, T):
    omega = (kB / hbar) * x * T
    m1 = m_L1(T)
    m2 = m_L2(T)
    rate = (B_L1 * omega**2 * (T ** m1) +
            B_L2 * omega**2 * (T ** m2)) * np.exp(-Theta / (alpha * T))
    return rate

def integr_k(x, T, branch):
    # integrand for thermal conductivity integral (without prefactor)
    x4 = x**4
    ex = np.exp(x)
    dens = x4 * ex / (ex - 1)**2
    tau_total = tauB_inv + tau_pt_inv(x, T)
    if branch == 'T':
        tau_total += tau3ph_T(x, T)
    else:  # 'L'
        tau_total += tau3ph_L(x, T)
    return dens / tau_total

output_path = f"{OUTDIR}/thermal_conductivity.csv"
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'K_total', 'K_transverse', 'K_longitudinal'])
    for T in Ts:
        # Prefactor common to all integrals (in W/(m·K))
        prefac = (kB / (2 * pi**2)) * (kB * T / hbar)**3

        # Transverse K_T: two intervals
        # First interval [0, Theta1/T] with V_T1
        upper1 = Theta1 / T
        if upper1 > 1e-8:
            I_T1, _ = integrate.quad(integr_k, 0, upper1, args=(T, 'T'), limit=200, epsabs=1e-12, epsrel=1e-8)
        else:
            I_T1 = 0.0
        # Second interval [Theta1/T, Theta2/T] with V_T2
        upper2 = Theta2 / T
        if upper2 > upper1 + 1e-8:
            I_T2, _ = integrate.quad(integr_k, upper1, upper2, args=(T, 'T'), limit=200, epsabs=1e-12, epsrel=1e-8)
        else:
            I_T2 = 0.0
        K_T = (2/3) * prefac * (I_T1 / V_T1 + I_T2 / V_T2)

        # Longitudinal K_L: two intervals
        # First interval [0, Theta4/T] with V_L1
        upper4 = Theta4 / T
        if upper4 > 1e-8:
            I_L1, _ = integrate.quad(integr_k, 0, upper4, args=(T, 'L'), limit=200, epsabs=1e-12, epsrel=1e-8)
        else:
            I_L1 = 0.0
        # Second interval [Theta4/T, Theta3/T] with V_L2
        upper3 = Theta3 / T
        if upper3 > upper4 + 1e-8:
            I_L2, _ = integrate.quad(integr_k, upper4, upper3, args=(T, 'L'), limit=200, epsabs=1e-12, epsrel=1e-8)
        else:
            I_L2 = 0.0
        K_L = (1/3) * prefac * (I_L1 / V_L1 + I_L2 / V_L2)

        K_total = K_T + K_L
        writer.writerow([T, K_total, K_T, K_L])

print(f"thermal_conductivity.csv written to {output_path}")
PYEOF
