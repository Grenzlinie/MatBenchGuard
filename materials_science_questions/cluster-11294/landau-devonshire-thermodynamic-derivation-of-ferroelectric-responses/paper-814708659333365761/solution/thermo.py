import math
import csv
import numpy as np
from scipy.optimize import newton

# Physical constants
EPS0 = 8.854187817e-12  # F/m

# PTO bulk Landau coefficients (Table II)
T0 = 479.0            # °C
# α1 = 3.8e5*(T - T0)  [J·m/C^2]   evaluated at room temperature (25°C)
RT = 25.0
alpha1_bulk = 3.8e5 * (RT - T0)   # constant for all TG, ≈ -1.7252e8
alpha11 = -7.3e7       # J·m^5/C^4
alpha111 = 2.6e8       # J·m^9/C^6

# Elastic compliances (Table II)
s11 = 8.0e-12          # m^2/N
s12 = -2.5e-12         # m^2/N
s_sum = s11 + s12       # 5.5e-12

# Electrostrictive coefficients (Table II)
Q11 = 0.089            # m^4/C^2
Q12 = -0.026           # m^4/C^2

# PTO TEC (constant, Table I)
alpha_PTO = 11.86e-6   # /°C

# --- TEC functions for each substrate (in /°C) ---

def alpha_Si(T_C):
    """Si TEC from Table I (units /°C)."""
    # T_C in °C
    return (3.725 * (1.0 - math.exp(-5.88e3 * (T_C + 149.0))) +
            5.548e-4 * (T_C + 273.0)) * 1e-6

def alpha_c_sapphire(T_C):
    """c-sapphire TEC."""
    return (8.026 + 8.17e-4 * T_C - 3.279 * math.exp(-2.91e-3 * T_C)) * 1e-6

def alpha_a_sapphire(T_C):
    """a-sapphire TEC (one of the anisotropic in-plane axes)."""
    return (7.419 + 6.43e-4 * T_C - 3.211 * math.exp(-2.59e-3 * T_C)) * 1e-6

# For anisotropic a-sapphire we need TECs along both in-plane axes.
# According to the paper's Table I and Refs. 17-19, a-sapphire has different
# in-plane TECs; we use the a-Al2O3 formula for one axis and c-Al2O3 for the other.

# MgO TEC (constant)
alpha_MgO = 13.47e-6

# --- Thermal strain integration ---

def compute_u_T_iso(alpha_sub, TG):
    """Compute u_T = integral_{25}^{TG} (alpha_PTO - alpha_sub(T)) dT
    using simple trapezoidal integration over T from 25 to TG at 0.1°C step."""
    if TG <= 25.0:
        return 0.0
    step = 0.1
    T = np.arange(25.0, TG + step, step)
    integrand = np.vectorize(lambda t: alpha_PTO - alpha_sub(t))(T)
    return np.trapz(integrand, T)

def compute_u_Ts_aniso(alpha_sub1, alpha_sub2, TG):
    """Compute u_T1 and u_T2 for anisotropic case."""
    if TG <= 25.0:
        return 0.0, 0.0
    step = 0.1
    T = np.arange(25.0, TG + step, step)
    integrand1 = np.vectorize(lambda t: alpha_PTO - alpha_sub1(t))(T)
    integrand2 = np.vectorize(lambda t: alpha_PTO - alpha_sub2(t))(T)
    u1 = np.trapz(integrand1, T)
    u2 = np.trapz(integrand2, T)
    return u1, u2

# --- Renormalized coefficients ---

def renormalized_coeffs_iso(u_T):
    """Return alpha1_star, alpha11_star for isotropic biaxial strain."""
    alpha1_star = alpha1_bulk - (2.0 * Q12 / s_sum) * u_T
    alpha11_star = alpha11 + (Q12**2 / s_sum)
    return alpha1_star, alpha11_star

def renormalized_coeffs_aniso(u_T1, u_T2):
    """Return alpha1_star, alpha11_star for anisotropic in-plane strain (eqs. 10,11)."""
    alpha1_star = alpha1_bulk - (Q12 / s_sum) * (u_T1 + u_T2)
    alpha11_star = alpha11 + (Q12**2 / s_sum)
    return alpha1_star, alpha11_star

# --- Polarization solver ---

