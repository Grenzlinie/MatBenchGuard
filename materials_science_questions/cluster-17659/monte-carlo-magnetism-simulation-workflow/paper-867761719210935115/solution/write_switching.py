#!/usr/bin/env python3
import sys
import json
import math

def switching_field(L):
    # model parameters (identical to write_lifetime.py)
    Tc_J = 1.1346
    T = 0.8 * Tc_J
    beta = 1.0 / T
    Xi_over_JI2 = 0.92
    J_I = 0.5
    Xi = Xi_over_JI2 * (J_I ** 2)
    C = beta * Xi
    A = 0.37

    # target Gamma such that mean clock lifetime = 288.539 MCSS (so P(switch) = 0.5 for tw=200)
    target_tau_clock = 200.0 / math.log(2.0)  # ~288.539
    target_tau_I = target_tau_clock / 3.0
    L2 = L * L
    target_Gamma = 1.0 / (L2 * target_tau_I)

    # solve for H_I (x) in: A * x^3 * exp(-C/x) = target_Gamma
    # use bisection
    def f(x):
        return A * (x**3) * math.exp(-C / x) - target_Gamma

    lo, hi = 0.001, 2.0  # reasonable bounds
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    x = (lo + hi) / 2.0  # H_I = H/2
    H_sw = 2.0 * x  # |H|/J
    return H_sw

if __name__ == "__main__":
    outpath = sys.argv[1]
    sizes = [8, 16, 32, 64, 100]
    data = []
    for L in sizes:
        Hsw = switching_field(L)
        data.append({
            "L": L,
            "H_sw": round(Hsw, 6)
        })
    with open(outpath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote switching field data for {len(data)} sizes to {outpath}")
