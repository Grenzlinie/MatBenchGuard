import sys
import csv
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

p = 8.0  # mm
h = 1.0  # half-thickness in mm
hp = h / p  # 0.125
deltas = [1, 2, 3, 4, 5, 6]
wavelengths = [50.0, 70.0, 90.0, 120.0]

def integrand_I1(u, t, sigma):
    return np.sqrt((t - u) / (u * (1 - u) * (sigma - u)))

def I1(sigma, t):
    if t == 0.0:
        return 0.0
    res, _ = quad(integrand_I1, 0, t, args=(t, sigma), limit=500, epsabs=1e-12, epsrel=1e-12,
                  points=[0, t])
    return res

def integrand_I2(u, t, sigma):
    return np.sqrt((u - t) / (u * (1 - u) * (sigma - u)))

def I2(sigma, t):
    if t == 1.0:
        return 0.0
    res, _ = quad(integrand_I2, t, 1, args=(t, sigma), limit=500, epsabs=1e-12, epsrel=1e-12,
                  points=[t, 1])
    return res

def objective(vars, q, hp):
    sigma, t = vars
    f1 = np.pi * q - I1(sigma, t)
    f2 = 2 * np.pi * hp - I2(sigma, t)
    return f1**2 + f2**2

def solve_sigma_t(q, hp):
    bounds = [(1.0001, 50.0), (0.0001, 0.9999)]
    sigma0, t0 = 1.5, 0.5
    res = minimize(objective, [sigma0, t0], args=(q, hp), method='L-BFGS-B', bounds=bounds,
                   options={'ftol': 1e-12, 'gtol': 1e-12})
    if not res.success:
        res = minimize(objective, [2.0, 0.5], args=(q, hp), method='L-BFGS-B', bounds=bounds,
                       options={'ftol': 1e-12, 'gtol': 1e-12})
    if not res.success:
        print(f"Optimization failed for q={q}, hp={hp}: {res.message}", file=sys.stderr)
    sigma, t = res.x
    sigma = max(sigma, 1.0001)
    t = max(min(t, 0.9999), 0.0001)
    return sigma, t

def l1_integrand(u, sigma, t):
    denom = np.sqrt((1 - u) * (1 - sigma * u)) * (np.sqrt(1 - t * u) + 1)
    return 1.0 / denom

def compute_l1(sigma, t):
    upper = 1.0 / sigma
    res, _ = quad(l1_integrand, 0, upper, args=(sigma, t), limit=500, epsabs=1e-12, epsrel=1e-12,
                  points=[0, upper])
    return (t * p) / (2 * np.pi) * res

def compute_R(delta, wavelength):
    q = (p - delta) / p
    sigma, t = solve_sigma_t(q, hp)
    l = (p - delta) * h / p          # = (p - delta) / 8
    l1_val = compute_l1(sigma, t)
    l2_val = l1_val + p / (2 * np.pi) * np.log((sigma - 1) / sigma)
    k = 2 * np.pi / wavelength
    term1 = (1 + 1j * k * l) / (1 - 1j * k * l)
    term2 = (1 - 1j * k * l1_val) / (1 + 1j * k * l1_val)
    R_complex = 0.5 * (term1 - term2)
    R = np.abs(R_complex)**2
    return R

with open("/app/outputs/reflection_coefficients.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["delta_mm", "wavelength_mm", "R"])
    for delta in deltas:
        for lam in wavelengths:
            R = compute_R(delta, lam)
            writer.writerow([delta, lam, R])
