#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: critical_temperatures.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy > /dev/null 2>&1
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import root_scalar
import csv
import os
import sys

def f(x, D):
    if D == np.inf:
        return np.tanh(x)
    else:
        return (2.0 * np.exp(D) * np.sinh(x)) / (2.0 * np.exp(D) * np.cosh(x) + 1.0)

def one_dim_corr(k, D):
    f2 = f(2*k, D)
    return (1.0 + np.sqrt(max(1.0 - 2.0 * f2, 0.0))) / f2

def A_honeycomb(k, D):
    f1 = f(k, D)
    f2 = f(2*k, D)
    f3 = f(3*k, D)
    A1 = 3 * f1
    A2 = 3 * f2 - 6 * f1
    A3 = (f3 - 3*f1) / 4.0
    A4 = (3.0/4.0) * (5*f1 + f3 - 4*f2)
    return A1, A2, A3, A4

def A_square(k, D):
    f1 = f(k, D)
    f2 = f(2*k, D)
    f3 = f(3*k, D)
    f4 = f(4*k, D)
    A1 = 4 * f1
    A2 = 6 * f2 - 12 * f1
    A3 = f3 - 3*f1
    A4 = 15*f1 - 12*f2 + 3*f3
    A5 = 0.5*f4 - f3 - f2 + 3*f1
    A6 = 0.5*f4 - 3*f3 + 7*f2 - 7*f1
    return A1, A2, A3, A4, A5, A6

def A_cubic(k, D):
    f1 = f(k, D)
    f2 = f(2*k, D)
    f3 = f(3*k, D)
    f4 = f(4*k, D)
    f5 = f(5*k, D)
    f6 = f(6*k, D)
    A1 = 6 * f1
    A2 = -30*f1 + 15*f2
    A3 = 5*f3 - 15*f1
    A4 = 75*f1 + 15*f3 - 60*f2
    A5 = -15*f3 + 45*f1 + (15.0/2.0)*f4 - 15*f2
    A6 = -45*f3 - 105*(f1 - f2) + (15.0/2.0)*f4
    A7 = (3.0/8.0)*f5 - (15.0/8.0)*f3 + (15.0/4.0)*f1
    A8 = (45.0/4.0)*f3 - (105.0/2.0)*f1 + (15.0/4.0)*f5 - 15*f4 + 30*f2
    A9 = -(3.0/8.0)*f5 + (15.0/8.0)*f3 - (15.0/4.0)*f1 + (3.0/16.0)*f6 - (3.0/4.0)*f4 + (15.0/16.0)*f2
    A10 = (405.0/8.0)*f3 + (315.0/4.0)*f1 + (15.0/8.0)*f5 - 15*f4 - 90*f2
    A11 = -(5.0/4.0)*f3 + (45.0/2.0)*f1 + (15.0/2.0)*f4 - (135.0/8.0)*f2 - (15.0/4.0)*f5 + (5.0/8.0)*f6
    return A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11

def compute_sum_a(k, D, lattice):
    corr = one_dim_corr(k, D)
    if lattice == 'honeycomb':
        A1, A2, A3, A4 = A_honeycomb(k, D)
        aj = A1 - abs(A2) - abs(A3)*corr + A4
        return 3 * aj - 1.0
    elif lattice == 'square':
        A1, A2, A3, A4, A5, A6 = A_square(k, D)
        aj = A1 - abs(A2) - abs(A3)*corr + A4 + corr*A5 + A6
        return 4 * aj - 1.0
    elif lattice == 'cubic':
        A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11 = A_cubic(k, D)
        aj = A1 - abs(A2) - abs(A3)*corr + A4 + corr*A5 + A6 + A7 + A8 + A9 + A10 + A11
        return 6 * aj - 1.0

def solve_temp(lattice, D):
    def eq(k): return compute_sum_a(k, D, lattice)
    for low, high in [(0.01, 0.5), (0.5, 2.0), (2.0, 5.0)]:
        try:
            res = root_scalar(eq, bracket=[low, high], method='brentq')
            if res.converged:
                k = res.root
                return 1.0 / k
        except ValueError:
            continue
    return np.nan

outdir = os.environ.get('OUTDIR', '/app/outputs')
output_path = os.path.join(outdir, 'critical_temperatures.csv')

with open(output_path, 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['lattice', 'D', 'kTc_over_J'])
    for lattice in ['honeycomb', 'square', 'cubic']:
        for D, Dstr in [(0.0, '0'), (np.inf, 'Inf')]:
            val = solve_temp(lattice, D)
            writer.writerow([lattice, Dstr, val])
PYEOF
