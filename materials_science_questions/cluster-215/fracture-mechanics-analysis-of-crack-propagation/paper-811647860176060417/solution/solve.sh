#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/helper.py

# === solve block: I_vs_x0.csv ===
python3 << 'PYEOF' > "$OUTDIR/I_vs_x0.csv"
import scipy.integrate as integrate
import numpy as np

def F(x):
    return 1.107 - 1.65*x + 0.93*x**2

def integrand(x, x0, n):
    factor = (np.sqrt(x0) * F(x0)) ** n
    return factor / ( (np.sqrt(x) * F(x)) ** n )

x0_vals = [0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
n_vals = [5, 10, 20]

print("x0,n,I_value")
for n in n_vals:
    for x0 in x0_vals:
        I, _ = integrate.quad(integrand, x0, 1, args=(x0, n), limit=200)
        print(f"{x0},{n},{I:.12f}")
PYEOF

# === solve block: scaling_verification.csv ===
python3 << 'PYEOF' > "$OUTDIR/scaling_verification.csv"
import scipy.integrate as integrate
import numpy as np

def F(x):
    # geometry factor for three-point bend S=4W
    return 1.107 - 1.65*x + 0.93*x**2

def integral_I(x0, n):
    # I = ∫_{x0}^{1} [ sqrt(x0)*F(x0) / (sqrt(x)*F(x)) ]^n dx
    def integrand(x):
        return (np.sqrt(x0) * F(x0) / (np.sqrt(x) * F(x)))**n
    I, _ = integrate.quad(integrand, x0, 1, limit=200)
    return I

# fixed parameters
Kstar = 1.0      # reference stress intensity
a_star = 1.0     # reference crack length
n = 16           # crack-growth exponent (typical for glass, as in paper)
K_Ii_fixed = 1.0 # arbitrary fixed initial stress intensity

rows = []

# Large-crack regime: fix x0 (nondimensional crack length) > 0.05, vary W
# T_f ∝ W is expected when x0 is held constant.
x0_large = 0.2
for W in [1.0, 2.0, 4.0, 8.0, 16.0]:
    a0 = x0_large * W   # keep x0 constant
    I_val = integral_I(x0_large, n)
    # nondimensional failure time T_f from Eq.(8)
    T_f = (W * I_val) / (a_star * (K_Ii_fixed / Kstar)**n)
    rows.append((W, a0, K_Ii_fixed, T_f))

# Small-crack regime: fix W and K_Ii, vary a0 (so x0 < 0.05)
# T_f ∝ a0 is expected.
W_small = 1.0
for a0 in [0.01, 0.02, 0.03, 0.04, 0.05]:
    x0 = a0 / W_small
    I_val = integral_I(x0, n)
    T_f = (W_small * I_val) / (a_star * (K_Ii_fixed / Kstar)**n)
    rows.append((W_small, a0, K_Ii_fixed, T_f))

print("W,a0,K_Ii,T_f")
for W, a0, K_Ii, Tf in rows:
    print(f"{W},{a0},{K_Ii},{Tf:.12f}")
PYEOF
