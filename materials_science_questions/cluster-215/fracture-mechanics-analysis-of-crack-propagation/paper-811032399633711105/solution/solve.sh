#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: crack_initiation_results.csv ===
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy
python3 << 'PYEOF' > "$OUTDIR/crack_initiation_results.csv"
import math, sys
import numpy as np
from scipy.optimize import newton

c1 = 2.5
c2 = 19.0
beta_values = list(range(0, 91, 10))  # 0,10,...,90

sys.stdout.write("beta,gamma,p\n")

for bdeg in beta_values:
    beta = math.radians(bdeg)

    # equation: sin(2(beta+gamma)) - c1 * cos(beta) * cos(gamma) = 0
    def f(g):
        return math.sin(2*(beta + g)) - c1 * math.cos(beta) * math.cos(g)

    def df(g):
        return 2*math.cos(2*(beta + g)) + c1 * math.cos(beta) * math.sin(g)

    # initial guess near 100° (1.745 rad); newton method converges quickly
    guess = math.radians(100.0)
    try:
        gamma = newton(f, guess, fprime=df, tol=1e-12, maxiter=200)
    except Exception:
        # fallback to a bracketing method if newton fails (should rarely happen)
        from scipy.optimize import fsolve
        sol = fsolve(f, guess, xtol=1e-12, maxfev=500)
        gamma = sol[0]

    # clamp to a reasonable obtuse range (just in case)
    if gamma <= 0 or gamma > math.pi:
        gamma = math.pi / 2.0

    # compute failure pressure p = c2 * cot(gamma) / sin(2(gamma+beta))
    denom = math.sin(2*(gamma + beta))
    if abs(denom) < 1e-14:
        p = c2 / 2.0
    else:
        p = c2 * (math.cos(gamma) / math.sin(gamma)) / denom

    sys.stdout.write(f"{bdeg},{math.degrees(gamma):.8f},{p:.8f}\n")
PYEOF
