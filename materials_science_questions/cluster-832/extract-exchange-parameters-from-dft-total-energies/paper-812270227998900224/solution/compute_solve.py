#!/usr/bin/env python3
"""Reference oracle: solve Bethe‑Peierls equations for mixed‑spin Ising model."""
import sys
import csv
import numpy as np
from scipy.optimize import fsolve, minimize

# ---- Coefficient tables (from paper Tables I and II) ----
# each row: a, b, c, d, p, q, r, u, v
T1 = [
    (24, 16, 0, 8,  4, 0, 2, 2, 0),
    (-24, 16, 0, -8,  -4, 0, 2, 2, 0),
    (48, 64, 0, 16, 2, 0, 0, 2, 0),
    (-48, 64, 0, -16,  -2, 0, 0, 2, 0),
    (0, 32, 0, 0, 0, 0, -2, 2, 0),
    (0, 64, 0, 0, 0, 0, 0, 2, 0),
    (0, -32, -24, -4, 4, 8, 0, 2, 8),
    (0, -32, -24, 4, -4, 8, 0, 2, 8),
    (0, -72, -54, -12, 3, 4, 0, 1.5, 4),
    (0, -72, -54, 12, -3, 4, 0, 1.5, 4),
    (0, -32, -24, -8, 2, 2, 0, 1, 2),
    (0, -16, -12, -4, 2, 0, 0, 1, 0),
    (0, -32, -24, -8, 2, 0, 0, 2, 8),
    (0, -32, -24, 8, -2, 2, 0, 1, 2),
    (0, -16, -12, 4, -2, 0, 0, 1, 0),
    (0, -32, -24, 8, -2, 0, 0, 2, 8),
    (0, -8, -6, -4, 1, 0, 0, 0.5, 0),
    (0, -16, -12, -8, 1, 0, 0, 1.5, 4),
    (0, -8, -6, -4, 1, -4, 0, 1.5, 4),
    (0, -8, -6, 4, -1, 0, 0, 0.5, 0),
    (0, -16, -12, 8, -1, 0, 0, 1.5, 4),
    (0, -8, -6, 4, -1, -4, 0, 1.5, 4),
]

T2 = [
    (24, 16, 0, 8,  4, 0, 2, 2, 0),
    (24, -16, 0, 8,  -4, 0, 2, 2, 0),
    (24, 32, 0, 8, 2, 0, 0, 2, 0),
    (24, -32, 0, 8,  -2, 0, 0, 2, 0),
    (24, 0, 0, 8, 0, 0, 2, 0, 0),
    (24, 0, 0, 8, 0, 0, 0, 0, 0),
    (0, -32, -24, -4, 4, 8, 0, 2, 8),
    (0, 32, 24, -4, -4, 8, 0, 2, 8),
    (0, -96, -72, -16, 3, 4, 0, 1.5, 4),
    (0, 96, 72, -16, -3, 4, 0, 1.5, 4),
    (0, -64, -48, -16, 2, 2, 0, 1, 2),
    (0, 64, 48, -16, -2, 2, 0, 1, 2),
    (0, -32, -24, -8, 2, 0, 0, 1, 0),
    (0, -64, -48, -16, 2, 0, 0, 2, 8),
    (0, 32, 24, -8, -2, 0, 0, 1, 0),
    (0, 64, 48, -16, -2, 0, 0, 2, 8),
    (0, -32, -24, -16, 1, 0, 0, 0.5, 0),
    (0, -64, -48, -32, 1, 0, 0, 1.5, 4),
    (0, -32, -24, -16, 1, -4, 0, 1.5, 4),
    (0, 32, 24, -16, -1, 0, 0, 0.5, 0),
    (0, 64, 48, -32, -1, 0, 0, 1.5, 4),
    (0, 32, 24, -16, -1, -4, 0, 1.5, 4),
    (0, 0, 0, -32, 0, -2, 0, 1, 2),
    (0, 0, 0, -16, 0, 0, 0, 1, 0),
    (0, 0, 0, -16, 0, 0, 0, 2, 8),
    (0, 0, 0, -8, 0, -8, 0, 2, 8),
    (0, 0, 0, -4, 0, 0, 0, 0, 0),
]

