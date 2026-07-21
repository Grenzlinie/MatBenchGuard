import sys
import csv
import numpy as np
from scipy.optimize import fsolve

T = 300.0

# material parameters (from paper)
sigma_m = 1.34e-5          # S/m
sigma_f = 500.07
t_sigma = 2.1

kappa_m = 0.63             # W/m/K
kappa_f = 31.2
t_kappa = 1.0
A_kappa = 2.0              # no percolation (paper's EMT fit)

kappaS_m = 1.15e-4         # W/m/μV
kappaS_f = 1.2
t_kappaS = 1.0


def solve_gemt(val_m, val_f, t, A, phi):
    """
    Solve the GEMT equation for effective property.
    phi   : filler volume fraction (0..1)
    val_m : matrix property
    val_f : filler property
    t     : critical exponent
    A     : coefficient depending on percolation threshold: (1-phi_c)/phi_c
    """
    if phi <= 0.0:
        return val_m
    if phi >= 1.0:
        return val_f
    a = 1.0 / t
    def f(x):
        if x <= 0.0:
            return -1e9
        xa = x ** a
        vma = val_m ** a
        vfa = val_f ** a
        term1 = phi * (vfa - xa) / (vfa + A * xa)
        term2 = (1.0 - phi) * (vma - xa) / (vma + A * xa)
        return term1 + term2
    # initial guess: linear interpolation
    guess = (1.0 - phi) * val_m + phi * val_f
    if guess <= 0.0:
        guess = 1e-12
    try:
        sol = fsolve(f, guess, maxfev=1000, xtol=1e-12, full_output=False)
        if isinstance(sol, (list, np.ndarray)):
            sol = sol[0]
        return sol
    except Exception:
        # fallback: return guess (should not happen for these parameters)
        return guess


def main():
    if len(sys.argv) != 4:
        print("Usage: helper.py <output_csv> <phi_sigma> <phi_kappaS>")
        sys.exit(1)
    output_file = sys.argv[1]
    phi_sigma = float(sys.argv[2])
    phi_kappaS = float(sys.argv[3])

    A_sigma = (1.0 - phi_sigma) / phi_sigma
    A_kappaS = (1.0 - phi_kappaS) / phi_kappaS

    # filler vol% from 0 to 12 in steps of 0.5
    percents = np.arange(0.0, 12.5, 0.5)
    rows = []
    for vol_pct in percents:
        phi = vol_pct / 100.0
        sigma_e = solve_gemt(sigma_m, sigma_f, t_sigma, A_sigma, phi)
        kappa_e = solve_gemt(kappa_m, kappa_f, t_kappa, A_kappa, phi)
        kappaS_e = solve_gemt(kappaS_m, kappaS_f, t_kappaS, A_kappaS, phi)
        Seebeck_e = kappa_e / kappaS_e if kappaS_e != 0.0 else 0.0   # μV/K
        ZT = (sigma_e * Seebeck_e ** 2 * T) / kappa_e
        rows.append([vol_pct, sigma_e, kappa_e, kappaS_e, Seebeck_e, ZT])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['filler_vol_percent', 'sigma_e', 'kappa_e', 'kappa_S_e', 'Seebeck_e', 'ZT'])
        writer.writerows(rows)


if __name__ == "__main__":
    main()
