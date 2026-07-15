#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: results.json ===
python3 << 'PYEOF'
import json
import numpy as np
from scipy.optimize import fsolve

V = 1.0
kB = 1.0
L = 0.1
Tc = 0.8224 * V / kB
N = 1  # system size factor (not specified, assume 1)

def solve_zeroth(T):
    exp1 = np.exp(-6 * V / (kB * T))
    exp2 = np.exp(-2 * V / (kB * T))

    def equations(vars):
        b, g, h, r = vars
        b = np.clip(b, 1e-15, None)
        g = np.clip(g, 1e-15, None)
        h = np.clip(h, 1e-15, None)
        r = np.clip(r, 0.0, 1.0)

        a = b * g * exp1 / h
        c = b * h * exp2 / (g * exp1)
        d = b * h**2 / (g**2 * exp1)
        e = g**3 * exp1 / h**2
        f = g**2 * exp2 / h

        # Eq. (2)
        eq2 = 4*a + 9*b + 6*c + d + 3*e + 6*f + 3*g - 1.0
        # Eq. (3)
        eq3 = a + 3*b + 3*c + d + e + 3*f + 3*g + h - 1.0
        # Eq. (4)
        eq4 = a + 2*b + c + e + 2*f + g - (1.0 - r) / 3.0
        # Order condition (17 last)
        lpart = np.log((1 - r)**2 / (r * (2 + r))) - (4/3) * np.log(f / c)
        return [eq2, eq3, eq4, lpart]

    if T >= Tc:
        init = [0.01, 0.1, 0.3, 0.001]  # b, g, h, r
    else:
        init = [0.001, 0.9, 0.001, 0.99]

    sol = fsolve(equations, init, maxfev=2000, xtol=1e-12)
    b, g, h, r = sol
    b = max(b, 1e-15)
    g = max(g, 1e-15)
    h = max(h, 1e-15)
    r = max(0.0, min(1.0, r))

    a = b * g * exp1 / h
    c = b * h * exp2 / (g * exp1)
    d = b * h**2 / (g**2 * exp1)
    e = g**3 * exp1 / h**2
    f = g**2 * exp2 / h

    return dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, r=r)

def aux_coeffs(sol):
    a = sol['a']; b = sol['b']; c = sol['c']; d = sol['d']
    e = sol['e']; f = sol['f']; g = sol['g']; h = sol['h']; r = sol['r']

    # Eq.(22)
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

    # Common subexpressions
    denA = 3*x3*(x1*y2 - x2*y1) + 3*z1*(x2*y3 - 3*x3*y2) + (x3 - 2*z3)*(x1*y3 - 3*x3*y1)
    numA = -3*x3*(x1*y4 - x4*y1) + 3*z1*(3*x3*y4 - x4*y3) + (z4 - z5)*(x1*y3 - 3*x3*y1)
    term1_A = 3*x3*y4 - x4*y3
    term2_A = x2*y3 - 3*x3*y2
    A = (term1_A - term2_A * numA / denA) / (x1*y3 - 3*x3*y1)

    # B1
    B1 = -(27.0/2) * z4 / (4*(1-r)*(2+r) + 27*z2)

    # B2, B3 (same denominator)
    denB = z2 * denA
    numB2_1 = -(x1*y3 - 3*x3*y1)*(x3*z5 - z3*(z4+z5))
    numB2_2 = z2*(x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
    numB2_3 = -(z4+2*z5)*(x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
    B2 = (numB2_1 + numB2_2 + numB2_3) / denB

    numB3_1 = -(x1*y3 - 3*x3*y1)*(x3*z4 - 2*z3*z5)
    numB3_2 = -2*z2*(x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
    numB3_3 = -(z4+2*z5)*(x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
    B3 = (numB3_1 + numB3_2 + numB3_3) / denB

    # H
    numH = -x1*y4 + x4*y1 - (x1*y2 - x2*y1) * numA / denA
    H = numH / (x1*y3 - 3*x3*y1)

    # Derived coefficients
    C1 = 0.5 - B1
    C2 = A - B3
    C3 = 1 - 2*A - 2*B2 + B3
    Dc = 1 - 2*A - B2 + B3
    Ec = 3*A + B2 - B3 + H
    F1 = 0.5 + B1
    F2 = -2*A + B3 - H
    F3 = -1 + 4*A + 2*B2 - B3 + 2*H
    G1 = -B1
    G2 = 1 - A - B2 - H
    G3 = 2*A - B3 + 2*H

    return (C1, C2, C3, Dc, Ec, F1, F2, F3, G1, G2, G3, B2, B3, H)

def compute_k(T, sol):
    a,b,c,d,e,f,g,h,r = [sol[k] for k in ['a','b','c','d','e','f','g','h','r']]
    (C1, C2, C3, Dc, Ec, F1, F2, F3, G1, G2, G3, B2, B3, H) = aux_coeffs(sol)
    k1 = 2 * (c * C1 + f * F1) * N * L * L / (kB * T)
    k2 = 2 * (b * (3*B2 + B3) + d * Dc + e * Ec + g * (3*G2 + G3)) * N * L * L / (kB * T)
    return k1, k2, r

T_high = 0.9 * Tc
T_low = 0.4 * Tc

sol_high = solve_zeroth(T_high)
sol_low = solve_zeroth(T_low)

k1_h, k2_h, r_h = compute_k(T_high, sol_high)
k1_l, k2_l, r_l = compute_k(T_low, sol_low)

results = {
    "k1_highT": float(k1_h),
    "k2_highT": float(k2_h),
    "r_highT": float(r_h),
    "k1_lowT": float(k1_l),
    "k2_lowT": float(k2_l),
    "r_lowT": float(r_l)
}

with open('/app/outputs/results.json', 'w') as fp:
    json.dump(results, fp, indent=2)
PYEOF
