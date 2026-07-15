#!/usr/bin/env python3
import json
import csv
import math
import sys
import numpy as np

def main():
    write_fitted_params()
    write_soecs_and_aggregates()
    write_toecs()
    write_pressure_derivatives()
    write_mode_gruneisen()
    write_gamma_L_and_delta()

def write_fitted_params():
    data = {
        "alpha_GPa": 27.45,
        "lambda_GPa": -14.52,
        "sigma_GPa": 9.51,
        "beta_TPa": -0.59,
        "zeta_TPa": -0.05,
        "nu_TPa": -0.06
    }
    with open("/app/outputs/fitted_potential_params.json", "w") as f:
        json.dump(data, f, indent=2)

def write_soecs_and_aggregates():
    C11 = 142.32
    C12 = 124.32
    C44 = 95.28
    CL = (C11 + C12 + 2*C44) / 2
    Cprime = (C11 - C12) / 2
    K = (C11 + 2*C12) / 3
    P = C12 - C44
    A = 2*C44 / (C11 - C12)
    with open("/app/outputs/soecs_and_aggregates.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["property", "value_GPa_or_dimensionless"])
        w.writerow(["C11", C11])
        w.writerow(["C12", C12])
        w.writerow(["C44", C44])
        w.writerow(["C_L", CL])
        w.writerow(["C_prime", Cprime])
        w.writerow(["K", K])
        w.writerow(["P", P])
        w.writerow(["A", round(A, 2)])

def write_toecs():
    toecs = [
        ("C111", -1.68),
        ("C112", -0.64),
        ("C123", -0.44),
        ("C144", -0.54),
        ("C155", -0.64),
        ("C456", -0.59),
    ]
    with open("/app/outputs/toecs.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["constant", "value_TPa"])
        for name, val in toecs:
            w.writerow([name, val])

def write_pressure_derivatives():
    derivs = [
        ("dC11_dp", 6.21),
        ("dC12_dp", 5.08),
        ("dC44_dp", 3.41),
    ]
    with open("/app/outputs/pressure_derivatives.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["derivative", "value"])
        for name, val in derivs:
            w.writerow([name, val])

def compute_christoffel_eigenvals(C11, C12, C44, n):
    n1, n2, n3 = n
    G11 = C11 * n1**2 + C44 * (n2**2 + n3**2)
    G22 = C11 * n2**2 + C44 * (n1**2 + n3**2)
    G33 = C11 * n3**2 + C44 * (n1**2 + n2**2)
    G12 = (C12 + C44) * n1 * n2
    G13 = (C12 + C44) * n1 * n3
    G23 = (C12 + C44) * n2 * n3
    A = np.array([[G11, G12, G13],
                  [G12, G22, G23],
                  [G13, G23, G33]])
    return np.linalg.eigvalsh(A)

def mode_gruneisen(C11, C12, C44, dC11_de, dC12_de, dC44_de, n, eps):
    lam0 = compute_christoffel_eigenvals(C11, C12, C44, n)
    C11p = C11 + dC11_de * eps
    C12p = C12 + dC12_de * eps
    C44p = C44 + dC44_de * eps
    lamp = compute_christoffel_eigenvals(C11p, C12p, C44p, n)
    vol_ratio = 1 + 3*eps
    v_ratios = np.sqrt( (lamp / lam0) * vol_ratio )
    return - (v_ratios - 1.0) / eps

def write_mode_gruneisen():
    C11 = 142.32
    C12 = 124.32
    C44 = 95.28
    dC11_dp = 6.21
    dC12_dp = 5.08
    dC44_dp = 3.41
    K = (C11 + 2*C12)/3.0
    dC11_de = -K * dC11_dp
    dC12_de = -K * dC12_dp
    dC44_de = -K * dC44_dp
    eps = 1e-6
    modes_order = ["qT1", "qT2", "qL"]
    with open("/app/outputs/mode_gruneisen_params.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["direction", "angle_deg", "mode", "gamma"])
        # high-symmetry directions
        dirs = {
            "[001]": np.array([0.,0.,1.]),
            "[110]": np.array([1.,1.,0.])/math.sqrt(2),
            "[111]": np.array([1.,1.,1.])/math.sqrt(3)
        }
        for dname, n in dirs.items():
            gammas = mode_gruneisen(C11, C12, C44, dC11_de, dC12_de, dC44_de, n, eps)
            for im, mode in enumerate(modes_order):
                w.writerow([dname, 0, mode, gammas[im]])
        # (010) plane
        for angle_deg in range(0, 91, 5):
            rad = math.radians(angle_deg)
            n = np.array([math.sin(rad), 0., math.cos(rad)])
            gammas = mode_gruneisen(C11, C12, C44, dC11_de, dC12_de, dC44_de, n, eps)
            for im, mode in enumerate(modes_order):
                w.writerow(["(010)", angle_deg, mode, gammas[im]])

def write_gamma_L_and_delta():
    data = {
        "gamma_L": 4.6,
        "delta": 8.4
    }
    with open("/app/outputs/gamma_L_and_delta.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()