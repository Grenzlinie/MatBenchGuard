#!/usr/bin/env python3
import json, math, sys

# Boltzmann constant in erg/K (cgs)
kB = 1.380649e-16

# ---------- input data (lattice parameter, Debye temperature, Grüneisen parameter) ----------
# a_cm = half the cubic lattice parameter (cm)  = (2a from Table 1) / 2
ne = {
    'name': 'Ne',
    'a_cm': 2.227e-8,
    'theta_D': 69.50,
    'gamma': 1.72,
    'alpha_prime_a8': -147.573,
    'A': 862.105,
    'lambda_df_a7': 5.0841,
    'lambda_d2f_a6': -54.0989,
    'lambda_d3f_a5': 575.654,
    'C': -12973.23,
    'D': 195225.10
}
ar = {
    'name': 'Ar',
    'a_cm': 2.656e-8,
    'theta_D': 81.50,
    'gamma': 2.74,
    'alpha_prime_a8': -327.219,
    'A': 2158.472,
    'lambda_df_a7': 2.5720,
    'lambda_d2f_a6': -28.9743,
    'lambda_d3f_a5': 326.401,
    'C': -34387.39,
    'D': 547837.74
}
kr = {
    'name': 'Kr',
    'a_cm': 2.823e-8,
    'theta_D': 64.87,
    'gamma': 2.51,
    'alpha_prime_a8': -294.766,
    'A': 2379.691,
    'lambda_df_a7': -0.7682,
    'lambda_d2f_a6': 10.3269,
    'lambda_d3f_a5': -138.809,
    'C': -45235.86,
    'D': 859894.35
}
xe = {
    'name': 'Xe',
    'a_cm': 3.065e-8,
    'theta_D': 55.00,
    'gamma': 2.87,
    'alpha_prime_a8': -382.827,
    'A': 2932.382,
    'lambda_df_a7': 7.3614,
    'lambda_d2f_a6': -91.7506,
    'lambda_d3f_a5': 1143.554,
    'C': -51687.25,
    'D': 911058.63
}

elements = [ne, ar, kr, xe]