def solve_P_zero_field(a1, a11, a111):
    """Solve for equilibrium P > 0 at E=0 using quadratic in P^2."""
    # Equation: P * (2*a1 + 4*a11*P^2 + 6*a111*P^4) = 0
    # Non-zero root: z = P^2 solves 6*a111*z^2 + 4*a11*z + 2*a1 = 0
    a = 6.0 * a111
    b = 4.0 * a11
    c = 2.0 * a1
    disc = b*b - 4.0*a*c
    if disc < 0:
        return 0.0
    # Positive root: (-b + sqrt(disc)) / (2*a) because a>0, b can be negative
    z = (-b + math.sqrt(disc)) / (2.0 * a)
    if z <= 0:
        return 0.0
    return math.sqrt(z)

def solve_P_field(a1, a11, a111, E, guess):
    """Solve dG/dP = 2*a1*P + 4*a11*P^3 + 6*a111*P^5 - E = 0 using Newton."""
    def f(P):
        return 2.0*a1*P + 4.0*a11*P**3 + 6.0*a111*P**5 - E
    def df(P):
        return 2.0*a1 + 12.0*a11*P**2 + 30.0*a111*P**4
    # Newton, suppressing warning for possible non-convergence in very small P
    try:
        P_sol = newton(f, guess, fprime=df, maxiter=100)
    except RuntimeError:
        # fallback: just return small positive
        P_sol = max(guess, 0.001)
    return max(P_sol, 0.0)

# --- Derived quantities ---

def epsilon33_from_P(P, a1, a11, a111):
    """Dielectric permittivity eq (5)."""
    denom = 2.0*a1 + 12.0*a11*P**2 + 30.0*a111*P**4
    if abs(denom) < 1e-30:
        return 1e6  # large but finite
    return 1.0 / (EPS0 * denom)

def d33_from_P_epsilon(P, eps33):
    """Piezoelectric coefficient eq (6)."""
    coeff = Q11 - (2.0 * s12 * Q12) / s_sum
    return 2.0 * EPS0 * eps33 * coeff * P

# --- Substrate definitions ---

def process_substrate(name, TG_range):
    """Compute CSV rows for a given substrate name over TG_range."""
    rows = []
    if name == 'Si':
        alpha_sub = alpha_Si
        iso = True
    elif name == 'c-sapphire':
        alpha_sub = alpha_c_sapphire
        iso = True
    elif name == 'MgO':
        alpha_sub = lambda T: alpha_MgO  # constant
        iso = True
    elif name == 'a-sapphire':
        iso = False
    else:
        raise ValueError(f"Unknown substrate {name}")

    for TG in TG_range:
        if iso:
            u_T = compute_u_T_iso(alpha_sub, TG)
            a1s, a11s = renormalized_coeffs_iso(u_T)
        else:
            u_T1, u_T2 = compute_u_Ts_aniso(alpha_a_sapphire, alpha_c_sapphire, TG)
            a1s, a11s = renormalized_coeffs_aniso(u_T1, u_T2)

        # Equilibrium polarization at E=0
        P0 = solve_P_zero_field(a1s, a11s, alpha111)
        # dielectric constant at E=0
        eps33_0 = epsilon33_from_P(P0, a1s, a11s, alpha111)
        # piezoelectric coefficient at E=0
        d33_0 = d33_from_P_epsilon(P0, eps33_0)

        # At E = 1000 kV/cm = 1e8 V/m
        E_field = 1e8
        # guess from zero-field P0 (if P0>0, else guess 0.1)
        guess = max(P0, 0.1)
        PE = solve_P_field(a1s, a11s, alpha111, E_field, guess)
        eps33_E = epsilon33_from_P(PE, a1s, a11s, alpha111)
        d33_E = d33_from_P_epsilon(PE, eps33_E)

        # Tunabilities
        if eps33_0 > 0:
            phi = (eps33_0 - eps33_E) / eps33_0 * 100.0
        else:
            phi = 0.0
        if d33_0 != 0.0:
            phi_prime = (1.0 - (eps33_E / eps33_0) * (PE / P0)) * 100.0 if P0 != 0 else 0.0
        else:
            phi_prime = 0.0

        rows.append({
            'TG': TG,
            'P': P0,
            'epsilon33': eps33_0,
            'd33': d33_0,
            'phi': phi,
            'phi_prime': phi_prime
        })
    return rows

def compute_and_write(substrate, filepath):
    """Compute and write CSV for given substrate."""
    TG_values = list(range(25, 801))  # 25 to 800 inclusive
    rows = process_substrate(substrate, TG_values)
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['TG', 'P', 'epsilon33', 'd33', 'phi', 'phi_prime'])
        writer.writeheader()
        writer.writerows(rows)
