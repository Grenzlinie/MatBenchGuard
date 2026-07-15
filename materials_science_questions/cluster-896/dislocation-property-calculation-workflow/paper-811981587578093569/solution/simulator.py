#!/usr/bin/env python3
import sys, math, csv
import numpy as np
from scipy.optimize import fsolve

# Material constants (SI units)
b = 0.176e-9               # Burgers vector magnitude
mu = 79e9                  # shear modulus
nu = 0.3
b_e = b / math.sqrt(2)     # equal edge/screw component assumption
b_s = b / math.sqrt(2)
tau_f = 300e6              # friction on head dislocation
tau_lattice = 30e6         # lattice friction on others

def forces(x_vec, d, n, tau_a):
    """Return net force per unit length on each dislocation in pile-up 1."""
    F = np.zeros(n)
    for i in range(n):
        xi = x_vec[i]
        # external force: applied minus friction
        if i == 0:
            f_ext = tau_a - tau_f
        else:
            f_ext = tau_a - tau_lattice
        f_ext *= b   # τ * Burgers vector magnitude

        # interactions with same pile-up (j != i)
        f_int = 0.0
        for j in range(n):
            if j == i:
                continue
            xj = x_vec[j]
            r = xi - xj
            # edge-edge same: Eq (1) in paper
            if abs(r) > 1e-20:
                f_int += (mu * b_e**2 / (2*math.pi*(1-nu))) * (1.0 / r)
            # screw-screw same: Eq (3)  1/(xi + xj)
            sum_x = xi + xj
            if sum_x > 1e-20:
                f_int += (mu * b_s**2 / (2*math.pi)) * (1.0 / sum_x)

        # interactions with opposing pile-up (positions -x_j)
        for j in range(n):
            xj_opp = -x_vec[j]
            r = xi - xj_opp   # = xi + xj
            r2 = r*r
            d2 = d*d
            # edge-edge different: Eq (2)
            term = r * (r2 - d2) / ((r2 + d2)**2)
            f_int += - (mu * b_e**2 / (2*math.pi*(1-nu))) * term
            # screw-screw different: Eq (4)
            denom = r2 - d2
            if abs(denom) > 1e-20:
                f_int += - (mu * b_s**2 / (2*math.pi)) * (r / denom)

        F[i] = f_ext + f_int
    return F

def solve_equilibrium(d, n, tau_a, x0):
    """Attempt to find equilibrium positions; returns (success, positions)."""
    try:
        sol = fsolve(lambda x: forces(x, d, n, tau_a), x0, maxfev=1000, xtol=1e-12)
    except Exception:
        return False, None
    # check physical: positive, increasing
    if np.all(sol > 1e-14) and np.all(np.diff(sol) > 0):
        return True, sol
    return False, None

def critical_tau_a(d, n):
    """Bisection on applied stress; use continuation in d for efficiency."""
    lo = 0.0
    hi = 2000e6
    x_g = None
    # Rough guess for initial x0 based on d
    x0 = np.linspace(5e-9, 100e-9, n)  # fallback
    for _ in range(30):
        mid = (lo + hi) / 2
        ok, sol = solve_equilibrium(d, n, mid, x0.copy() if x0 is not None else np.linspace(0.1*d, 5*d, n))
        if ok:
            hi = mid
            x0 = sol
        else:
            lo = mid
            # optionally try a different guess
            if x0 is not None:
                ok2, sol2 = solve_equilibrium(d, n, mid, x0 * 0.9)
                if ok2:
                    hi = mid
                    x0 = sol2
                    continue
            # if still fails, keep searching
    return (lo + hi) / 2 / 1e6   # MPa

def main():
    d_nm_list = [10, 12, 15, 18, 20, 25, 30, 35, 40, 50, 60, 75, 100, 150, 200, 260, 300, 400, 500]
    n_list = [5, 10, 15, 20]
    outfile = '/app/outputs/simulation_results.csv'
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['d_nm', 'n', 'tau_a_MPa'])
        for n in n_list:
            # process d from large to small to reuse solution
            d_sorted = sorted(d_nm_list, reverse=True)
            x_prev = None
            for d_nm in d_sorted:
                d = d_nm * 1e-9
                # find critical tau_a using a single bisection with history
                def tau_solver():
                    lo = 0.0
                    hi = 2000e6
                    x0 = x_prev if x_prev is not None else np.linspace(0.1*d, 5*d, n)
                    for _ in range(30):
                        mid = (lo + hi) / 2
                        ok, sol = solve_equilibrium(d, n, mid, x0.copy())
                        if ok:
                            hi = mid
                            x0 = sol
                        else:
                            lo = mid
                    return (lo + hi) / 2 / 1e6, x0
                tau_mpa, x_prev = tau_solver()
                writer.writerow([d_nm, n, round(tau_mpa, 2)])
    print('simulation_results.csv written', file=sys.stderr)

if __name__ == '__main__':
    main()
