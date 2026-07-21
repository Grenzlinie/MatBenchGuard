import sys
import os
import csv
import numpy as np
from scipy.special import jv, yv

UNZ = 1.0
A0 = 0.01
PI = np.pi

def f0_value(R, omega):
    z = abs(omega) * R
    sgn = np.sign(omega)
    if z == 0:
        J0 = 1.0
        Y0 = -np.inf
    else:
        J0 = jv(0, z)
        Y0 = yv(0, z)
    return -sgn * J0 - 1j * Y0

def f1_value(R, omega):
    z = abs(omega) * R
    sgn = np.sign(omega)
    J1 = jv(1, z)
    Y1 = yv(1, z)
    return -1j * J1 + sgn * Y1

def g0(omega):
    return (1j * omega / 4.0) * f0_value(A0, omega)

def B_omega(omega):
    g = g0(omega)
    denom = 1.0 - (UNZ**2) * (g**2)
    return (UNZ * omega**2) / (16.0 * PI * denom)

def ldos(R, omega):
    rho0 = abs(omega) / 4.0
    B = B_omega(omega)
    f0 = f0_value(R, omega)
    f1 = f1_value(R, omega)
    correction = 2.0 * np.imag(B) * UNZ * (f0**2 - f1**2)
    result = rho0 + correction
    return float(np.real(result))

def spin_density(R, omega, theta=0.0):
    B = B_omega(omega)
    ImB = np.imag(B)
    f0 = f0_value(R, omega)
    f1 = f1_value(R, omega)
    common1 = f0**2 + f1**2
    common2 = -2j * f0 * f1
    sx = ImB * common2 * np.cos(theta)
    sy = ImB * common2 * np.sin(theta)
    sz = ImB * common1
    return float(np.real(sx)), float(np.real(sy)), float(np.real(sz))

def chi_zz(R):
    return -1.0 / (8.0 * PI * R**3)

def find_resonance():
    omegas = np.linspace(0.01, 1.0, 10000)
    min_abs = np.inf
    best_omega = 0.5
    for omega in omegas:
        g = g0(omega)
        val = 1.0 - g**2
        if abs(val) < min_abs:
            min_abs = abs(val)
            best_omega = omega
    return best_omega

def generate_ldos():
    omega = -0.7
    R_values = np.linspace(0.1, 10.0, 20)
    rows = []
    for R in R_values:
        rho = ldos(R, omega)
        rows.append((R, rho))
    with open("/app/outputs/ldos_decay.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["R", "rho"])
        for R, rho in rows:
            writer.writerow([f"{R:.12g}", f"{rho:.12g}"])

def generate_spin_parity():
    R = 0.5
    theta = 0.0
    omegas = np.linspace(-1.0, 1.0, 200)
    rows = []
    for omega in omegas:
        sx, sy, sz = spin_density(R, omega, theta)
        rows.append((omega, sx, sy, sz))
    with open("/app/outputs/spin_parity.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["omega", "s_x", "s_y", "s_z"])
        for omega, sx, sy, sz in rows:
            writer.writerow([f"{omega:.12g}", f"{sx:.12g}", f"{sy:.12g}", f"{sz:.12g}"])

def generate_rkky():
    R_values = np.linspace(0.1, 10.0, 20)
    rows = []
    for R in R_values:
        ch = chi_zz(R)
        rows.append((R, ch))
    with open("/app/outputs/rkky_decay.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["R", "chi_zz"])
        for R, ch in rows:
            writer.writerow([f"{R:.12g}", f"{ch:.12g}"])

def generate_resonance():
    omega_loc = find_resonance()
    with open("/app/outputs/resonance_energy.txt", "w") as f:
        f.write(f"{omega_loc:.12g}\n")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "ldos_decay":
        generate_ldos()
    elif mode == "spin_parity":
        generate_spin_parity()
    elif mode == "rkky_decay":
        generate_rkky()
    elif mode == "resonance_energy":
        generate_resonance()
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)