def eq_value(coeffs, K1, K2, K3, K1p, K2p, r):
    """Compute one of the two equations (13 or 14)."""
    total = 0.0
    for row in coeffs:
        a, b, c, d, p, q, r1, u, v = row
        term = (a * K1 + b * K2) + (c * K1 + d * K3) * r
        total += term * np.exp(p * K1 + q * K2 + r1 * K3 + u * K1p + v * K2p)
    return total

def system(x, r2, r3, r1p, r2p):
    """System of two equations for K1 (x[0]) and r (x[1])."""
    K1, r = x
    K2 = r2 * K1
    K3 = r3 * K1
    K1p = r1p * K1
    K2p = r2p * K1
    f1 = eq_value(T1, K1, K2, K3, K1p, K2p, r)
    f2 = eq_value(T2, K1, K2, K3, K1p, K2p, r)
    return [f1, f2]

# ---- Initial guess for all‑zero case ----
def global_initial_guess():
    """Find solution for J1 only via a quick grid search + fsolve."""
    def sum_sq(x):
        f = system(x, 0, 0, 0, 0)
        return f[0]**2 + f[1]**2
    # coarse grid
    best = None
    best_val = np.inf
    for K1 in np.linspace(0.2, 5, 20):
        for r in np.linspace(0.2, 5, 20):
            val = sum_sq([K1, r])
            if val < best_val:
                best_val = val
                best = [K1, r]
    # refine with fsolve
    sol, infodict, ier, msg = fsolve(lambda x: system(x, 0, 0, 0, 0), best, full_output=True)
    if ier == 1:
        return sol[0], sol[1]
    # fallback: use best from grid
    return best

def scan_parameter(param, values):
    """Solve for a series of parameter values and return list of (value, K1, r)."""
    # set base ratio dict
    ratios = {p:0.0 for p in ['r2','r3','r1p','r2p']}
    # locate zero index
    idx0 = -1
    abs_vals = [abs(v) for v in values]
    if 0.0 in values:
        idx0 = values.index(0.0)
    else:
        # find closest to zero
        idx0 = np.argmin(abs_vals)
    # solve for zero point using global guess
    val0 = values[idx0]
    if val0 == 0.0:
        # global guess
        K1_ref, r_ref = global_initial_guess()
    else:
        # need to solve exactly at val0; use global guess as initial
        pass  # we'll handle below
    solutions = [None] * len(values)
    # solve outward from idx0
    def solve_one(v):
        # set current ratio
        if param == 'J1\u2032':
            ratios = {'r2':0, 'r3':0, 'r1p':v, 'r2p':0}
        elif param == 'J2\u2032':
            ratios = {'r2':0, 'r3':0, 'r1p':0, 'r2p':v}
        elif param == 'J2':
            ratios = {'r2':v, 'r3':0, 'r1p':0, 'r2p':0}
        else: # J3
            ratios = {'r2':0, 'r3':v, 'r1p':0, 'r2p':0}
        return ratios

    # first solve point idx0
    rdict0 = solve_one(val0)
    def run_solve(guess):
        try:
            sol, infodict, ier, msg = fsolve(lambda x: system(x, rdict0['r2'], rdict0['r3'], rdict0['r1p'], rdict0['r2p']), guess, full_output=True, maxfev=2000)
            if ier == 1:
                return sol
            else:
                # try a different guess
                for pert in [(0.5,1.0), (1.0,2.0), (2.0,0.5)]:
                    sol2, infodict2, ier2, _ = fsolve(lambda x: system(x, rdict0['r2'], rdict0['r3'], rdict0['r1p'], rdict0['r2p']), [guess[0]+pert[0], guess[1]+pert[1]], full_output=True)
                    if ier2 == 1:
                        return sol2
                return None
        except Exception:
            return None

    if val0 == 0.0:
        sol0 = run_solve([K1_ref, r_ref])
    else:
        # use global guess
        K1_ref, r_ref = global_initial_guess()
        sol0 = run_solve([K1_ref, r_ref])
    if sol0 is not None:
        K1_prev, r_prev = sol0
        solutions[idx0] = (K1_prev, r_prev)
    else:
        solutions[idx0] = (0.0, 0.0)  # no solution
        K1_prev, r_prev = 0.0, 0.0

    # solve to the right (larger indices)
    for i in range(idx0+1, len(values)):
        v = values[i]
        rdict = solve_one(v)
        guess = [K1_prev, r_prev]
        sol = run_solve(guess)
        if sol is not None:
            K1_prev, r_prev = sol
            solutions[i] = (K1_prev, r_prev)
        else:
            solutions[i] = (0.0, 0.0)  # fallback
            # if solver fails, mark as no order
        # update prev
    # solve to the left (smaller indices)
    if idx0 > 0:
        K1_prev, r_prev = solutions[idx0] if solutions[idx0] is not None else (0.0, 0.0)
        for i in range(idx0-1, -1, -1):
            v = values[i]
            rdict = solve_one(v)
            guess = [K1_prev, r_prev]
            sol = run_solve(guess)
            if sol is not None:
                K1_prev, r_prev = sol
                solutions[i] = (K1_prev, r_prev)
            else:
                solutions[i] = (0.0, 0.0)

    results = []
    for i, v in enumerate(values):
        K1, r = solutions[i] if solutions[i] is not None else (0.0, 0.0)
        Tc = 1.0 / K1 if K1 > 0 else 0.0
        results.append((v, Tc, r))
    return results

