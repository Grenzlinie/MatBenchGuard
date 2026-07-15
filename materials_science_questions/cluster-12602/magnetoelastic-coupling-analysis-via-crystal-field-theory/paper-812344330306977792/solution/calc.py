#!/usr/bin/env python3
"""Reference oracle computation for the exchange-striction Landau model."""

import sys
import math
import json
import csv

# --- Physical constants (cgs) used in the paper ---
k_B = 1.380649e-16   # erg/K
mu_B = 9.274e-21     # erg/G  (1 G = 1e-4 T)

# --- Material parameters from the paper ---
B0 = 1.5e12          # erg/cm^3
n  = 2.4e22          # cm^{-3}
gamma   = 2.0e-13    # erg
epsilon = -5.0e-10   # erg
Tc0 = 121.0          # K

# --- Unit conversion ---
GPa_to_erg_cm3 = 1.0e10   # 1 GPa = 1e10 dyn/cm^2 = 1e10 erg/cm^3


def Tc_P(P_erg):
    """Pressure-dependent Curie temperature (Eq. 5)."""
    term1 = gamma / (2.0 * k_B * B0) * P_erg
    term2 = epsilon / (12.0 * k_B * B0 * B0) * P_erg * P_erg
    return Tc0 - term1 + term2


def gamma_star(P_erg):
    """Effective first-order coupling (Eq. 6)."""
    return gamma - epsilon * P_erg / (3.0 * B0)


def B_coeff(T, P_erg):
    """Cubic coefficient B (Eq. 6)."""
    tc = Tc_P(P_erg)
    gs = gamma_star(P_erg)
    term_a = (1.0/3.0) * (tc / T)**3
    term_b = (n / (8.0 * k_B * T * B0)) * gs * gs
    return term_a - term_b


def C_coeff(T, P_erg):
    """Quintic coefficient C (Eq. 7)."""
    tc = Tc_P(P_erg)
    gs = gamma_star(P_erg)
    term1 = (1.0/8.0) * (n / (k_B * T * B0)) * (tc / T)**2 * gs * gs
    term2 = (1.0/64.0) * (n * n * epsilon / (k_B * T * B0 * B0)) * gs * gs
    term3 = (2.0/15.0) * (tc / T)**5
    return term1 - term2 - term3


# ---------------------------------------------------------------------
# B_coefficient.csv output
# ---------------------------------------------------------------------
def write_b_csv(outpath):
    pressures_GPa = [0.0, 0.5, 1.0, 1.5]
    rows = []
    for P_GPa in pressures_GPa:
        P_erg = P_GPa * GPa_to_erg_cm3
        T = Tc_P(P_erg)
        B = B_coeff(T, P_erg)
        rows.append({"pressure_GPa": P_GPa, "B_value": B})

    with open(outpath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["pressure_GPa", "B_value"])
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------
# tricritical point (solve B(Tc(P),P)=0)
# ---------------------------------------------------------------------
def write_tricritical(outpath):
    def f(P_erg):
        T = Tc_P(P_erg)
        return B_coeff(T, P_erg)

    # bisection on P_erg (corresponds to 0..5 GPa)
    lo = 0.0
    hi = 5.0 * GPa_to_erg_cm3  # 5 GPa
    # ensure sign change
    f_lo = f(lo)
    f_hi = f(hi)
    if f_lo * f_hi > 0:
        raise ValueError("B(Tc(P),P) does not change sign in [0,5] GPa")

    for _ in range(200):
        mid = (lo + hi) / 2.0
        f_mid = f(mid)
        if abs(f_mid) < 1e-12:
            break
        if f_lo * f_mid < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid

    P_erg = (lo + hi) / 2.0
    P_GPa = P_erg / GPa_to_erg_cm3
    T_t = Tc_P(P_erg)

    data = {"P_t_GPa": round(P_GPa, 6), "T_t_K": round(T_t, 3)}
    with open(outpath, "w") as f:
        json.dump(data, f, indent=2)


# ---------------------------------------------------------------------
# wing critical point at P=1.4 GPa
# ---------------------------------------------------------------------
def write_wing(outpath):
    P_GPa = 1.4
    P_erg = P_GPa * GPa_to_erg_cm3
    tc = Tc_P(P_erg)

    # check that B(Tc,P) < 0 and C(Tc,P) > 0 (should hold)
    B_tc = B_coeff(tc, P_erg)
    C_tc = C_coeff(tc, P_erg)
    if B_tc >= 0 or C_tc <= 0:
        raise ValueError("B or C sign unexpected at Tc(P=1.4)")

    # define A = (T - tc)/T, target = (9/20) * B^2 / C
    def target_diff(T):
        A_val = (T - tc) / T
        Bv = B_coeff(T, P_erg)
        Cv = C_coeff(T, P_erg)
        if Cv <= 0:
            return float('inf')  # guard
        return A_val - (9.0/20.0) * (Bv * Bv) / Cv

    # bisection on T (above Tc, where A>0 and B still negative, C positive)
    T_lo = tc       # here A=0 and diff = -(9/20)*B^2/C < 0
    T_hi = tc + 100.0  # large enough so diff becomes positive
    # find an upper bound where target_diff > 0
    for step in range(200):
        if target_diff(T_hi) > 0:
            break
        T_hi += 50.0
    else:
        raise ValueError("Could not bracket wing critical temperature")

    for _ in range(200):
        T_mid = (T_lo + T_hi) / 2.0
        if target_diff(T_mid) > 0:
            T_hi = T_mid
        else:
            T_lo = T_mid
    T_cr = (T_lo + T_hi) / 2.0

    B_cr = B_coeff(T_cr, P_erg)
    C_cr = C_coeff(T_cr, P_erg)

    # Eq. (8): m_cr^2 = -(3/10) B/C,  h_cr = (6/25)(B^2/C)*m_cr
    m_cr = math.sqrt(-0.3 * B_cr / C_cr)
    h_cr = (6.0/25.0) * (B_cr * B_cr / C_cr) * m_cr

    # convert reduced field to H in Tesla: H = h * k * T / mu -> yields Gauss, then /1e4 -> T
    H_Gauss = h_cr * k_B * T_cr / mu_B
    H_Tesla = H_Gauss / 1.0e4

    data = {
        "pressure_GPa": P_GPa,
        "T_cr_K": round(T_cr, 3),
        "H_cr_T": round(H_Tesla, 4),
        "m_cr": round(m_cr, 4)
    }
    with open(outpath, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: calc.py <mode> <output_file>")
        sys.exit(1)
    mode = sys.argv[1]
    outfile = sys.argv[2]

    if mode == "b_csv":
        write_b_csv(outfile)
    elif mode == "tricritical":
        write_tricritical(outfile)
    elif mode == "wing":
        write_wing(outfile)
    else:
        print("Unknown mode")
        sys.exit(1)
