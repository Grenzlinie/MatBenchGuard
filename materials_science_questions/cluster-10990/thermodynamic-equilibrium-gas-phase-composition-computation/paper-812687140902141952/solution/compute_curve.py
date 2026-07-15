#!/usr/bin/env python3
import sys
import csv
import numpy as np

def main():
    if len(sys.argv) != 3:
        print("Usage: compute_curve.py <output_dir> <mode (phase|cover)>", file=sys.stderr)
        sys.exit(1)
    out_dir = sys.argv[1]
    mode = sys.argv[2]
    
    # constants
    theta_D = 1860.0          # K
    eps_a = 4.0               # eV
    k_perp = 3107.0           # cm^{-1}
    k_par = 1405.0            # cm^{-1}
    
    if mode == "phase":
        T = np.arange(1000, 2501, 10)   # 1000..2500 inclusive
        cases = [
            ("d3", 3, 7.0, 1e-3, "P_d3_f1e-3"),
            ("d3", 3, 7.0, 1e-4, "P_d3_f1e-4"),
            ("d2", 2, 5.0, 1e-3, "P_d2_f1e-3"),
            ("d2", 2, 5.0, 1e-4, "P_d2_f1e-4"),
        ]
        header = ["T"] + [col for _, _, _, _, col in cases]
        rows = []
        for i, t in enumerate(T):
            row = [t]
            for _, d, eps_c, f, _ in cases:
                # eq 10
                P = 0.108 * t**2.5 / f * (2.0 * np.sinh(theta_D/(2.0*t)))**d * np.exp(-11600.0*eps_c/t)
                row.append(P)
            rows.append(row)
        
        with open(f"{out_dir}/step_01_phase_boundary.csv", "w", newline='') as fh:
            writer = csv.writer(fh)
            writer.writerow(header)
            writer.writerows(rows)
        print("step_01_phase_boundary.csv written")
        
    elif mode == "cover":
        T = np.arange(1000, 2001, 10)
        cases = [
            ("d3", 3, 7.0, 0.01, "theta_d3_f0.01"),
            ("d3", 3, 7.0, 0.005, "theta_d3_f0.005"),
            ("d2", 2, 5.0, 0.01, "theta_d2_f0.01"),
            ("d2", 2, 5.0, 0.005, "theta_d2_f0.005"),
        ]
        header = ["T"] + [col for _, _, _, _, col in cases]
        rows = []
        for i, t in enumerate(T):
            row = [t]
            for _, d, eps_c, f, _ in cases:
                sinh_factor = (2.0 * np.sinh(theta_D/(2.0*t)))**d
                exp_factor = np.exp(-11600.0*(eps_c - eps_a)/t)
                vib_factor = (2.0 * np.sinh(0.719 * k_perp/t))**(-1) * (2.0 * np.sinh(0.719 * k_par/t))**(-2)
                Z1_over_q1 = 2.0 * exp_factor * sinh_factor * vib_factor
                A = 41.1 * (1.0 - f)/f * Z1_over_q1
                theta = A / (1.0 + A)
                row.append(theta)
            rows.append(row)
        
        with open(f"{out_dir}/step_02_covering_ratio.csv", "w", newline='') as fh:
            writer = csv.writer(fh)
            writer.writerow(header)
            writer.writerows(rows)
        print("step_02_covering_ratio.csv written")
        
    else:
        print("Unknown mode; use 'phase' or 'cover'", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
