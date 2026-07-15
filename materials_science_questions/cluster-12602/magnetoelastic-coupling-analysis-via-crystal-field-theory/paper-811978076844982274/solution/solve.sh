#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: magnetoelastic_results.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import csv, os, sys

OUTDIR = '/app/outputs'
os.makedirs(OUTDIR, exist_ok=True)

k = -1.1
c = 1.0
l = 1.0
m = 2.0

ts = np.linspace(0.0, 2.0, 101)

def safe_logcosh(x):
    ax = np.abs(x)
    return ax + np.log1p(np.exp(-2*ax)) - np.log(2)

def f_system(z, t, phase):
    sigma, eps = z
    if sigma < 0:
        sigma = 0.0
    if t == 0:
        return [0.0, 0.0]
    a = l * eps / t
    if phase == 'A':
        b = sigma * (m - (1 + k*eps)) / t
    else:
        b = sigma * (m + 1 + k*eps) / t
    logcosh_b = safe_logcosh(b)
    logX = np.log(2) + a + logcosh_b
    tanh_b = np.tanh(b)
    if logX > 0:
        sigma_eq = tanh_b / (1.0 + np.exp(-logX))
    else:
        sigma_eq = np.exp(logX) * tanh_b / (1.0 + np.exp(logX))
    tmp = 1.0 / (1.0 + np.exp(-logX))
    term1 = 2.0 * l * tmp
    if phase == 'A':
        eps_eq = (term1 - sigma**2 * k) / (2.0 * c)
    else:
        eps_eq = (term1 + sigma**2 * k) / (2.0 * c)
    return [sigma_eq - sigma, eps_eq - eps]

def compute_f(sigma, eps, t, phase):
    if t == 0:
        if phase == 'A':
            return 1.0 - m - (2*l - k)**2 / (4*c)
        else:
            return -1.0 - m - (2*l + k)**2 / (4*c)
    sigma1 = sigma if phase == 'F' else sigma
    sigma2 = sigma if phase == 'F' else -sigma
    y2 = l * eps
    y4 = y2
    y1 = sigma2 * (1 + k*eps) + sigma1 * m
    y3 = sigma1 * (1 + k*eps) + sigma2 * m
    a2 = y2 / t
    a4 = y4 / t
    b1 = y1 / t
    b3 = y3 / t
    logcosh1 = safe_logcosh(b1)
    logX1 = np.log(2) + a2 + logcosh1
    X1 = np.exp(logX1)
    Z1 = X1 + 1
    Q1 = X1 / Z1
    logcosh2 = safe_logcosh(b3)
    logX2 = np.log(2) + a4 + logcosh2
    X2 = np.exp(logX2)
    Z2 = X2 + 1
    Q2 = X2 / Z2
    term_log = t * (np.log(Z1) + np.log(Z2))
    f = -term_log
    f += -sigma1 * sigma2 * (1 + k*eps)
    f += -l * eps * (Q1 + Q2)
    f += -0.5 * m * (sigma1**2 + sigma2**2)
    f += y1 * sigma1 + y3 * sigma2
    f += y2 * Q1 + y4 * Q2
    f += c * eps**2
    return f

prev_A = [1.0, (4*l - k) / (2*c)]
prev_F = [1.0, (4*l + k) / (2*c)]
rows = []
for t in ts:
    if t == 0.0:
        sigma_A, eps_A = prev_A
        sigma_F, eps_F = prev_F
    else:
        try:
            sol_A = fsolve(lambda z: f_system(z, t, 'A'), prev_A, xtol=1e-12, maxfev=2000)
            if np.linalg.norm(f_system(sol_A, t, 'A')) < 1e-8:
                prev_A = sol_A
        except Exception:
            pass
        sigma_A, eps_A = prev_A
        try:
            sol_F = fsolve(lambda z: f_system(z, t, 'F'), prev_F, xtol=1e-12, maxfev=2000)
            if np.linalg.norm(f_system(sol_F, t, 'F')) < 1e-8:
                prev_F = sol_F
        except Exception:
            pass
        sigma_F, eps_F = prev_F
    f_A = compute_f(sigma_A, eps_A, t, 'A')
    f_F = compute_f(sigma_F, eps_F, t, 'F')
    rows.append([t, sigma_A, sigma_F, eps_A, eps_F, f_A, f_F])

csv_path = os.path.join(OUTDIR, 'magnetoelastic_results.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['t', 'sigma_A', 'sigma_F', 'epsilon_A', 'epsilon_F', 'f_A', 'f_F'])
    writer.writerows(rows)
print('magnetoelastic_results.csv written')
PYEOF