def generate_parameter_scans():
    scans = {
        "J1\u2032": np.arange(-2.0, 2.01, 0.05),
        "J2\u2032": np.arange(-2.0, 2.01, 0.1),
        "J2": np.arange(-1.0, 1.01, 0.05),
        "J3": np.arange(-2.0, 2.01, 0.2),
    }
    all_rows = []
    for param, values in scans.items():
        res = scan_parameter(param, list(values))
        for v, Tc, r in res:
            all_rows.append([param, f"{v:.6f}", f"{Tc:.6f}", f"{r:.6f}"])
    return all_rows

def get_instability_point():
    # Reuse the J1' scan
    j1p_values = np.arange(-2.0, 2.01, 0.05)
    res = scan_parameter('J1\u2032', list(j1p_values))
    # sort by value ascending and look for first from 0 downward where Tc <= 1e-6
    # find zero index and go towards negative
    zero_idx = -1
    for i, (v, Tc, r) in enumerate(res):
        if abs(v) < 1e-9:
            zero_idx = i
            break
    if zero_idx == -1:
        # find closest to zero
        zero_idx = min(range(len(res)), key=lambda i: abs(res[i][0]))
    # scan from zero_idx downward (negative direction)
    for i in range(zero_idx, -1, -1):
        val, Tc, r = res[i]
        if Tc <= 1e-6:
            return (val, Tc, r)
    # if none found, return the most negative
    val, Tc, r = res[0]
    return (val, Tc, r)

def main():
    if len(sys.argv) != 2:
        print("Usage: compute_solve.py [parameter_scans|instability_point]", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    if mode == "parameter_scans":
        rows = generate_parameter_scans()
        writer = csv.writer(sys.stdout)
        writer.writerow(["parameter","parameter_value","kB_Tc_over_J1","mu1_over_lambda1"])
        for row in rows:
            writer.writerow(row)
    elif mode == "instability_point":
        cr_val, Tc, r = get_instability_point()
        writer = csv.writer(sys.stdout)
        writer.writerow(["parameter","critical_value","kB_Tc_over_J1","mu1_over_lambda1"])
        writer.writerow(["J1\u2032", f"{cr_val:.6f}", f"{Tc:.6f}", f"{r:.6f}"])
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
