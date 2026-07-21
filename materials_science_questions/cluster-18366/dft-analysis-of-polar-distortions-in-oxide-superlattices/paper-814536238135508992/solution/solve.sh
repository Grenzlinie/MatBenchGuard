#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: tc_vs_ns.csv ===
python3 - "$OUTDIR/tc_vs_ns.csv" << 'PYEOF'
import numpy as np
import sys

# Physical constants and calibrated parameters
m1, m2, m3 = 1.8, 3.5, 6.0
ratio_m2 = m2 / m1
ratio_m3 = m3 / m1
x_c1 = 6.1   # dimensionless variable at n_c1 = 1.2e18 cm^{-3}
x_c2 = 20.0  # at n_c2 = 2.5e19 cm^{-3}

# Calibration from first-band experimental maximum
T_cmax_exp = 0.2  # K, at n_s ≈ 2e18 cm^{-3}
x_max1 = 7.18
T_bar1_max = x_max1**2 * np.exp(-x_max1 / np.log1p(x_max1))
A = T_cmax_exp / T_bar1_max  # overall prefactor

def bisect_root(f, a, b, args=(), tol=1e-12, max_iter=200):
    """Bisection root finder; returns a root even if f(a)*f(b) <= 0 initially by expanding bracket."""
    fa = f(a, *args)
    fb = f(b, *args)
    # Ensure a < b and sign change
    if a > b:
        a, b = b, a
        fa, fb = fb, fa
    if fa * fb <= 0:
        pass  # already bracketed
    else:
        # expand bracket
        scale = 1.5
        for _ in range(max_iter):
            if abs(fa) < abs(fb):
                a = a - scale * (b - a)
                fa = f(a, *args)
            else:
                b = b + scale * (b - a)
                fb = f(b, *args)
            if fa * fb <= 0:
                break
        else:
            # fallback to linear interpolation if no sign change after expansion
            return a  # safe fallback; shouldn't happen for monotonic functions
    # Bisection
    for _ in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c, *args)
        if fc == 0.0 or (b - a) / 2.0 < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2.0

def F2(x, ns_18):
    return x**3 + ratio_m2**1.5 * (x**2 - x_c1**2)**1.5 - 195.0 * ns_18

def F3(x, ns_18):
    return x**3 + ratio_m2**1.5 * (x**2 - x_c1**2)**1.5 + ratio_m3**1.5 * (x**2 - x_c2**2)**1.5 - 195.0 * ns_18

def solve_x(n_s):
    """Map n_s (cm^{-3}) to dimensionless x."""
    ns_18 = n_s * 1e-18
    # Single-band regime
    if n_s <= 1.2e18:
        return 5.74 * ns_18 ** (1.0/3.0)
    # Try two-band root
    guess = 5.74 * ns_18 ** (1.0/3.0)
    a = x_c1  # lower bound exactly at x_c1 to avoid complex (x**2 - x_c1**2)**1.5
    b = max(guess * 1.5, 30.0)
    x2_root = bisect_root(F2, a, b, args=(ns_18,))
    if x2_root <= x_c2:
        return max(x2_root, x_c1)
    # Three-band root
    a3 = x_c2  # lower bound exactly at x_c2
    b3 = max(guess * 1.5, 60.0)
    x3_root = bisect_root(F3, a3, b3, args=(ns_18,))
    return max(x3_root, x_c2)

def safe_exp_minus_inv(lam):
    """Return exp(-1/lam) safely, avoiding division by zero and negative lam."""
    if lam <= 0.0:
        return 0.0
    return np.exp(-1.0 / lam)

def compute_for_ns(n_s):
    x = solve_x(n_s)
    # Band 1
    lam1 = np.log1p(x) / x  # ln(1+x)/x
    T_C1 = A * x**2 * safe_exp_minus_inv(lam1)

    # Band 2
    T_C2 = 0.0
    if x > x_c1:
        x2 = np.sqrt(max(0.0, ratio_m2 * (x**2 - x_c1**2)))
        if x2 > 1e-12:
            denom = m1 * x + m2 * x2
            if denom > 0:
                lam2 = (ratio_m2 / x2) * np.log1p((m1 * x2**2) / denom)
                T_bar2 = (m1 / m2) * x2**2 * safe_exp_minus_inv(lam2)
                T_C2 = A * T_bar2

    # Band 3
    T_C3 = 0.0
    if x > x_c2:
        x2 = np.sqrt(max(0.0, ratio_m2 * (x**2 - x_c1**2)))
        x3 = np.sqrt(max(0.0, ratio_m3 * (x**2 - x_c2**2)))
        if x3 > 1e-12:
            denom = m1 * x + m2 * x2 + m3 * x3
            if denom > 0:
                lam3 = (ratio_m3 / x3) * np.log1p((m1 * x3**2) / denom)
                T_bar3 = (m1 / m3) * x3**2 * safe_exp_minus_inv(lam3)
                T_C3 = A * T_bar3

    return T_C1, T_C2, T_C3

# Generate n_s range
n_base = np.logspace(np.log10(0.3e18), np.log10(2e21), 400)
n_extra = np.concatenate([
    np.linspace(0.5e18, 1.2e18, 20),
    np.linspace(1.21e18, 2e19, 30),
    np.linspace(2e19, 5e20, 40)
])
n_samples = np.unique(np.sort(np.concatenate([n_base, n_extra])))