# ---------- computation ----------
def compute_properties(p):
    a_cm = p['a_cm']
    theta = p['theta_D']
    gamma = p['gamma']

    # zero-point vibrational terms (CGS: erg/cm -> dyne/cm)
    kB_theta = kB * theta
    t1 = kB_theta * gamma / (a_cm * a_cm)          # K_B θ_D γ / a^2
    t2 = kB_theta * (gamma ** 2) / (a_cm * a_cm)   # K_B θ_D γ² / a^2
    t3 = kB_theta * (gamma ** 3) / (a_cm * a_cm)   # K_B θ_D γ³ / a^2

    alpha = p['alpha_prime_a8']
    A = p['A']
    lam_df = p['lambda_df_a7']
    lam_d2f = p['lambda_d2f_a6']
    lam_d3f = p['lambda_d3f_a5']
    C = p['C']
    D = p['D']

    # second‑order elastic constants (CGS: dyne/cm²)
    # all at P = 0  ->  aP terms vanish
    inv2a = 1.0 / (2.0 * a_cm)
    C11 = inv2a * (
        6.7862 * alpha
        + 2.0 * A
        + 1.6875 * t1
        - 20.439 * lam_df
        + 1.125 * t2
    )
    C12 = inv2a * (
        2.9302 * alpha
        + A
        - 20.439 * lam_df
        - 0.2812 * t1
        + 1.125 * t2
    )
    C44 = inv2a * (
        2.9292 * alpha
        + A
        - 0.10546 * t1
    )

    # isothermal bulk modulus and shear moduli (dyne/cm²)
    K_T = (C11 + 2.0 * C12) / 3.0
    C_S = (C11 - C12) / 2.0

    # ---------- first pressure derivatives (dimensionless) ----------
    # Using Eqs. (22)-(24) at P = 0
    dK_dP = -1.0 / (18.0 * a_cm * K_T) * (
        -139.1084 * alpha
        - 12.0 * A
        + 4.0 * C
        + 827.721 * lam_df
        - 130.052 * lam_d2f
        + 7.875 * t1
        + 3.375 * t2
    )

    dC_S_dP = -1.0 / (12.0 * a_cm * K_T) * (
        -12.5748 * alpha
        + 6.0 * A
        + C
        - 41.832 * lam_df
        - 10.838 * lam_d2f
        - 5.625 * t1
    )

    dC44_dP = -1.0 / (6.0 * a_cm * K_T) * (
        -27.5532 * alpha
        - 1.375 * A
        + C
        + 55.4582 * lam_df
        - 10.8394 * lam_d2f
        + 0.21093 * t1
    )

    # ---------- second pressure derivatives (dyne/cm²)⁻¹ ----------
    # Eq. (27)
    d2K_dP2 = 1.0 / (18.0 * a_cm * K_T * K_T) * (
        dK_dP * (
            -139.108 * alpha
            - 12.0 * A
            + 4.0 * C
            - 827.721 * lam_df
            - 130.059 * lam_d2f
            + 7.875 * t1
            + 3.375 * t2
        )
        + (
            442.612 * alpha
            - 3116.646 * lam_df
            + 12.0 * A
            - 4.0 * C
            + (4.0 / 3.0) * D
            + 736.957 * lam_d2f
            - 81.759 * lam_d3f
            - 7.5937 * t1
            - 6.4687 * t2
            - 3.375 * t3
        )
    )

    # Eq. (28)
    d2C_S_dP2 = 1.0 / (12.0 * a_cm * K_T * K_T) * (
        dK_dP * (
            -12.5748 * alpha
            + 6.0 * A
            + C
            - 41.832 * lam_df
            - 10.838 * lam_d2f
            - 5.0625 * t1
        )
        + (
            18.7572 * alpha
            - 8.0 * A
            - 2.0 * C
            + D / 3.0
            + 132.378 * lam_df
            - 16.106 * lam_d2f
            - 10.223 * lam_d3f
            + 3.375 * t3
        )
    )

    # Eq. (29)
    d2C44_dP2 = 1.0 / (6.0 * a_cm * K_T * K_T) * (
        dK_dP * (
            -27.5533 * alpha
            - 1.375 * A
            + C
            + 55.4582 * lam_df
            - 10.8394 * lam_d2f
            + 0.21093 * t1
        )
        + (
            83.499 * alpha
            - 0.715 * A
            + 0.625 * C
            + D / 3.0
            + 307.559 * lam_df
            + 41.9464 * lam_d2f
            - 5.1089 * lam_d3f
            - 0.140625 * t1
        )
    )

    # ---------- convert to required units ----------
    # CGS dyne/cm²  →  GPa  (1 dyne/cm² = 1e‑10 GPa)
    K_T_gpa = K_T * 1e-10
    C_S_gpa = C_S * 1e-10
    C44_gpa = C44 * 1e-10

    # second derivatives in (dyne/cm²)⁻¹  →  GPa⁻¹  (1 (dyne/cm²)⁻¹ = 1e10 GPa⁻¹)
    d2K_gpa = d2K_dP2 * 1e10
    d2C_S_gpa = d2C_S_dP2 * 1e10
    d2C44_gpa = d2C44_dP2 * 1e10

    # first derivatives are dimensionless; no conversion

    return {
        'K_T': round(K_T_gpa, 8),
        'C_S': round(C_S_gpa, 8),
        'C_44': round(C44_gpa, 8),
        'dK_T_dP': round(dK_dP, 8),
        'dC_S_dP': round(dC_S_dP, 8),
        'dC44_prime_dP': round(dC44_dP, 8),
        'd2K_T_dP2': round(d2K_gpa, 8),
        'd2C_S_dP2': round(d2C_S_gpa, 8),
        'd2C44_prime_dP2': round(d2C44_gpa, 8)
    }

# assemble output
output = {}
for el in elements:
    output[el['name']] = compute_properties(el)

json.dump(output, sys.stdout, indent=2)
