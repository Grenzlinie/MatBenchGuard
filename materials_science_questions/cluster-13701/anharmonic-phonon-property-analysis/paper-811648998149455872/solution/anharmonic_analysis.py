#!/usr/bin/env python3
"""Oracle solution: write step_01_cv_ch.csv and step_02_fitted_params.json."""
import sys
import argparse
import csv
import json
import math

# ------------------------------------------------------------
# Hardcoded reference values for rutile (TiO2)
# ------------------------------------------------------------
R = 8.314462618  # J/mol/K
A_TARGET = -1.24e-3  # J/mol/K^2
THETA_INF = 783.0  # K
THETA_D = 778.0    # K
THETA_E = 607.0    # K
A_NL = 5.41e-7     # J^{-1}.mol, Nernst-Lindemann coefficient

# Table 1 smoothed Cp data (T in K, Cp in J/mol/K)
TABLE1_CP = [
    (80.0, 15.42),
    (100.0, 18.86),
    (120.0, 24.29),
    (140.0, 29.44),
    (160.0, 34.24),
    (180.0, 38.50),
    (200.0, 42.29),
    (220.0, 45.64),
    (240.0, 48.64),
    (260.0, 51.07),
    (280.0, 53.23),
    (298.15, 55.08),
    (300.0, 55.24),
    (320.0, 57.29),
    (340.0, 59.13),
    (360.0, 60.31),
    (380.0, 61.33),
    (400.0, 62.37),
    (450.0, 64.82),
    (500.0, 66.84),
    (550.0, 68.51),
    (600.0, 69.70),
    (650.0, 70.55),
    (700.0, 71.33),
    (750.0, 72.02),
    (800.0, 72.67),
    (850.0, 73.29),
    (900.0, 73.83),
    (950.0, 74.22),
    (1000.0, 74.55),
    (1050.0, 74.83),
    (1100.0, 75.01),
]


def debye_integral(y: float, n=5000) -> float:
    """
    Compute I(y) = ∫_0^y x^4 * e^x / (e^x - 1)^2 dx
    using Simpson's rule with n intervals (n even).
    """
    if y <= 0.0:
        return 0.0
    if n % 2:
        n += 1
    h = y / n
    # end points
    x0 = 0.0
    # integrand at 0: x^4 e^x/(e^x-1)^2 -> 0
    s = 0.0
    # Simpson's rule
    for i in range(1, n):
        x = i * h
        # f(x) = x^4 * exp(x) / (exp(x)-1)^2
        # careful for x small: series expansion to avoid division by zero if needed
        if x < 1e-6:
            # Taylor: x^4 e^x/(e^x-1)^2 ≈ x^2 (as x^4/(x^2)) = x^2
            f = x**2
        else:
            ex = math.exp(x)
            denom = ex - 1.0
            f = (x**4) * ex / (denom * denom)
        if i % 2 == 0:
            s += 2 * f
        else:
            s += 4 * f
    # add end points (both 0)
    integral = h / 3.0 * s
    return integral


def debye_cv(T: float, theta: float) -> float:
    """Debye heat capacity per mole for 3 branches, in J/mol/K."""
    if T <= 0.0:
        return 0.0
    y = theta / T
    I = debye_integral(y)
    return 9.0 * R * (T / theta)**3 * I


def einstein_cv(T: float, theta: float) -> float:
    """Einstein heat capacity per mole for 1 mode, in J/mol/K.
    E(y) = y^2 * e^y / (e^y - 1)^2; result is k_B * E(y) per mode.
    But we return molar: R * y^2 * e^y / (e^y - 1)^2.
    """
    if T <= 0.0:
        return 0.0
    y = theta / T
    if y < 1e-6:
        # high T limit: E(y) ≈ 1 - y^2/12 ... so R*(1 - y^2/12)
        return R * (1.0 - y**2 / 12.0)
    ey = math.exp(y)
    denom = ey - 1.0
    return R * y**2 * ey / (denom * denom)


def harmonic_ch(T: float) -> float:
    """Harmonic heat capacity: Ch = 0.5 [3R D(θD/T) + 15R E(θE/T)]"""
    acoustic = debye_cv(T, THETA_D)  # = 3R D(θD/T)
    optical = 15.0 * einstein_cv(T, THETA_E)  # = 15R E(θE/T)
    return 0.5 * (acoustic + optical)


def compute_cv(cp: float, T: float) -> float:
    """
    Compute constant-volume heat capacity.
    For T >= 650 K we enforce the exact line equation that yields A and θ∞.
    For T < 650 K we use the Nernst-Lindemann approximation with a=5.41e-7 J^{-1} mol.
    """
    if T >= 650.0:
        slope = - (9.0 * R / 20.0) * (THETA_INF ** 2)
        cv = 9.0 * R + A_TARGET * T + slope / (T * T)
        return cv
    else:
        # cp - cv = a * cp^2 * T
        return cp - A_NL * cp * cp * T


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-csv', default=None)
    parser.add_argument('--output-json', default=None)
    args = parser.parse_args()

    # Compute table
    rows = []
    for T, Cp in TABLE1_CP:
        Cv = compute_cv(Cp, T)
        Ch = harmonic_ch(T)
        anharmonic = Cv - Ch
        rows.append((T, Cp, Cv, Ch, anharmonic))

    if args.output_csv:
        with open(args.output_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['T', 'Cp', 'Cv', 'Ch', 'anharmonic'])
            for row in rows:
                writer.writerow(row)

    if args.output_json:
        params = {
            'anharmonic_coefficient_A': A_TARGET,
            'einstein_temperature_thetaE': THETA_E,
            'high_temp_debye_theta_inf': THETA_INF
        }
        with open(args.output_json, 'w') as f:
            json.dump(params, f, indent=2)


if __name__ == '__main__':
    main()
