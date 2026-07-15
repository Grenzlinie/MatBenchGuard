#!/usr/bin/env python3
import sys, csv
import numpy as np
from scipy.optimize import brentq

R = 8.314
c = 12

E11 = -3.918e3          # J/mol
E22 =  5.887e3          # J/mol
S1_diff = 6.13          # J/(K mol)
E1mHc = -154.3e3        # J/mol  (negative, binding energy)
S2_diff = 44.17
E2mHc = 78.30e3         # J/mol

def a_c1(theta1, T):
    if theta1 <= 0 or theta1 >= 1:
        return np.inf
    pref = theta1 / (1 - theta1)
    return pref * np.exp(S1_diff / R) * np.exp((E1mHc + c * theta1 * E11) / (R * T))

def a_c2(ratio, T):
    if ratio <= 0 or ratio >= 1:
        return np.inf
    pref = ratio / (1 - ratio)
    return pref * np.exp(S2_diff / R) * np.exp((E2mHc + c * ratio * E22) / (R * T))

def solve_ratio(x, T):
    # feasible ratio range
    if x <= 1.0:
        lo, hi = 1e-12, 1.0 - 1e-12
    else:
        lo = x - 1.0 + 1e-12
        hi = 1.0 - 1e-12
    def f(ratio):
        th1 = x / (1.0 + ratio)
        if th1 <= 1e-12 or th1 >= 1.0 - 1e-12:
            return np.inf
        return np.log(a_c1(th1, T)) - np.log(a_c2(ratio, T))
    fa, fb = f(lo), f(hi)
    if fa * fb > 0:
        # Fallback: pick the boundary with smaller absolute residual
        return lo if abs(fa) < abs(fb) else hi
    return brentq(f, lo, hi, xtol=1e-12)

def main(outpath):
    temps = [1173, 1473, 1773, 2073, 2373]
    xs = np.arange(0.90, 1.9501, 0.05)
    rows = []
    for x in xs:
        for T in temps:
            ratio = solve_ratio(x, T)
            th1 = x / (1.0 + ratio)
            ac = a_c1(th1, T)
            rows.append([round(x, 4), int(T), float(ac)])
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'T', 'a_c'])
        writer.writerows(rows)

if __name__ == '__main__':
    main(sys.argv[1])
