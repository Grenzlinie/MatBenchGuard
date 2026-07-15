#!/usr/bin/env python3
"""Compute zeroth-order AB3 superlattice order parameter and induced anisotropy
constants k1, k2 from the quasi-chemical quadruplet approximation (McGlashan
theory + linearised directional order), using the paper's equations (17), (21),
(22), (24).

Usage:
    python3 compute_results.py /app/outputs/results.json
"""

import sys
import json
import numpy as np
from scipy.optimize import fsolve

# Fixed parameters
V = 1.0
kB = 1.0
L = 0.1
Lprime = 0.1   # same as L (as specified)
N = 1.0       # per lattice site
beta = np.array([1.0, 0.0, 0.0])  # [100]

Tc = 0.8224   # V/kB
T_high = 0.9 * Tc
T_low = 0.4 * Tc

def solve_zeroth(V, kB, T):
    """Solve McGlashan's AB3 zeroth-order equations (Eq. 17).
    Returns dict with 'r','a','b','c','d','e','f','g','h', or None on failure.
    """
    VkT = V / (kB * T)
    E2 = np.exp(-2 * VkT)
    E6 = E2 ** 3

    def eqs(vars):
        r, a, b, c, d, e, f, g, h = vars
        eq0 = 4*a + 9*b + 6*c + d + 3*e + 6*f + 3*g - 1.0
        eq1 = a + 3*b + 3*c + d + e + 3*f + 3*g + h - 1.0
        eq2 = a + 2*b + c + e + 2*f + g - (1.0 - r) / 3.0
        eq3 = a*a * d / (b**3) - E6
        eq4 = e * h*h / (g**3) - E6
        eq5 = a * h / (b * g) - E6
        eq6 = a * c / (b**2) - E2
        eq7 = f * h / (g**2) - E2
        # avoid division by zero if r=0; start away from 0
        denom = r * (2.0 + r)
        lhs = (1.0 - r)**2 / denom
        rhs = (f / c)**(4/3) if c > 0 and f > 0 else 0.0
        eq8 = lhs - rhs
        return [eq0, eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8]

    # Several initial guesses to improve convergence
    guesses = [
        [0.3, 0.04, 0.08, 0.12, 0.1, 0.1, 0.12, 0.08, 0.36],   # moderate r
        [0.7, 0.01, 0.05, 0.1, 0.2, 0.15, 0.1, 0.05, 0.34],
        [0.95, 0.001, 0.01, 0.05, 0.1, 0.2, 0.1, 0.02, 0.519],
    ]

    for guess in guesses:
        try:
            sol, infodict, ier, msg = fsolve(eqs, guess, full_output=True, xtol=1e-12, maxfev=2000)
            if ier == 1:
                r, a, b, c, d, e, f, g, h = sol
                # check constraints loosely
                if r > 0.0 and r < 1.0 and all(v > 0 for v in (a,b,c,d,e,f,g,h)):
                    return {
                        'r': float(r),
                        'a': float(a), 'b': float(b), 'c': float(c),
                        'd': float(d), 'e': float(e), 'f': float(f),
                        'g': float(g), 'h': float(h)
                    }
        except Exception:
            continue
    raise RuntimeError(f"Zeroth-order solver failed for T={T}")


