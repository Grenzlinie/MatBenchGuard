#!/usr/bin/env python3
import sys
import csv
import numpy as np
from scipy.integrate import quad
from scipy.special import j0

# Model parameters (all public, from the paper)
eps_s = 78.3
eps_star = 6.0
eps_1 = 4.0
L = 5.0

# ---------- Φ integral (Eq. 8) ----------
def phi_integrand(x, R, Z, Z0):
    factor1 = 1.0 - eps_star/eps_s
    factor2 = eps_star/eps_s
    a = (1.0 + (x*L)**(-2))**(-0.5)
    term1 = factor1 * a * np.exp(-Z0 * np.sqrt(x**2 + L**(-2))) + factor2 * np.exp(-x*Z0)
    term2 = factor1 * a * np.exp(-Z * np.sqrt(x**2 + L**(-2))) + factor2 * np.exp(-x*Z)
    Delta = factor1 * a + factor2 + eps_star/eps_1
    return j0(x*R) * term1 * term2 / Delta

def phi(R, Z, Z0):
    res, _ = quad(phi_integrand, 0, np.inf, args=(R, Z, Z0), epsabs=1e-12, epsrel=1e-8)
    return res

# ---------- ε_eff_NL (Eq. 7) ----------
def epsilon_eff_NL(R, Z, Z0):
    r12 = np.sqrt(R**2 + (Z - Z0)**2)
    factor1 = 1.0 - eps_star/eps_s
    factor2 = eps_star/eps_s
    Phi_val = phi(R, Z, Z0)
    term1 = factor1 * np.exp(-r12/L) + factor2
    term2 = r12 / np.sqrt(R**2 + (Z + Z0)**2) * (factor1 * np.exp(-np.sqrt(R**2 + (Z + Z0)**2)/L) + factor2)
    eps_inv = (term1 + term2 - 2.0 * Phi_val * r12) / eps_star
    if eps_inv <= 0:
        return 1e10   # numerical guard; should never happen
    return 1.0 / eps_inv

def U12_NL(R, Z, Z0):
    r12 = np.sqrt(R**2 + (Z - Z0)**2)
    eps = epsilon_eff_NL(R, Z, Z0)
    return 1.0 / (eps * r12)

# ---------- Ψ integral (Eq. 17) ----------
def psi_integrand(x, R, Z_abs, Z0):
    factor3 = (eps_s/eps_star - 1.0)
    Delta1 = 1.0 + eps_s/eps_1 + factor3 * (1.0 + (x*L)**(-2))**(-0.5)
    factor4 = (eps_star/eps_1) * ((eps_s + eps_1)/(eps_s - eps_star))
    Delta2 = 1.0 + factor4 * (1.0 + (x*L)**(-2))**(0.5)
    term = np.exp(-x * Z_abs) * (np.exp(-x * Z0) / Delta1 + np.exp(-(Z0/L) * np.sqrt(1 + (x*L)**2)) / Delta2)
    return j0(x*R) * term

def psi(R, Z, Z0):
    Z_abs = abs(Z)
    res, _ = quad(psi_integrand, 0, np.inf, args=(R, Z_abs, Z0), epsabs=1e-12, epsrel=1e-8)
    return res

# ---------- ε_eff_NL_cross (Eq. 16) ----------
def epsilon_eff_NL_cross(R, Z, Z0):
    r13 = np.sqrt(R**2 + (Z0 + abs(Z))**2)
    Psi_val = psi(R, Z, Z0)
    eps_inv = (2.0 * r13 / eps_1) * Psi_val
    if eps_inv <= 0:
        return 1e10
    return 1.0 / eps_inv

def U13_NL_cross(R, Z, Z0):
    r13 = np.sqrt(R**2 + (Z0 + abs(Z))**2)
    eps = epsilon_eff_NL_cross(R, Z, Z0)
    return 1.0 / (eps * r13)

# ---------- Slab energy (Eq. 21) ----------
def slab_U(R, Z, d, eps_slab):
    def integrand(x):
        D = 1.0 - ((eps_slab - eps_1)/(eps_slab + eps_1))**2 * np.exp(-2.0*x*d)
        return j0(x*R) * np.exp(-x*Z) / D
    int_val, _ = quad(integrand, 0, np.inf, epsabs=1e-12, epsrel=1e-8)
    RHS = 4.0 * eps_slab * (eps_1 + eps_slab)**(-2) * int_val
    U = RHS * 560.0   # magnitude of attractive energy (positive)
    return U

