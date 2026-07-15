#!/usr/bin/env python3
"""Compute P, N, M for the thermo-magneto-mechanical tube problems.
Uses scipy.integrate.quad for numerical integration."""
import argparse
import csv
import numpy as np
from scipy.integrate import quad

# --- constants (SI) ---
mu0 = 4e-7 * np.pi               # vacuum permeability N/A^2
mu_e = 0.1e6                     # shear modulus at ref temp (Pa)
alpha_e = 30.0
m_e = 1.0                        # T^2
c2 = 0.5 * mu0                   # magneto-mechanical coupling
Theta_0 = 293.0                  # reference temperature (K)
Theta_i = 293.0                  # fixed internal temperature
A_i = 0.01                       # inner radius (m)

def theta(r, Theta_e, a_i, a_e):
    """Temperature profile Θ(r) = k1 + k2 ln r."""
    if a_e == a_i:
        return Theta_i, Theta_i, 0.0
    k2 = (Theta_e - Theta_i) / (np.log(a_e) - np.log(a_i))
    k1 = Theta_i - k2 * np.log(a_i)
    return k1 + k2 * np.log(r), k1, k2

def geometry(lambda_i, lambda_z, zeta):
    """Compute deformed radii a_i, a_e and helper b = A_i^2 - λ_z a_i^2."""
    A_e = zeta * A_i
    a_i = lambda_i * A_i
    b = A_i**2 - lambda_z * a_i**2
    a_e_sq = a_i**2 + (1.0/lambda_z)*(A_e**2 - A_i**2)
    a_e = np.sqrt(a_e_sq)
    return a_i, a_e, b

def R_sq(r, lam_z, b):
    return lam_z * r**2 + b

def I4(r, c_val, lam_z, b):
    """Magnetic invariant I4 = (c/R)^2."""
    return (c_val**2) / R_sq(r, lam_z, b)

def mu_val(I4_val):
    """Field-sensitive shear modulus μ(I4)."""
    return mu_e/4.0 * (1.0 + alpha_e * np.tanh(I4_val / m_e))

def omega1(r, Theta_e, a_i, a_e, c_val, lam_z, b):
    """Ω_1 = [Θ(r)/Θ_0] * μ(I4)."""
    I4v = I4(r, c_val, lam_z, b)
    Th, _, _ = theta(r, Theta_e, a_i, a_e)
    return (Th / Theta_0) * mu_val(I4v)

def omega5(r, Theta_e, a_i, a_e):
    Th, _, _ = theta(r, Theta_e, a_i, a_e)
    return (Th / Theta_0) * c2

def lam_sq(r, lam_z, b):
    """λ² = (r/R)² = r²/(λ_z r² + b)"""
    return r**2 / R_sq(r, lam_z, b)

def integrand_P(r, lam_z, c_val, Theta_e, a_i, a_e, b):
    """Integrand for pressure: (1/r)[σ_φφ - σ_rr] before adding Maxwell."""
    l2 = lam_sq(r, lam_z, b)
    # l2 = λ², l2_inv = λ⁻²
    l2_inv = 1.0 / l2
    om1 = omega1(r, Theta_e, a_i, a_e, c_val, lam_z, b)
    om5 = omega5(r, Theta_e, a_i, a_e)
    I4v = I4(r, c_val, lam_z, b)
    term = 2.0 * om1 * (l2 - 1.0/(l2 * lam_z**2)) - 2.0 * om5 * l2_inv * I4v
    return term / r

def compute_P(lambda_i, lambda_z, zeta, c_val, Theta_e):
    a_i, a_e, b = geometry(lambda_i, lambda_z, zeta)
    # pressure integral
    Pint, _ = quad(integrand_P, a_i, a_e, args=(lam_z, c_val, Theta_e, a_i, a_e, b),
                   epsabs=1e-12, epsrel=1e-12)
    # Maxwell contribution
    P_max = 0.5 * mu0 * c_val**2 * (1.0/a_i**2 - 1.0/a_e**2)
    P_pa = Pint + P_max
    return P_pa / 1e6   # MPa

def integrand_N2(r, lam_z, c_val, Theta_e, a_i, a_e, b):
    l2 = lam_sq(r, lam_z, b)
    om1 = omega1(r, Theta_e, a_i, a_e, c_val, lam_z, b)
    coeff = 2.0*lam_z**2 - 1.0/(l2 * lam_z**2) - l2
    return r * coeff * om1

