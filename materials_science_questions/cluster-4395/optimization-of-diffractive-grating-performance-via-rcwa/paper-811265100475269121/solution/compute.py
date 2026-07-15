#!/usr/bin/env python3
"""Compute BMDM coupling coefficients, grating period, and insertion losses."""
import sys
import math
import json

# Constants from the paper (all in SI units)
n1 = 3.473
n2 = 1.444
lambda0 = 1550e-9  # m
w = 600e-9         # m
d = 250e-9         # m
r = 136.13e-9      # m
t = r              # grating teeth depth = r

# Effective indices (given)
n_eff = [3.32, 2.83, 1.9]  # TE0, TE1, TE2
n_eff_single = 2.93

# Derived quantities
k0 = 2*math.pi / lambda0
beta = [2*math.pi * neff / lambda0 for neff in n_eff]
beta_single = 2*math.pi * n_eff_single / lambda0

# ϱ_m and γ_m
rho = []
gamma = []
for neff in n_eff:
    rho_val = k0 * math.sqrt(n1**2 - neff**2)
    gamma_val = k0 * math.sqrt(neff**2 - n2**2)
    rho.append(rho_val)
    gamma.append(gamma_val)

rho_single = k0 * math.sqrt(n1**2 - n_eff_single**2)
gamma_single = k0 * math.sqrt(n_eff_single**2 - n2**2)

# sinc function (defined as sin(pi*x)/(pi*x))
def sinc(x):
    if x == 0:
        return 1.0
    return math.sin(math.pi*x) / (math.pi*x)

# Eq.13: self-coupling coefficient ζ_m^ν
def zeta(m, nu):
    num = rho[m]**2 * sinc(nu/2.0)
    denom = 2 * beta[m] * (w + 2/gamma[m])
    return (num / denom) * (math.sinh(gamma[m]*t) / gamma[m]) * math.exp(-gamma[m]*r)

# Eq.14: cross-coupling coefficient κ_m^ν
def kappa(m, nu):
    num = rho[m] * rho_single * sinc(nu/2.0)
    denom = math.sqrt(beta[m] * beta_single * (w + 2/gamma[m]) * (d + 2/gamma_single))
    delta_gamma = gamma_single - gamma[m]
    if abs(delta_gamma) < 1e-12:
        factor = t/2.0
    else:
        factor = math.sinh(delta_gamma * t / 2.0) / delta_gamma
    return (num / denom) * factor * math.exp(-(gamma_single + gamma[m]) * r / 2.0)

# Eq.17: varsigma_m
def varsig(m):
    num = rho[m] * rho_single * (gamma[m] + gamma_single) * math.exp(-gamma_single * r)
    denom = (rho[m]**2 + gamma_single**2) * math.sqrt(beta[m] * beta_single * (w + 2/gamma[m]) * (d + 2/gamma_single))
    return num / denom

# Eq.19: iota^ν
def iota(nu):
    num = rho_single**2 * sinc(nu/2.0)
    denom = 2 * beta_single * (d + 2/gamma_single)
    return (num / denom) * (math.sinh(gamma_single * t) / gamma_single) * math.exp(-gamma_single * r)

# Eq.20: varpi_m (not used in IL, but compute for completeness)
def varpi(m):
    num = rho[m] * rho_single * (gamma[m] + gamma_single) * math.exp(-gamma[m] * r)
    denom = (rho_single**2 + gamma[m]**2) * math.sqrt(beta[m] * beta_single * (w + 2/gamma[m]) * (d + 2/gamma_single))
    return num / denom

# Compute needed coefficients
zeta_2_0 = zeta(2, 0)       # m=2, nu=0
kappa_1_0 = kappa(1, 0)     # m=1, nu=0
kappa_2_1 = kappa(2, 1)     # m=2, nu=1
varsigma_1 = varsig(1)
iota_0 = iota(0)

kappa_prime_1 = kappa_1_0 + varsigma_1

# Grating period Λ (Eq.32)
Lambda = 1.0 / ((n_eff[2] + n_eff_single)/lambda0 + (zeta_2_0 + iota_0)/(2*math.pi))
Lambda_nm = Lambda * 1e9

# Global minimum period Λ_min (Eq.33) using 328 nm as max period
one_over_328nm = 1.0 / (328e-9)
term = (rho[2]**2) / (4*beta[2]*gamma[2]*(w + 2/gamma[2]))
term_single = (rho_single**2) / (4*beta_single*gamma_single*(d + 2/gamma_single))
Lambda_min = 1.0 / (one_over_328nm + (1.0/(2*math.pi)) * term * term_single)
Lambda_min_nm = Lambda_min * 1e9

# Coupling length L = 34 * Lambda_min
L = 34 * Lambda_min

# Insertion loss IL1 (Eq.31) with phase matching Δβ1=0 → s1 = |kappa_prime_1|
s1 = abs(kappa_prime_1)
eta1 = (kappa_prime_1**2 / s1**2) * (math.sin(s1 * L)**2)   # = sin^2(s1*L)
IL1_dB = 10 * math.log10(eta1) if eta1 > 1e-15 else -150.0

# Insertion loss IL2 (Eq.27) with Δβ2=0 → s2 = |kappa_2_1|
s2 = abs(kappa_2_1)
eta2 = (kappa_2_1**2 * math.sinh(s2 * L)**2) / (s2**2 * math.cosh(s2 * L)**2)
IL2_dB = 10 * math.log10(eta2) if eta2 > 1e-15 else -150.0

def output_coefficients():
    coeffs = {
        "zeta": {
            "m2_nu0": zeta_2_0
        },
        "kappa": {
            "m1_nu0": kappa_1_0,
            "m2_nu1": kappa_2_1
        },
        "iota": {
            "nu0": iota_0
        },
        "varsigma": {
            "m1": varsigma_1
        },
        "varpi": {
            "m1": varpi(1)
        }
    }
    json.dump(coeffs, sys.stdout, indent=2)

def output_grating_period():
    print(f"{Lambda_nm:.2f}")

def output_insertion_losses():
    print("IL1_dB,IL2_dB")
    print(f"{IL1_dB:.2f},{IL2_dB:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: compute.py --coefficients|--grating_period|--insertion_losses")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "--coefficients":
        output_coefficients()
    elif cmd == "--grating_period":
        output_grating_period()
    elif cmd == "--insertion_losses":
        output_insertion_losses()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