# ===== test points definitions =====

def write_phi_values(filename):
    points = []
    Z0 = 1.5
    for r in [1.0, 3.0, 5.0, 7.0, 10.0, 15.0]:
        points.append((r, Z0, Z0))          # parallel
        points.append((0.0, Z0+r, Z0))     # perpendicular
    Z0 = 6.5
    for r in [1.0, 3.0, 5.0, 7.0, 10.0, 15.0]:
        points.append((r, Z0, Z0))
        points.append((0.0, Z0+r, Z0))
    Z0 = 35.0
    for r in [1.0, 5.0, 10.0, 20.0]:
        points.append((r, Z0, Z0))
        points.append((0.0, Z0+r, Z0))
    points.append((0.0, 100.0, 100.0))
    points.append((0.0, 50.0, 50.0))
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['R','Z','Z0','Phi'])
        for (R, Z, Z0) in points:
            writer.writerow([R, Z, Z0, phi(R, Z, Z0)])

def write_psi_values(filename):
    points = []
    for Z0 in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 40.0]:
        points.append((0.0, -1.5, Z0))
    points.append((0.0, -3.0, 1.0))
    points.append((0.0, -3.0, 5.0))
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['R','Z','Z0','Psi'])
        for (R, Z, Z0) in points:
            writer.writerow([R, Z, Z0, psi(R, Z, Z0)])

def write_pe_energies(filename):
    # same points as phi for consistency
    points = []
    Z0 = 1.5
    for r in [1.0, 3.0, 5.0, 7.0, 10.0, 15.0]:
        points.append((r, Z0, Z0))
        points.append((0.0, Z0+r, Z0))
    Z0 = 6.5
    for r in [1.0, 3.0, 5.0, 7.0, 10.0, 15.0]:
        points.append((r, Z0, Z0))
        points.append((0.0, Z0+r, Z0))
    Z0 = 35.0
    for r in [1.0, 5.0, 10.0, 20.0]:
        points.append((r, Z0, Z0))
        points.append((0.0, Z0+r, Z0))
    points.append((0.0, 100.0, 100.0))
    points.append((0.0, 50.0, 50.0))
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['R','Z','Z0','U12_NL','epsilon_eff_NL'])
        for (R, Z, Z0) in points:
            writer.writerow([R, Z, Z0, U12_NL(R, Z, Z0), epsilon_eff_NL(R, Z, Z0)])

def write_cpe_energies(filename):
    points = []
    for Z0 in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 40.0]:
        points.append((0.0, -1.5, Z0))
    points.append((0.0, -3.0, 1.0))
    points.append((0.0, -3.0, 5.0))
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['R','Z','Z0','U13_NL_cross','epsilon_eff_NL_cross'])
        for (R, Z, Z0) in points:
            writer.writerow([R, Z, Z0, U13_NL_cross(R, Z, Z0), epsilon_eff_NL_cross(R, Z, Z0)])

def write_slab_energies(filename):
    specs = [('low_dielectric', 9.0), ('high_dielectric', 41.2)]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['case','epsilon_slab','U_slab_12'])
        for case, eps_slab in specs:
            writer.writerow([case, eps_slab, slab_U(0.0, 11.0, 6.0, eps_slab)])

# ===== main =====
if __name__ == '__main__':
    outname = None
    if len(sys.argv) >= 3 and sys.argv[1] == '--output':
        outname = sys.argv[2]
    elif len(sys.argv) == 2:
        outname = sys.argv[1]
    else:
        print("Usage: compute.py --output <basename>")
        sys.exit(1)

    dispatcher = {
        'phi_values.csv': write_phi_values,
        'psi_values.csv': write_psi_values,
        'pe_energies.csv': write_pe_energies,
        'cpe_energies.csv': write_cpe_energies,
        'slab_energies.csv': write_slab_energies
    }
    if outname not in dispatcher:
        print(f"Unknown output: {outname}")
        sys.exit(1)
    dispatcher[outname](f'/app/outputs/{outname}')
