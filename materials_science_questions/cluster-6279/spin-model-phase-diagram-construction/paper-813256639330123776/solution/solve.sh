#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: tricritical_points_bimodal.csv ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

python3 - "$OUTDIR" << 'PYEOF'
import sys, csv, math, numpy as np
from scipy.optimize import fsolve

def comb(n,k):
    return math.comb(n,k)

def f(a1, a2, H1, H2, Jx, Jy, Jz, beta):
    t = a1 + a2 + H1 + H2
    X0 = math.sqrt((Jx-Jy)**2 + t**2)
    Y0 = math.sqrt((Jx+Jy)**2 + (a1 - a2 + H1 - H2)**2)
    if X0 < 1e-12:
        bY0 = beta * Y0
        if bY0 > 700.0:
            return 0.0
        cosh_bY0 = math.cosh(bY0)
        return t * beta / (1.0 + math.exp(-2*beta*Jz) * cosh_bY0)
    tanh_bX0 = math.tanh(beta * X0)
    exp_term = math.exp(-2 * beta * Jz)
    log_ratio = beta * (Y0 - X0)
    if log_ratio > 700.0:
        return 0.0
    ratio_num = 1.0 + math.exp(-2 * beta * Y0)
    ratio_den = 1.0 + math.exp(-2 * beta * X0)
    ratio = math.exp(log_ratio) * ratio_num / ratio_den
    denom = 1.0 + exp_term * ratio
    return (t / X0) * tanh_bX0 / denom

def theta_prime_single(p, q, r, z0, z1, H1, H2, Jx, Jy, Jz, beta):
    total = 0.0
    const = 2**(-(2*z0 + z1))
    for t1 in range(z0 - p + 1):
        for v1 in range(p + 1):
            for t2 in range(z0 - q + 1):
                for v2 in range(q + 1):
                    for t3 in range(z1 - r + 1):
                        for v3 in range(r + 1):
                            K = comb(z0-p, t1) * comb(p, v1) * comb(z0-q, t2) * comb(q, v2) * comb(z1-r, t3) * comb(r, v3)
                            K *= (-1)**(v1+v2+v3)
                            a1 = (z0 - 2*t1 - 2*v1 + z1 - 2*t3 - 2*v3) * Jz
                            a2 = (z0 - 2*t2 - 2*v2 + z1 - 2*t3 - 2*v3) * Jz
                            total += K * f(a1, a2, H1, H2, Jx, Jy, Jz, beta)
    return total * const

def compute_Ck(z0, z1, rx, ry, w, H0, T, max_k):
    Jz = 1.0
    Jx = rx
    Jy = ry
    beta = 1.0 / T
    C = np.zeros(max_k + 1)
    H_vals = [H0, -H0]
    for p in range(z0+1):
        for q in range(z0+1):
            for r in range(z1+1):
                k = p+q+r
                if 1 <= k <= max_k and k % 2 == 1:
                    coeff = comb(z0, p) * comb(z0, q) * comb(z1, r)
                    theta_sum = 0.0
                    for H1 in H_vals:
                        for H2 in H_vals:
                            theta_sum += theta_prime_single(p, q, r, z0, z1, H1, H2, Jx, Jy, Jz, beta)
                    C[k] += coeff * theta_sum / 4.0
    return C

def eqs(vars, z0, z1, rx, ry):
    H0, T = vars[0], vars[1]
    C = compute_Ck(z0, z1, rx, ry, 0.0, H0, T, 3)
    return [C[1] - 1.0, C[3]]

def solve_tricritical(z0, z1, rx, ry):
    guess = [2.0, 2.5]
    if z0 == 5 and rx==1.0 and ry==1.0:
        guess = [2.3, 2.7]
    elif z0 == 7 and rx==1.0 and ry==1.0:
        guess = [2.8, 3.0]
    try:
        sol = fsolve(eqs, guess, args=(z0, z1, rx, ry), xtol=1e-12, maxfev=2000)
        H0_sol, T_sol = sol[0], sol[1]
    except Exception:
        try:
            sol = fsolve(eqs, [1.5, 2.0], args=(z0, z1, rx, ry), xtol=1e-12, maxfev=2000)
            H0_sol, T_sol = sol[0], sol[1]
        except:
            print("Warning: fsolve failed for", z0, rx, ry)
            return None, None
    return H0_sol, T_sol

OUTDIR = sys.argv[1]
rows = []
r_y_vals = [1.0, 1.5, 2.0]
for name, z0, z1 in [('SC',5,0), ('BCC',7,0)]:
    for ry in r_y_vals:
        H0, Tc = solve_tricritical(z0, z1, 1.0, ry)
        if H0 is not None:
            rows.append([name, ry, round(H0,6), round(Tc,6)])
        else:
            print(f"Failure for {name} ry={ry}")