lines = ['n_s,T_C_1,T_C_2,T_C_3']
for n in n_samples:
    T1, T2, T3 = compute_for_ns(n)
    lines.append(f'{n:.6e},{T1:.8e},{T2:.8e},{T3:.8e}')

with open(sys.argv[1], 'w') as f:
    f.write('\n'.join(lines) + '\n')

# Write reusable /solution/run.py for maxima block
with open('/solution/run.py', 'w') as rf:
    rf.write(r'''
import numpy as np
import sys
import os

# same parameters
m1, m2, m3 = 1.8, 3.5, 6.0
ratio_m2 = m2 / m1
ratio_m3 = m3 / m1
x_c1 = 6.1
x_c2 = 20.0
T_cmax_exp = 0.2
x_max1 = 7.18
T_bar1_max = x_max1**2 * np.exp(-x_max1 / np.log1p(x_max1))
A = T_cmax_exp / T_bar1_max

def bisect_root(f, a, b, args=(), tol=1e-12, max_iter=200):
    fa = f(a, *args)
    fb = f(b, *args)
    if a > b:
        a, b = b, a
        fa, fb = fb, fa
    if fa * fb <= 0:
        pass
    else:
        scale = 1.5
        for _ in range(max_iter):
            if abs(fa) < abs(fb):
                a = a - scale * (b - a)
                fa = f(a, *args)
            else:
                b = b + scale * (b - a)
                fb = f(b, *args)
            if fa * fb <= 0:
                break
        else:
            return a
    for _ in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c, *args)
        if fc == 0.0 or (b - a) / 2.0 < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2.0

def F2(x, ns_18):
    return x**3 + ratio_m2**1.5 * (x**2 - x_c1**2)**1.5 - 195.0 * ns_18

def F3(x, ns_18):
    return x**3 + ratio_m2**1.5 * (x**2 - x_c1**2)**1.5 + ratio_m3**1.5 * (x**2 - x_c2**2)**1.5 - 195.0 * ns_18

def solve_x(n_s):
    ns_18 = n_s * 1e-18
    if n_s <= 1.2e18:
        return 5.74 * ns_18 ** (1.0/3.0)
    guess = 5.74 * ns_18 ** (1.0/3.0)
    a = x_c1
    b = max(guess * 1.5, 30.0)
    x2_root = bisect_root(F2, a, b, args=(ns_18,))
    if x2_root <= x_c2:
        return max(x2_root, x_c1)
    a3 = x_c2
    b3 = max(guess * 1.5, 60.0)
    x3_root = bisect_root(F3, a3, b3, args=(ns_18,))
    return max(x3_root, x_c2)

def safe_exp_minus_inv(lam):
    if lam <= 0.0:
        return 0.0
    return np.exp(-1.0 / lam)

def compute_for_ns(n_s):
    x = solve_x(n_s)
    lam1 = np.log1p(x) / x
    T_C1 = A * x**2 * safe_exp_minus_inv(lam1)
    T_C2 = 0.0
    if x > x_c1:
        x2 = np.sqrt(max(0.0, ratio_m2 * (x**2 - x_c1**2)))
        if x2 > 1e-12:
            denom = m1 * x + m2 * x2
            if denom > 0:
                lam2 = (ratio_m2 / x2) * np.log1p((m1 * x2**2) / denom)
                T_bar2 = (m1 / m2) * x2**2 * safe_exp_minus_inv(lam2)
                T_C2 = A * T_bar2
    T_C3 = 0.0
    if x > x_c2:
        x2 = np.sqrt(max(0.0, ratio_m2 * (x**2 - x_c1**2)))
        x3 = np.sqrt(max(0.0, ratio_m3 * (x**2 - x_c2**2)))
        if x3 > 1e-12:
            denom = m1 * x + m2 * x2 + m3 * x3
            if denom > 0:
                lam3 = (ratio_m3 / x3) * np.log1p((m1 * x3**2) / denom)
                T_bar3 = (m1 / m3) * x3**2 * safe_exp_minus_inv(lam3)
                T_C3 = A * T_bar3
    return T_C1, T_C2, T_C3

def write_maxima(out_path):
    ns = np.logspace(np.log10(0.3e18), np.log10(2e21), 2000)
    max1 = (0.0, 0.0)
    max2 = (0.0, 0.0)
    max3 = (0.0, 0.0)
    for n in ns:
        T1, T2, T3 = compute_for_ns(n)
        if T1 > max1[1]:
            max1 = (n, T1)
        if T2 > max2[1]:
            max2 = (n, T2)
        if T3 > max3[1]:
            max3 = (n, T3)
    with open(out_path, 'w') as f:
        f.write('band,n_s_max,T_C_max\n')
        f.write(f'1,{max1[0]:.6e},{max1[1]:.8e}\n')
        f.write(f'2,{max2[0]:.6e},{max2[1]:.8e}\n')
        f.write(f'3,{max3[0]:.6e},{max3[1]:.8e}\n')

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] != 'maxima':
        print('Usage: run.py maxima <outfile>', file=sys.stderr)
        sys.exit(1)
    write_maxima(sys.argv[2])
''')
PYEOF

# === solve block: maxima.csv ===
python3 /solution/run.py maxima "$OUTDIR/maxima.csv"