def compute_N_scaled(lambda_i, lambda_z, zeta, c_val, Theta_e):
    a_i, a_e, b = geometry(lambda_i, lambda_z, zeta)
    P = compute_P(lambda_i, lambda_z, zeta, c_val, Theta_e) * 1e6   # convert back to Pa for N calculation
    # N2
    N2_int, _ = quad(integrand_N2, a_i, a_e, args=(lam_z, c_val, Theta_e, a_i, a_e, b),
                     epsabs=1e-12, epsrel=1e-12)
    N2 = 2.0 * np.pi * N2_int
    # N3: analytic expression from Eq. (102)
    _, k1, k2 = theta(a_i, Theta_e, a_i, a_e)   # any r gives same k1,k2
    term_a = (k1/Theta_0 - 1.0/lam_z**2) * np.log(a_e / a_i)
    term_b = k2/(2.0*Theta_0) * (np.log(a_e)**2 - np.log(a_i)**2)
    N3 = mu0 * np.pi * c_val**2 * (term_a + term_b)
    # total normal force (N)
    N_total = np.pi * a_i**2 * P + N2 + N3
    # scaled normal force (N/(π A_i^2)), in Pa, then MPa
    N_scaled_Pa = N_total / (np.pi * A_i**2)
    return N_scaled_Pa / 1e6   # MPa

def compute_M(tau, lambda_z, zeta, c_val, Theta_e):
    a_i, a_e, b = geometry(1.0, lambda_z, zeta)  # lambda_i=1 for torsion (no inflation)
    # temperature constants
    _, k1, k2 = theta(a_i, Theta_e, a_i, a_e)
    # M1: analytic
    term1 = k1/4.0 * (a_e**4 - a_i**4)
    term2 = k2/16.0 * (a_e**4 * (4.0*np.log(a_e) - 1.0) - a_i**4 * (4.0*np.log(a_i) - 1.0))
    M1 = mu_e * np.pi * tau * lambda_z**2 / Theta_0 * (term1 + term2)
    # M2 integral
    def integrand_M2(r):
        return r**2 * k1 * alpha_e * np.tanh(c_val**2 / (lambda_z * r**2 + b))
    M2_int, _ = quad(integrand_M2, a_i, a_e, epsabs=1e-12, epsrel=1e-12)
    M2 = mu_e * np.pi * tau * lambda_z**2 / Theta_0 * M2_int
    # M3 integral
    def integrand_M3(r):
        return r**2 * k2 * np.log(r) * alpha_e * np.tanh(c_val**2 / (lambda_z * r**2 + b))
    M3_int, _ = quad(integrand_M3, a_i, a_e, epsabs=1e-12, epsrel=1e-12)
    M3 = mu_e * np.pi * tau * lambda_z**2 / Theta_0 * M3_int
    M_total = M1 + M2 + M3   # in N·m (SI)
    return M_total

# --- parameter sets (hidden, but fixed for oracle) ---
BVP1_PARAMS = [
    # lambda_i, lambda_z, zeta, c, Theta_e
    (1.2, 1.0, 2.0, 1.0, 313),
    (1.5, 1.0, 2.0, 1.0, 333),
    (1.2, 1.2, 2.0, 1.0, 333),
    (1.5, 1.2, 2.0, 2.0, 313),
]

BVP2_PARAMS = [
    # tau (rad/m -> rad/mm: contract says rad/mm; keep SI: tau in rad/m -> convert to rad/mm? contract says tau rad/mm. We'll compute M with tau in SI (rad/m) then convert to? The contract says tau in rad/mm; we can output tau in rad/mm but our internal calculation uses SI, so we need to convert: tau_SI = tau_input * 1e3 (since rad/mm = rad/10^-3 m = 10^3 rad/m). So input to script is in rad/mm, we multiply by 1000 to get rad/m.
    # So we store here in rad/mm.
    (0.1, 1.0, 2.0, 1.0, 313),
    (0.2, 1.0, 2.0, 1.0, 313),
    (0.1, 1.2, 2.0, 1.0, 333),
    (0.2, 1.0, 3.0, 2.0, 313),
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['bvp1','bvp2'], required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    if args.mode == 'bvp1':
        rows = []
        for lam_i, lam_z, zeta, c_val, Th_e in BVP1_PARAMS:
            P = compute_P(lam_i, lam_z, zeta, c_val, Th_e)
            N = compute_N_scaled(lam_i, lam_z, zeta, c_val, Th_e)
            rows.append([lam_i, lam_z, zeta, c_val, Th_e, P, N])
        with open(args.out, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['lambda_i','lambda_z','zeta','c','Theta_e','P','N'])
            writer.writerows(rows)
    else:  # bvp2
        rows = []
        for tau_mm, lam_z, zeta, c_val, Th_e in BVP2_PARAMS:
            # convert tau from rad/mm to rad/m
            tau_SI = tau_mm * 1000.0
            M = compute_M(tau_SI, lam_z, zeta, c_val, Th_e)
            rows.append([tau_mm, lam_z, zeta, c_val, Th_e, M])
        with open(args.out, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['tau','lambda_z','zeta','c','Theta_e','M'])
            writer.writerows(rows)

if __name__ == '__main__':
    main()
