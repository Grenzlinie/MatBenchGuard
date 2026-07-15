#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: lambda_line.json ===
python3 << 'PYEOF'
with open('/solution/compute_all.py', 'r') as f:
    content = f.read()
content = content.replace('(-1)**hkl_sum', 'np.where(hkl_sum % 2 == 0, 1, -1)')
with open('/solution/compute_all.py', 'w') as f:
    f.write(content)
PYEOF

python3 << 'PYEOF'
import json, os, numpy as np
from scipy.optimize import minimize_scalar

# RPA direct correlation functions (Gaussian pair potentials)
# Unit: R11 = 1
e11 = e22 = 2.0
e12 = 1.8877

# Fourier transform of -beta v_ij(k)
def cij(k, i, j):
    if i == j:
        eps = e11 if i == 0 else e22
        Rij = 1.0 if i == 0 else 0.665
    else:
        eps = e12
        Rij = 0.6
    return -eps * np.pi**1.5 * Rij**3 * np.exp(-0.25 * k**2 * Rij**2)

def D_min(rho, x):
    """Minimum of D(k) over k>0 for given density and concentration."""
    rho1 = rho * (1 - x)
    rho2 = rho * x
    c11_val = lambda k: cij(k, 0, 0)
    c22_val = lambda k: cij(k, 1, 1)
    c12_val = lambda k: cij(k, 0, 1)
    def d(k):
        return (1 - rho1 * c11_val(k)) * (1 - rho2 * c22_val(k)) - rho1 * rho2 * c12_val(k)**2
    res = minimize_scalar(d, bounds=(1e-6, 15), method='bounded')
    return res.fun

# Grid for concentration
xs = np.linspace(0.01, 0.99, 100)
points = []
for x in xs:
    # bracket rho where D_min changes sign
    rho_min, rho_max = 1.0, 50.0
    f_min = D_min(rho_min, x)
    f_max = D_min(rho_max, x)
    if f_min * f_max > 0:
        continue  # no crossing
    # root finding via bisection
    for _ in range(30):
        mid = 0.5 * (rho_min + rho_max)
        f_mid = D_min(mid, x)
        if abs(f_mid) < 1e-6:
            rho_min = rho_max = mid
            break
        if f_min * f_mid > 0:
            rho_min = mid
            f_min = f_mid
        else:
            rho_max = mid
    rho_sol = 0.5 * (rho_min + rho_max)
    points.append({"density": round(rho_sol, 4), "concentration": round(x, 4)})

outdir = os.environ.get("OUTDIR", "/app/outputs")
with open(os.path.join(outdir, "lambda_line.json"), "w") as f:
    json.dump(points, f, indent=2)
PYEOF

# === solve block: coexistence_curve.json ===
python3 /solution/compute_all.py --mode coexistence

# === solve block: lindemann_ratios.json ===
python3 /solution/compute_all.py --mode lindemann

# === solve finalize ===
echo 'All oracle outputs written.'
