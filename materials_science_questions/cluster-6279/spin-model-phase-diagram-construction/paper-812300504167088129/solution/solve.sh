#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: phase_diagram.csv ===
mkdir -p "$OUTDIR"
python3 - "$OUTDIR" <<'PYEOF'
import numpy as np
from scipy.special import iv
from scipy.integrate import quad
from scipy.optimize import root_scalar
import sys, os, csv

output_dir = sys.argv[1]

# parameters
k_B = 1.0
J1 = 2.0
J2 = -1.0
Jz = 0.0
Tc_XY = (Jz/2 + J1**2 / (8 * abs(J2)) + abs(J2)) / k_B   # 1.5

def P1(z):
    return iv(1, z) / iv(0, z)

def solve_Tc(H):
    if H == 0.0:
        return Tc_XY
    def f(T):
        return T - Tc_XY * (1 + P1(H / T))
    # root bracket: Tc_XY yields negative value, large T positive
    return root_scalar(f, bracket=[Tc_XY, 1000.0], method='brentq').root

def compute_c_and_sin2(T, H):
    beta = 1.0 / T
    h_ = H / T
    max_iter = 2000
    tol = 1e-10
    mixing = 0.3
    n = 6
    # initial guess: small cosine modulation with wavevector q=1/6
    c = 0.1 * np.cos(np.pi * np.arange(n) / 3.0)

    def integrand(phi, xi):
        return np.exp(xi * np.cos(phi) - h_ * (1.0 - np.cos(2.0*phi)))

    def avg_cos(xi):
        f_cos = lambda phi: np.cos(phi) * integrand(phi, xi)
        f_one = lambda phi: integrand(phi, xi)
        num, _ = quad(f_cos, 0, 2*np.pi, limit=200)
        den, _ = quad(f_one, 0, 2*np.pi, limit=200)
        return num / den

    def avg_sin2(xi):
        f_sin2 = lambda phi: np.sin(phi)**2 * integrand(phi, xi)
        f_one  = lambda phi: integrand(phi, xi)
        num, _ = quad(f_sin2, 0, 2*np.pi, limit=200)
        den, _ = quad(f_one, 0, 2*np.pi, limit=200)
        return num / den

    for it in range(max_iter):
        c_old = c.copy()
        xi = np.zeros(n)
        for i in range(n):
            im1 = (i-1) % n
            ip1 = (i+1) % n
            im2 = (i-2) % n
            ip2 = (i+2) % n
            xi[i] = beta * (J1 * (c_old[ip1]+c_old[im1]) + J2 * (c_old[ip2]+c_old[im2]))
            c[i] = avg_cos(xi[i])
        diff = np.max(np.abs(c - c_old))
        c = c_old + mixing * (c - c_old)
        if diff < tol:
            break
    # compute xi_2 (site index 1 corresponds to phi_2)
    i2 = 1
    im1 = (i2-1) % n
    ip1 = (i2+1) % n
    im2 = (i2-2) % n
    ip2 = (i2+2) % n
    xi2 = beta * (J1 * (c[ip1]+c[im1]) + J2 * (c[ip2]+c[im2]))
    sin2 = avg_sin2(xi2)
    return c, sin2

def residual_Tcprime(T, H):
    _, sin2 = compute_c_and_sin2(T, H)
    return T - 2 * sin2 * Tc_XY

def solve_Tcprime(H, Tc):
    eps = 1e-6
    f_low = residual_Tcprime(eps, H)
    f_high = residual_Tcprime(Tc, H)
    if f_low * f_high > 0:
        # no positive root; Tc' = 0
        return 0.0
    else:
        return root_scalar(residual_Tcprime, args=(H,), bracket=[eps, Tc], method='brentq').root

# main
H_vals = np.arange(0.0, 2.05, 0.1)
rows = []
for H in H_vals:
    Tc = solve_Tc(H)
    Tc_prime = solve_Tcprime(H, Tc)
    rows.append((H, Tc, Tc_prime))

csv_path = os.path.join(output_dir, 'phase_diagram.csv')
with open(csv_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['H','Tc','Tc_prime'])
    w.writerows(rows)
PYEOF