with open(f"{OUTDIR}/tricritical_points_bimodal.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["lattice","r_y","H0_over_J","kBTc_over_J"])
    writer.writerows(rows)

# Write the shared compute module used by the next block
compute_code = '''
import math
import numpy as np
from scipy.optimize import fsolve

def comb(n,k):
    return math.comb(n,k)

def f(a1, a2, H1, H2, Jx, Jy, Jz, beta):
    t = a1 + a2 + H1 + H2
    X0 = math.sqrt((Jx-Jy)**2 + t**2)
    Y0 = math.sqrt((Jx+Jy)**2 + (a1 - a2 + H1 - H2)**2)
    if X0 < 1e-12:
        bY0 = beta * Y0
        if bY0 > 700.0:
            return 0.0
        cosh_bY0 = math.cosh(bY0)
        return t * beta / (1.0 + math.exp(-2*beta*Jz) * cosh_bY0)
    tanh_bX0 = math.tanh(beta * X0)
    exp_term = math.exp(-2 * beta * Jz)
    log_ratio = beta * (Y0 - X0)
    if log_ratio > 700.0:
        return 0.0
    ratio_num = 1.0 + math.exp(-2 * beta * Y0)
    ratio_den = 1.0 + math.exp(-2 * beta * X0)
    ratio = math.exp(log_ratio) * ratio_num / ratio_den
    denom = 1.0 + exp_term * ratio
    return (t / X0) * tanh_bX0 / denom

def theta_prime_single(p, q, r, z0, z1, H1, H2, Jx, Jy, Jz, beta):
    total = 0.0
    const = 2**(-(2*z0 + z1))
    for t1 in range(z0 - p + 1):
        for v1 in range(p + 1):
            for t2 in range(z0 - q + 1):
                for v2 in range(q + 1):
                    for t3 in range(z1 - r + 1):
                        for v3 in range(r + 1):
                            K = comb(z0-p, t1) * comb(p, v1) * comb(z0-q, t2) * comb(q, v2) * comb(z1-r, t3) * comb(r, v3)
                            K *= (-1)**(v1+v2+v3)
                            a1 = (z0 - 2*t1 - 2*v1 + z1 - 2*t3 - 2*v3) * Jz
                            a2 = (z0 - 2*t2 - 2*v2 + z1 - 2*t3 - 2*v3) * Jz
                            total += K * f(a1, a2, H1, H2, Jx, Jy, Jz, beta)
    return total * const

def compute_Ck(z0, w, H0, T, Jx, Jy, max_k):
    z1 = 0
    Jz = 1.0
    beta = 1.0 / T
    C = np.zeros(max_k + 1)
    pairs = [
        (0.0, 0.0, w*w),
        (H0, H0, ((1-w)/2)**2),
        (-H0, -H0, ((1-w)/2)**2),
        (H0, -H0, ((1-w)/2)**2),
        (-H0, H0, ((1-w)/2)**2),
        (0.0, H0, w*(1-w)/2),
        (0.0, -H0, w*(1-w)/2),
        (H0, 0.0, w*(1-w)/2),
        (-H0, 0.0, w*(1-w)/2)
    ]
    for p in range(z0+1):
        for q in range(z0+1):
            for r in range(z1+1):
                k = p+q+r
                if k <= max_k and k % 2 == 1:
                    coeff = comb(z0, p) * comb(z0, q) * comb(z1, r)
                    theta_sum = 0.0
                    for H1, H2, weight in pairs:
                        theta_sum += weight * theta_prime_single(p, q, r, z0, z1, H1, H2, Jx, Jy, Jz, beta)
                    C[k] += coeff * theta_sum
    return C

def compute_w_star(z0, rx, ry, T_low=0.001, tol=1e-6):
    Jx = rx
    Jy = ry

    def has_root(w):
        def eq(H0):
            C = compute_Ck(z0, w, H0, T_low, Jx, Jy, max_k=1)
            return C[1] - 1.0
        H0_vals = np.linspace(0.0, 10.0, 200)
        # loop over H0 values to avoid vectorised call that fails with math.sqrt
        for i in range(len(H0_vals)-1):
            if eq(H0_vals[i]) * eq(H0_vals[i+1]) <= 0:
                return True
        return False

    lo, hi = 0.0, 1.0
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if has_root(mid):
            lo = mid
        else:
            hi = mid
    return lo
'''

with open('/solution/compute.py', 'w') as f:
    f.write(compute_code)
PYEOF

# === solve block: w_star_trimodal.csv ===
python3 -c "
import sys, csv
sys.path.insert(0,'/solution')
from compute import compute_w_star

w_star = compute_w_star(z0=5, rx=1.0, ry=1.0)
with open('/app/outputs/w_star_trimodal.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['lattice','r_x','r_y','w_star'])
    writer.writerow(['SC', 1.0, 1.0, round(w_star,6)])
"
