#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: lattice_deformation.json ===
python3 << 'PYEOF' > $OUTDIR/lattice_deformation.json
import json, math, sys
from scipy.optimize import root

# physical constants (cgs)
e = 4.803e-10
l_cm = 2.0e-8
s = 9
t = 6
n = 2.06

# overlap and vdW coefficients
lam_OT = 15.6e-82; mu_OT = 31.3e-60
lam_OO = 113.5e-82; mu_OO = 135.0e-60
lam_BO = 99.0e-82; mu_BO = 162.0e-60
lam_BB = 82.7e-82; mu_BB = 239.0e-60
lam_BT = 12.0e-82; mu_BT = 43.0e-60
lam_TT = 1.1e-82; mu_TT = 10.0e-60
pi = math.pi

# ionic polarisabilities (Anderson & Shockley)
alpha_Ti = (0.0365 / (4*pi)) * (2*l_cm)**3

# dipole coefficient a0' (negative)
a0p = -0.1974 * (n * e)**2 / (2.0 * alpha_Ti)
k_sens = 7.30

def a_coeff(da, db):
    return (5.123e5 - 7.130e6 * da + 2 * 6.954e5 * db
            + 4.340e7 * da**2 - 2 * 4.2605e6 * db**2)

def b_coeff(da, db):
    return (1.895e22 - 2.374e23 * da - 2 * 5.760e21 * db
            + 1.673e24 * da**2 + 2 * 4.087e22 * db**2)

def a_prime(da):
    return a0p * (1.0 - k_sens * da)

def da_dda(da, db):
    return -7.130e6 + 2 * 4.340e7 * da

def da_ddb(da, db):
    return 2 * 6.954e5 - 4 * 4.2605e6 * db

def db_dda(da, db):
    return -2.374e23 + 2 * 1.673e24 * da

def db_ddb(da, db):
    return -2 * 5.760e21 + 4 * 4.087e22 * db

def dU1_dda(da, db):
    l = l_cm
    val = (-2*s*lam_OT*l**(-s) * (1.0 - (s+1)*da)
           + 2*t*mu_OT*l**(-t) * (1.0 - (t+1)*da))
    fac1_s = s*(4*lam_OO+4*lam_BO)*l**(-s) * (2.0**(-s/2))
    fac1_t = t*(4*mu_OO+4*mu_BO)*l**(-t) * (2.0**(-t/2))
    val -= fac1_s * (1.0 - s/2*da - (s+2)/4 * 2*db)
    val += fac1_t * (1.0 - t/2*da - (t+2)/4 * 2*db)
    fac2_s = 8*s*lam_BT*l**(-s) * (3.0**(-(s+2)/2))
    fac2_t = 8*t*mu_BT*l**(-t) * (3.0**(-(t+2)/2))
    val -= fac2_s * (1.0 - (s-1)/3*da - (s+2)/3 * 2*db)
    val += fac2_t * (1.0 - (t-1)/3*da - (t+2)/3 * 2*db)
    fac3_s = s*(3*lam_OO+lam_BB+lam_TT) * (2*l)**(-s)
    fac3_t = t*(3*mu_OO+mu_BB+mu_TT) * (2*l)**(-t)
    val -= fac3_s * (1.0 - (s+1)*da)
    val += fac3_t * (1.0 - (t+1)*da)
    # Coulomb
    val += 49.1 * e**2 / (6.0*l) * (1.0 - 2*da)
    return val

def dU1_ddb1(da, db1, db2):
    l = l_cm
    val = (-2*s*lam_OT*l**(-s) * (1.0 - (s+1)*db1)
           + 2*t*mu_OT*l**(-t) * (1.0 - (t+1)*db1))
    fac1_s = s*(4*lam_OO+4*lam_BO)*l**(-s) * (2.0**(-s/2))
    fac1_t = t*(4*mu_OO+4*mu_BO)*l**(-t) * (2.0**(-t/2))
    val -= fac1_s * (1.0 - s/2*db1 - (s+2)/4*(db2+da))
    val += fac1_t * (1.0 - t/2*db1 - (t+2)/4*(db2+da))
    fac2_s = 8*s*lam_BT*l**(-s) * (3.0**(-(s+2)/2))
    fac2_t = 8*t*mu_BT*l**(-t) * (3.0**(-(t+2)/2))
    val -= fac2_s * (1.0 - (s-1)/3*db1 - (s+2)/3*(db2+da))
    val += fac2_t * (1.0 - (t-1)/3*db1 - (t+2)/3*(db2+da))
    fac3_s = s*(3*lam_OO+lam_BB+lam_TT) * (2*l)**(-s)
    fac3_t = t*(3*mu_OO+mu_BB+mu_TT) * (2*l)**(-t)
    val -= fac3_s * (1.0 - (s+1)*db1)
    val += fac3_t * (1.0 - (t+1)*db1)
    # Coulomb
    val += 49.1 * e**2 / (6.0*l) * (1.0 - 2*db1)
    return val

def eq_system(vars):
    da, db = vars
    ap = a_prime(da)
    a = a_coeff(da, db)
    b = max(b_coeff(da, db), 1e-30)  # avoid zero div
    if ap + a >= 0:
        f1 = dU1_dda(da, db)
        f2 = dU1_ddb1(da, db, db)
        return [f1, f2]
    f1 = dU1_dda(da, db) \
         - (ap + a) / (2.0*b) * ( (-k_sens * a0p) + da_dda(da, db) ) \
         + (ap + a)**2 / (4.0 * b**2) * db_dda(da, db)
    f2 = dU1_ddb1(da, db, db) \
         - (ap + a) / (2.0*b) * ( 0.0 + da_ddb(da, db) ) \
         + (ap + a)**2 / (4.0 * b**2) * db_ddb(da, db)
    return [f1, f2]

# Solve with multiple initial guesses
guesses = [[0.02, 0.005], [0.03, 0.002], [0.015, 0.006], [0.01, 0.008]]
sol = None
for idx, guess in enumerate(guesses):
    res = root(eq_system, guess, method='lm', tol=1e-12)
    if res.success:
        sol = res.x
        break
if sol is None:
    # fallback to fsolve
    from scipy.optimize import fsolve
    sol = fsolve(eq_system, [0.02, 0.005], xtol=1e-12, maxfev=2000)

da_sol, db_sol = sol

ap_sol = a_prime(da_sol)
a_sol = a_coeff(da_sol, db_sol)
b_sol = b_coeff(da_sol, db_sol)

disc = -(ap_sol + a_sol) / (2.0 * b_sol) if b_sol > 0 else -1.0
if disc > 0:
    x_cm = math.sqrt(disc)
else:
    x_cm = 0.0
x_ang = x_cm / 1e-8

result = {
    "delta_a": float(da_sol),
    "delta_b": float(db_sol),
    "ti_shift": float(x_ang)
}
# Ensure no NaN/Inf in output
for k, v in result.items():
    if not math.isfinite(v):
        result[k] = 0.0
json.dump(result, sys.stdout, allow_nan=False)
PYEOF
