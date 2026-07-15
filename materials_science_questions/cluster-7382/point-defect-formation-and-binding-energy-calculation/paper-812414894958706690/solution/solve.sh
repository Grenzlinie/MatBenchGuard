#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: activity_isotherms.csv ===
python3 - <<'PYEOF' > "$OUTDIR/activity_isotherms.csv"
import sys, math
import numpy as np
from scipy.optimize import brentq

R = 8.314
C1 = 6.13 / R
E1_H = 154.3e3
E11 = -3.918e3
C2 = 44.17 / R
E2_H = 78.30e3
E22 = 5.887e3
c = 12

temps = [1173, 1473, 1773, 2073, 2373]
xs = [round(0.9 + i*0.05, 10) for i in range(22)]  # 0.90 .. 1.95

print("x,T,a_c")
for T in temps:
    for x in xs:
        # shift bounds inward to avoid NaN at boundaries
        lb = max(1e-8, x/2 + 1e-8)
        ub = min(1.0 - 1e-8, x - 1e-8)
        if lb >= ub:
            print(f"{x},{T},NaN")
            continue
        def f(theta):
            if theta <= 0 or theta >= 1:
                return np.nan
            ratio = (x - theta) / theta
            if ratio <= 0 or ratio >= 1:
                return np.nan
            log_a1 = math.log(theta/(1-theta)) + C1 + (E1_H + c*theta*E11)/(R*T)
            log_a2 = math.log(ratio/(1-ratio)) + C2 + (E2_H + c*ratio*E22)/(R*T)
            return log_a1 - log_a2
        # grid scan for sign change
        thetas = np.linspace(lb, ub, 200)
        vals = np.array([f(t) for t in thetas])
        root = None
        for i in range(len(thetas)-1):
            fi = vals[i]
            fj = vals[i+1]
            if np.isfinite(fi) and np.isfinite(fj) and fi * fj <= 0:
                try:
                    root = brentq(f, thetas[i], thetas[i+1], xtol=1e-12, maxiter=200)
                except Exception:
                    pass
                if root is not None:
                    break
        if root is None:
            # fallback: point of minimum absolute log-difference
            idx = np.nanargmin(np.abs(vals))
            if np.isfinite(vals[idx]) and abs(vals[idx]) < 1e-3:
                root = thetas[idx]
        if root is not None:
            a_c = math.exp(math.log(root/(1-root)) + C1 + (E1_H + c*root*E11)/(R*T))
        else:
            a_c = float('nan')
        print(f"{x},{T},{a_c}")
PYEOF
