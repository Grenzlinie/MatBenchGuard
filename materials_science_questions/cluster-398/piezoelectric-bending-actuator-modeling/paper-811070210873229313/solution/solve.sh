#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_power_output.csv ===
python3 <<'PYEOF' >"$OUTDIR/step_01_power_output.csv"
import numpy as np

# Constants (SI)
V_drive = 1.0

# Piezo disk
c_d = 3802.0
rho_d = 7500.0
d_d = 1.6e-3
diam = 0.025
area = np.pi * (diam/2)**2
K_eps = 4.703e-9
h = 3.402e9
Z_disk = rho_d * c_d          # acoustic impedance (Rayl)

# Stainless steel
c_ss = 6000.0
rho_ss = 7800.0
L_ss = 2.52e-3
Z_ss = rho_ss * c_ss

# Polythene
c_p = 2000.0
rho_p = 930.0
L_p = 100e-6
Z_p = rho_p * c_p

# Water
c_w = 1480.0
rho_w = 1000.0
Z_w = rho_w * c_w

# Air
c_a = 330.0
rho_a = 1.3
Z_a = rho_a * c_a

# m1 (air load) is constant
m1 = Z_a / Z_disk
m1_m1 = m1 - 1.0
m1_p1 = 1.0 + m1

# Frequency array
freq = np.linspace(1.0e6, 1.2e6, 201)
omega = 2.0 * np.pi * freq

# Phase in disk
k_d = omega / c_d
beta = k_d * d_d
e_ip = np.exp(1j * beta)
e_im = np.exp(-1j * beta)

# Phase in layers
k_ss = omega / c_ss
k_p = omega / c_p

# Helper: input impedance of a layer
# Z0 = characteristic impedance, ZL = load, phi = kL
def Z_in(Z0, ZL, phi):
    return Z0 * (ZL * np.cos(phi) + 1j * Z0 * np.sin(phi)) / (Z0 * np.cos(phi) + 1j * ZL * np.sin(phi))

# Layer phases
phi_ss = k_ss * L_ss
phi_p = k_p * L_p

# No membrane: stainless steel -> water
Z_right_no = Z_in(Z_ss, Z_w, phi_ss)

# With membrane: water -> polythene -> stainless steel
Z_in_poly = Z_in(Z_p, Z_w, phi_p)
Z_right_with = Z_in(Z_ss, Z_in_poly, phi_ss)

# Compute electrical impedance and power for a given load Z_right
def impedance(Z_right):
    m2 = Z_right / Z_disk
    # Solve linear system for B/Y and C/Y
    N_C = 1.0 + e_im * (m2 - 1.0) / m1_p1
    D_C = e_ip * (m2 + 1.0) - e_im * (m2 - 1.0) * m1_m1 / m1_p1
    C_Y = N_C / D_C
    B_Y = (-1.0 - C_Y * m1_m1) / m1_p1
    # Displacement difference
    DXi_Y = B_Y * (e_im - 1.0) + C_Y * (e_ip - 1.0)
    # Motional impedance (from first-principles derivation)
    Z_mot = (h**2) / (area * omega**2 * Z_disk) * DXi_Y
    # Capacitive term
    Z_cap = d_d / (1j * omega * area * K_eps)
    return Z_cap + Z_mot

Z_no = impedance(Z_right_no)
Z_with = impedance(Z_right_with)

# Power with V=1 V
P_no = V_drive**2 * np.real(Z_no) / (2.0 * np.abs(Z_no)**2)
P_with = V_drive**2 * np.real(Z_with) / (2.0 * np.abs(Z_with)**2)

# Write CSV
print("frequency_Hz,power_without_membrane_W,power_with_membrane_W")
for i in range(len(freq)):
    print(f"{freq[i]:.4f},{P_no[i]:.15e},{P_with[i]:.15e}")
PYEOF
