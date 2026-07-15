#!/usr/bin/env python3
import sys
import argparse
import json
import csv
import numpy as np
from scipy.integrate import quad

def load_data(path):
    T, CpR = [], []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            T.append(float(row['T_mean']))
            CpR.append(float(row['Cp_over_R']))
    return np.array(T), np.array(CpR)

def rel_error(T):
    if T <= 5.0:
        return 0.05
    elif T <= 14.0:
        return 0.05 + (0.01 - 0.05) / (14.0 - 5.0) * (T - 5.0)
    elif T <= 30.0:
        return 0.01 + (0.005 - 0.01) / (30.0 - 14.0) * (T - 14.0)
    else:
        return 0.005

def fit_high_poly(T_high, CpR_high, degree=5):
    weights = 1.0 / (rel_error(T_high) * CpR_high)**2
    coeffs = np.polynomial.polynomial.polyfit(T_high, CpR_high, degree, w=weights)
    return coeffs

def fit_low_constrained(T_low, CpR_low, degree, x0, y0, dy0):
    # P_low(x) = y0 + dy0*(x-x0) + (x-x0)^2 * Q(x), Q(x) degree (degree-2)
    if degree < 2:
        raise ValueError("Degree must be at least 2 to enforce two constraints")
    weights = 1.0 / (rel_error(T_low) * CpR_low)**2
    # design matrix for Q coefficients
    A = np.zeros((len(T_low), degree-1))
    for i in range(degree-1):
        A[:, i] = (T_low - x0)**2 * T_low**i
    rhs = CpR_low - (y0 + dy0*(T_low - x0))
    # weighted least squares
    W = np.diag(weights)
    Aw = W @ A
    bw = W @ rhs
    coeffs_free, _, _, _ = np.linalg.lstsq(Aw, bw, rcond=None)
    # reconstruct full polynomial coefficients by sampling and fitting
    t_samp = np.linspace(np.min(T_low), np.max(T_low), 2000)
    p_samp = y0 + dy0*(t_samp - x0)
    for i in range(degree-1):
        p_samp += coeffs_free[i] * ( (t_samp - x0)**2 * t_samp**i )
    coeffs_full = np.polynomial.polynomial.polyfit(t_samp, p_samp, degree)
    return coeffs_full

def write_coefficients(output_path):
    T_all, CpR_all = load_data('/solution/silicalite_heat_capacity_data.csv')
    low_mask = T_all < 40.0
    high_mask = T_all > 20.0
    T_low = T_all[low_mask]
    CpR_low = CpR_all[low_mask]
    T_high = T_all[high_mask]
    CpR_high = CpR_all[high_mask]
    high_degree = 5
    high_coeffs = fit_high_poly(T_high, CpR_high, degree=high_degree)
    x0 = 25.6
    y0 = np.polynomial.polynomial.polyval(x0, high_coeffs)
    dy0 = np.polynomial.polynomial.polyval(x0, np.polynomial.polynomial.polyder(high_coeffs))
    low_degree = 5
    low_coeffs = fit_low_constrained(T_low, CpR_low, low_degree, x0, y0, dy0)
    # coefficients to list (ascending order)
    result = {
        "low_T_poly": low_coeffs.tolist(),
        "high_T_poly": high_coeffs.tolist()
    }
    with open(output_path, 'w') as f:
        json.dump(result, f)

def compute_thermo(output_path):
    T_all, CpR_all = load_data('/solution/silicalite_heat_capacity_data.csv')
    low_mask = T_all < 40.0
    high_mask = T_all > 20.0
    T_low = T_all[low_mask]
    CpR_low = CpR_all[low_mask]
    T_high = T_all[high_mask]
    CpR_high = CpR_all[high_mask]
    high_degree = 5
    high_coeffs = fit_high_poly(T_high, CpR_high, degree=high_degree)
    x0 = 25.6
    y0 = np.polynomial.polynomial.polyval(x0, high_coeffs)
    dy0 = np.polynomial.polynomial.polyval(x0, np.polynomial.polynomial.polyder(high_coeffs))
    low_degree = 5
    low_coeffs = fit_low_constrained(T_low, CpR_low, low_degree, x0, y0, dy0)
    # Debye extrapolation
    T5 = 5.0
    Cp5_over_R = np.polynomial.polynomial.polyval(T5, low_coeffs)  # low poly valid at 5 K
    A = Cp5_over_R / (T5**3)   # Cp/R = A * T^3
    # functions for integration
    def cp_over_R(T):
        if T <= T5:
            return A * T**3
        elif T < x0:
            return np.polynomial.polynomial.polyval(T, low_coeffs)
        else:
            return np.polynomial.polynomial.polyval(T, high_coeffs)
    # entropy integral: DeltaS_R = int_0^298.15 (Cp/R)/T dT
    S_0_5 = A/3 * T5**3
    S_5_298, _ = quad(lambda T: cp_over_R(T)/T, T5, 298.15, limit=200)
    DeltaS_R = S_0_5 + S_5_298
    # enthalpy increment: DeltaH_R_K = int_0^298.15 (Cp/R) dT  (in K units, dimensionless)
    H_0_5 = A/4 * T5**4
    H_5_298, _ = quad(lambda T: cp_over_R(T), T5, 298.15, limit=200)
    DeltaH_R_K = H_0_5 + H_5_298
    Cp_298 = np.polynomial.polynomial.polyval(298.15, high_coeffs)
    # write CSV
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'Cp_m_R', 'DeltaS_R', 'DeltaH_R_K'])
        writer.writerow([298.15, Cp_298, DeltaS_R, DeltaH_R_K])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--task', required=True, choices=['coefficients', 'thermo'])
    args = parser.parse_args()
    if args.task == 'coefficients':
        write_coefficients(args.output)
    else:
        compute_thermo(args.output)
