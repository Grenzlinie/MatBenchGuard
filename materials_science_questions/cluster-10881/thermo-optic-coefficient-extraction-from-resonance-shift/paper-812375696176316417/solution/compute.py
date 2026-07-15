import numpy as np
from scipy.special import j0
from scipy.optimize import root_scalar
import csv

# Paper parameters (GaAs coupler)
a = 1.0          # cm
d = 0.5          # cm
k = 0.037        # W/(cm*K)
beta = 0.012     # cm^-1
n0 = 3.30
gamma = 18.7e-5  # 1/K
alpha = 5.7e-6   # 1/K
T0 = 298.0       # K
Tn = 298.1       # K
g = (Tn - T0) / d  # 0.1 / 0.5 = 0.2 K/cm

# power range
P_values = list(range(0, 2001, 100))  # [0, 100, ..., 2000]

def compute_lambda(P):
    Tc = T0 + 2e-4 * P
    if P == 0 or abs(Tc - T0) < 1e-12:
        return 0.0
    ratio = T0 / Tc   # < 1
    # solve J0(x) = ratio
    if ratio > 0.9999:
        # small P: use series J0(x) ≈ 1 - x^2/4
        # 1 - x^2/4 = ratio  => x = 2 * sqrt(1 - ratio)
        eps = 1.0 - ratio
        x = 2.0 * np.sqrt(eps)
        return x / a
    def f(x):
        return j0(x) - ratio
    # bracket [0, first zero of J0] = ~2.4048255577
    x0 = root_scalar(f, bracket=[0.0, 2.4049], method='bisect').root
    return x0 / a

def compute_delta_L(P, lam):
    if P == 0:
        return 0.0
    I = P / (np.pi * a**2)   # W/cm^2
    # common factor
    factor = (alpha + gamma) * n0 * (T0 * d + 0.5 * g * d**2 + (beta * I) / (6.0 * k) * d**3)
    if lam == 0.0:
        return 0.0
    J0_lam_a = j0(lam * a)
    # avoid division by zero if J0_lam_a is 0 (unlikely for P in range)
    if J0_lam_a == 0:
        return None  # will handle
    delta = factor * (1.0 / J0_lam_a - 1.0)
    return delta

def compute_f_th(P, lam, delta_L):
    if P == 0 or delta_L == 0.0:
        # infinite focal length for no thermal lens, replace with very large number
        return 1.0e12
    return a**2 / (2.0 * delta_L * (n0 - 1.0))

# precompute all
data = []
for P in P_values:
    lam = compute_lambda(P)
    dL = compute_delta_L(P, lam)
    fth = compute_f_th(P, lam, dL)
    data.append((P, lam, dL, fth))

def write_lambda(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['P', 'lambda'])
        for row in data:
            writer.writerow([row[0], row[1]])

def write_delta_L(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['P', 'delta_L'])
        for row in data:
            writer.writerow([row[0], row[2]])

def write_focal_length(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['P', 'f_th'])
        for row in data:
            writer.writerow([row[0], row[3]])
