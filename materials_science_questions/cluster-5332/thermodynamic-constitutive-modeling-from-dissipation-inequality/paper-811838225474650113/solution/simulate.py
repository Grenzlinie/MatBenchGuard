import sys
import csv
import numpy as np
from scipy.integrate import solve_ivp

# Material parameters from Table 2 (units: mu1,mu2 in MPa; v in MPa·s; beta dimensionless)
MU1 = 129.1267
MU2 = 70.3011
VISC = 12.4878
BETA = 0.5666

# Original cross-sectional area [mm^2] (ASTM D638 Type IV specimen: 6 mm × 3.2 mm)
A0 = 19.2

def stress_relaxation(output_path):
    conditions = [
        (0.07, 0.0325),
        (0.07, 0.0176),
        (0.08, 0.0008),
    ]
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['test_id', 'time_s', 'force_N'])
        for strain, rate in conditions:
            t_ramp = strain / rate
            t_end = 200.0

            def lambda_fn(t):
                if t <= t_ramp:
                    return 1.0 + rate * t
                else:
                    return 1.0 + strain

            def lambda_dot_fn(t):
                if t <= t_ramp:
                    return rate
                else:
                    return 0.0

            def rhs(t, B):
                lam = lambda_fn(t)
                lam_d = lambda_dot_fn(t)
                b = B[0]
                sqrt_b = np.sqrt(b)
                power = (MU1 / (2.0 * VISC)) ** (1.0 / (2.0 * BETA - 1.0))
                inner = (2.0 + b * sqrt_b) / sqrt_b - (9.0 * b) / (2.0 * b * sqrt_b + 1.0)
                inner_pow = inner ** ((1.0 - BETA) / (2.0 * BETA - 1.0))
                term = (3.0 * b) / (2.0 * b * sqrt_b + 1.0) - b
                dbdt = 2.0 * power * inner_pow * term + 2.0 * b * lam_d / lam
                return [dbdt]

            sol = solve_ivp(rhs, [0, t_end], [1.0], method='RK45', rtol=1e-6, atol=1e-9)
            B_vals = sol.y[0]
            t_vals = sol.t
            lam_vals = np.array([lambda_fn(t) for t in t_vals])
            sqrt_b_vals = np.sqrt(B_vals)
            Tzz = MU1 * (B_vals - 1.0 / sqrt_b_vals) + MU2 * (lam_vals**2 - 1.0 / lam_vals)
            fz = A0 * Tzz / lam_vals
            test_id = f"{strain}_{rate}"
            for t, force in zip(t_vals, fz):
                writer.writerow([test_id, t, force])

def cyclic(output_path):
    freq = 0.4          # Hz
    period = 1.0 / freq
    n_cycles = 20
    t_end = n_cycles * period
    eps_max = 0.06
    strain_ratio = 0.1
    eps_min = strain_ratio * eps_max
    delta_eps = eps_max - eps_min

    def lambda_fn(t):
        t_mod = t % period
        return 1.0 + eps_min + delta_eps * (t_mod / period)

    def lambda_dot_fn(t):
        return delta_eps / period

    def rhs(t, B):
        lam = lambda_fn(t)
        lam_d = lambda_dot_fn(t)
        b = B[0]
        sqrt_b = np.sqrt(b)
        power = (MU1 / (2.0 * VISC)) ** (1.0 / (2.0 * BETA - 1.0))
        inner = (2.0 + b * sqrt_b) / sqrt_b - (9.0 * b) / (2.0 * b * sqrt_b + 1.0)
        inner_pow = inner ** ((1.0 - BETA) / (2.0 * BETA - 1.0))
        term = (3.0 * b) / (2.0 * b * sqrt_b + 1.0) - b
        dbdt = 2.0 * power * inner_pow * term + 2.0 * b * lam_d / lam
        return [dbdt]

    t_eval = np.linspace(0, t_end, 2000)
    sol = solve_ivp(rhs, [0, t_end], [1.0], method='RK45', t_eval=t_eval, rtol=1e-6, atol=1e-9)
    B_vals = sol.y[0]
    t_vals = sol.t
    lam_vals = np.array([lambda_fn(t) for t in t_vals])
    sqrt_b_vals = np.sqrt(B_vals)
    Tzz = MU1 * (B_vals - 1.0 / sqrt_b_vals) + MU2 * (lam_vals**2 - 1.0 / lam_vals)
    fz = A0 * Tzz / lam_vals
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time_s', 'force_N'])
        for t, force in zip(t_vals, fz):
            writer.writerow([t, force])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['stress_relaxation', 'cyclic'])
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if args.mode == 'stress_relaxation':
        stress_relaxation(args.output)
    else:
        cyclic(args.output)