def compute_aux_coeffs(r, a, b, c, d, e, f, g, h):
    """Compute auxiliary coefficients from Eqs. (21) and (22)."""
    # Eq. (22)
    x1 = 4*a - 6*c - 2*d + 9*e + 12*f + 3*g
    x2 = 3*b + 4*c + d - 3*e - 4*f - g
    x3 = e + 2*f + g
    x4 = 2*c + d - 2*f - g
    y1 = a - 3*c - 2*d + 3*e + 6*f + 3*g
    y2 = b + 2*c + d - e - 2*f - g
    y3 = e + 3*f + 3*g + h
    y4 = c + d - f - g
    z1 = a - c + 3*e + 4*f + g
    z2 = -b - c - f - g
    z3 = b + c - e - f
    z4 = c - f
    z5 = f + g

    # Common denominator
    denom_common = 3*x3*(x1*y2 - x2*y1) + 3*z1*(x2*y3 - 3*x3*y2) + (x3 - 2*z3)*(x1*y3 - 3*x3*y1)
    if abs(denom_common) < 1e-14:
        raise ValueError("Denominator common too small")

    # Numerator factor 1
    num1 = -3*x3*(x1*y4 - x4*y1) + 3*z1*(3*x3*y4 - x4*y3) + (z4 - z5)*(x1*y3 - 3*x3*y1)

    x1y3_3x3y1 = x1*y3 - 3*x3*y1
    if abs(x1y3_3x3y1) < 1e-14:
        raise ValueError("x1y3-3x3y1 too small")

    # R
    R = (-6*(1-r)*(2+r)*z4) / (4*(1-r)*(2+r) + 27*z2)

    # A
    A = (3*x3*y4 - x4*y3 - (x2*y3 - 3*x3*y2) * num1 / denom_common) / x1y3_3x3y1

    # B1
    B1 = -27/2 * z4 / (4*(1-r)*(2+r) + 27*z2)

    # B2
    term1_B2 = -(x1y3_3x3y1) * (x3*z5 - z3*(z4+z5))
    term2_B2 = z2 * (x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
    term3_B2 = -(z4+2*z5) * (x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
    B2 = (term1_B2 + term2_B2 + term3_B2) / z2 / denom_common

    # B3
    term1_B3 = -(x1y3_3x3y1) * (x3*z4 - 2*z3*z5)
    term2_B3 = -2*z2 * (x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
    term3_B3 = -(z4+2*z5) * (x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
    B3 = (term1_B3 + term2_B3 + term3_B3) / z2 / denom_common

    # H
    num2 = -3*x3*(x1*y4 - x4*y1) + 3*z1*(3*x3*y4 - x4*y3) + (z4 - z5)*(x1y3_3x3y1)
    H = (-x1*y4 + x4*y1 - (x1*y2 - x2*y1)*num2/denom_common) / x1y3_3x3y1

    # Derived coefficients (Eq. 22)
    C1 = 0.5 - B1
    C2 = A - B3
    C3 = 1 - 2*A - 2*B2 + B3
    D = 1 - 2*A - B2 + B3
    E = 3*A + B2 - B3 + H
    F1 = 0.5 + B1
    F2 = -2*A + B3 - H
    F3 = -1 + 4*A + 2*B2 - B3 + 2*H
    G1 = -B1
    G2 = 1 - A - B2 - H
    G3 = 2*A - B3 + 2*H

    return (R, A, B1, B2, B3, H, C1, C2, C3, D, E, F1, F2, F3, G1, G2, G3)


def compute_k1k2(r, a, b, c, d, e, f, g, h, T, L, Lprime, N):
    """Compute k1 and k2 from Eq. (24)."""
    coeffs = compute_aux_coeffs(r, a, b, c, d, e, f, g, h)
    _, _, _, B2, B3, _, C1, _, _, D, E, F1, _, _, _, G2, G3 = coeffs
    k1 = 2.0 * (c*C1 + f*F1) * N * L * Lprime / (kB * T)
    k2 = 2.0 * (b*(3*B2 + B3) + d*D + e*E + g*(3*G2 + G3)) * N * L * Lprime / (kB * T)
    return k1, k2


def main():
    out_path = sys.argv[1]

    zeroth_high = solve_zeroth(V, kB, T_high)
    zeroth_low  = solve_zeroth(V, kB, T_low)

    r_high = zeroth_high['r']
    r_low  = zeroth_low['r']

    k1_high, k2_high = compute_k1k2(r_high, **{k: zeroth_high[k] for k in ['a','b','c','d','e','f','g','h']},
                                     T=T_high, L=L, Lprime=Lprime, N=N)
    k1_low, k2_low   = compute_k1k2(r_low, **{k: zeroth_low[k] for k in ['a','b','c','d','e','f','g','h']},
                                     T=T_low, L=L, Lprime=Lprime, N=N)

    results = {
        "k1_highT": k1_high,
        "k2_highT": k2_high,
        "r_highT": r_high,
        "k1_lowT": k1_low,
        "k2_lowT": k2_low,
        "r_lowT": r_low
    }

    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Written results to {out_path}")


if __name__ == "__main__":
    main()
