#!/usr/bin/env python3
import numpy as np
from scipy.optimize import fsolve
import json, sys, math

N = 4

def _eigenvalsandvecs(a1, a2, a3):
    """Return list of (E_k, alpha_sq, gamma_sq) for k=0..2."""
    p = math.sqrt(max(3*a1*a1 + 6*a2*a2 + a3*a3, 1e-30))
    sin_arg = a3 * (9*a1*a1 - 9*a2*a2 - a3*a3) / (p*p*p)
    sin_arg = max(-1.0, min(1.0, sin_arg))
    theta = math.asin(sin_arg)
    # eigenvalues
    E = np.zeros(3)
    E[0] = (2.0/3.0)*p*math.sin(theta/3.0) - 2.0/3.0
    E[1] = -(p/3.0)*(math.sin(theta/3.0) + math.sqrt(3)*math.cos(theta/3.0)) - 2.0/3.0
    E[2] = (p/3.0)*(math.sqrt(3)*math.cos(theta/3.0) + math.sin(theta/3.0)) - 2.0/3.0
    # compute alpha_sq, gamma_sq for each
    data = []
    for Ek in E:
        num = a1 - (a3 + Ek)
        denom = math.sqrt(2*a2*a2*(a1*a1 + (a3+Ek)*(a3+Ek)) + (a1*a1 - (a3+Ek)*(a3+Ek))**2)
        if denom == 0:
            alpha_raw = 0.0
        else:
            alpha_raw = a2 * num / denom
        # Compute norm^2 of (alpha, beta, gamma) before normalization
        # beta = - (a1 + a3 + Ek)/a2 * alpha_raw
        # gamma = - (a1 + a3 + Ek)/(a1 - a3 - Ek) * alpha_raw
        # handle a2=0 or a1 - a3 - Ek = 0
        term1 = 1.0
        denom_b = a2 if a2 != 0 else 1e-100
        beta_coeff = (a1 + a3 + Ek) / denom_b
        term2 = beta_coeff * beta_coeff
        denom_g = (a1 - (a3 + Ek))
        if denom_g == 0:
            gamma_coeff = 0.0
            term3 = 0.0
        else:
            gamma_coeff = (a1 + a3 + Ek) / denom_g
            term3 = gamma_coeff * gamma_coeff
        norm_sq = alpha_raw*alpha_raw * (term1 + term2 + term3)
        if norm_sq == 0:
            alpha_sq, gamma_sq = 0.0, 0.0
        else:
            alpha_sq = (alpha_raw*alpha_raw) / norm_sq
            gamma_sq = (alpha_raw*alpha_raw * gamma_coeff * gamma_coeff) / norm_sq
        data.append((Ek, alpha_sq, gamma_sq))
    return data

def F1z(a1, a2, a3):
    data = _eigenvalsandvecs(a1, a2, a3)
    Z = sum(math.exp(-E) for E, _, _ in data)
    num = sum((alpha_sq - gamma_sq)*math.exp(-E) for E, alpha_sq, gamma_sq in data)
    return num / Z

def F2z(a1, a2, a3):
    data = _eigenvalsandvecs(a1, a2, a3)
    Z = sum(math.exp(-E) for E, _, _ in data)
    num = sum((alpha_sq + gamma_sq)*math.exp(-E) for E, alpha_sq, gamma_sq in data)
    return num / Z

def solve_q0z(T, D, c, Omega):
    beta = 1.0 / T
    a2 = beta * Omega / math.sqrt(2)
    a3 = beta * D
    q0z = 0.5
    for it in range(2000):
        s = 0.0
        for mu1 in range(N+1):
            for mu2 in range(N - mu1 + 1):
                for mu3 in range(N - mu1 - mu2 + 1):
                    coeff = math.comb(N, mu1) * math.comb(N-mu1, mu2) * math.comb(N-mu1-mu2, mu3)
                    factor = (2**(mu1+mu3)) * ((1-c)**mu1) * ((c - q0z)**mu3) * (q0z**(N - mu1 - mu3))
                    gamma = N - mu1 - 2*mu2 - mu3
                    a1 = beta * gamma
                    f2 = F2z(a1, a2, a3)
                    s += coeff * factor * f2
        q_new = s * (2**(-N))
        if abs(q_new - q0z) < 1e-14:
            q0z = q_new
            break
        q0z = q_new
    return q0z

def compute_coeffs(T, D, c, Omega, q0z):
    beta = 1.0/T
    a2 = beta * Omega / math.sqrt(2)
    a3 = beta * D
    a_val = 0.0
    b_val = 0.0
    factor_const = 2.0**(-N)
    for mu1 in range(N+1):
        for mu2 in range(N - mu1 + 1):
            for mu3 in range(N - mu1 - mu2 + 1):
                comb_common = math.comb(N, mu1) * math.comb(N-mu1, mu2) * math.comb(N-mu1-mu2, mu3)
                factor_base = (2**(mu1+mu3)) * ((1-c)**mu1) * ((c - q0z)**mu3)
                gamma = N - mu1 - 2*mu2 - mu3
                a1 = beta * gamma
                f1 = F1z(a1, a2, a3)
                for i in range(mu2 + 1):
                    for j in range(N - mu1 - mu2 - mu3 + 1):
                        if i + j == 1:
                            factor = factor_base * math.comb(mu2, i) * math.comb(N - mu1 - mu2 - mu3, j) * ((-1)**i) * (q0z**(N - mu1 - mu3 - i - j))
                            a_val += comb_common * factor * f1
                        if i + j == 3:
                            factor = factor_base * math.comb(mu2, i) * math.comb(N - mu1 - mu2 - mu3, j) * ((-1)**i) * (q0z**(N - mu1 - mu3 - i - j))
                            b_val += comb_common * factor * f1
    a_val *= factor_const
    b_val *= factor_const
    return a_val, b_val

def tricrit_residuals(params, c, Omega):
    T, D = params[0], params[1]
    if T <= 0:
        return [1e6, 1e6]  # penalize negative
    q0z = solve_q0z(T, D, c, Omega)
    a, b = compute_coeffs(T, D, c, Omega, q0z)
    return [a - 1.0, b]

def find_tricrit(c, Omega, T_guess, D_guess):
    sol = fsolve(lambda p: tricrit_residuals(p, c, Omega), [T_guess, D_guess],
                 maxfev=500, xtol=1e-12, epsfcn=1e-8)
    Tt, Dt = sol[0], sol[1]
    return float(Tt), float(Dt)

def main():
    tasks = [
        {"c": 1.0, "Omega_over_J": 0.1, "T_guess": 1.5, "D_guess": -1.88},
        {"c": 0.8, "Omega_over_J": 0.1, "T_guess": 1.0, "D_guess": -1.5},
        {"c": 0.8, "Omega_over_J": 0.5, "T_guess": 0.8, "D_guess": -1.45},
    ]
    results = []
    for task in tasks:
        c = task["c"]
        Omega = task["Omega_over_J"]
        Tt, Dt = find_tricrit(c, Omega, task["T_guess"], task["D_guess"])
        results.append({
            "c": c,
            "Omega_over_J": Omega,
            "Tt_over_J": Tt,
            "neg_Dt_over_J": -Dt  # absolute value
        })
    json.dump(results, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
