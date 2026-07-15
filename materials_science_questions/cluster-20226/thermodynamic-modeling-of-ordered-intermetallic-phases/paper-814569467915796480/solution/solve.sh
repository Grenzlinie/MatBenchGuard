#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: equilibrium_curves.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 << 'PYEOF'
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar, root_scalar
import os, sys

# ------------------------------------------------------------
# 1.  Accurate α(ω) for fcc precipitate macrolattice
#     by direct reciprocal‑space sum with large cutoff
# ------------------------------------------------------------
M = 80
h = np.arange(-M, M+1, dtype=np.int32)
k = np.arange(-M, M+1, dtype=np.int32)
l = np.arange(-M, M+1, dtype=np.int32)
H, K, L = np.meshgrid(h, k, l, indexing='ij')
Kmag2 = H.astype(np.float64)**2 + K.astype(np.float64)**2 + L.astype(np.float64)**2
even = ((H + K + L) % 2 == 0)
mask = even & (Kmag2 > 0)
Kmag = np.sqrt(Kmag2[mask])
del H, K, L, Kmag2   # free memory

omega_grid = np.linspace(1e-4, 0.5, 300)
alpha_arr = np.empty_like(omega_grid)
pi = np.pi
for i, w in enumerate(omega_grid):
    beta = (3*w)**(1/3) * pi**(2/3) / (2**(1/3))
    y = beta * Kmag
    y = np.where(y < 1e-12, 1e-12, y)
    term = ((3*(y*np.cos(y) - np.sin(y))/y**3)**2) / y**2
    S = np.sum(term)
    alpha_arr[i] = 3 * w * S

alpha_spline = interp1d(omega_grid, alpha_arr, kind='cubic',
                        bounds_error=False, fill_value='extrapolate')

# ------------------------------------------------------------
# 2.  Free‑energy minimisation for ξ = 0.5
# ------------------------------------------------------------
xi = 0.5
g_max = 0.4725   # max of x^{1/3}(1-x)

def get_x(omega):
    a = alpha_spline(omega)
    C = xi * a**(1/3) / (3 * (1-omega))
    if C >= g_max:
        return None
    f = lambda x: x**(1/3) * (1-x) - C
    try:
        res = root_scalar(f, bracket=[0.25, 1.0], method='brentq')
        return res.root if res.converged else None
    except:
        return None

def fe(omega, omega0):
    if omega <= 1e-10:
        return 0.5 * omega0**2
    x = get_x(omega)
    if x is None:
        return np.inf
    f = 1.5 * x * (1-x) * omega * (1-omega)
    f += 0.5 * omega * (1 - omega0 - (1-omega)*x)**2
    f += 0.5 * (1-omega) * (omega0 - omega*x)**2
    return f

# ------------------------------------------------------------
# 3.  Compute equilibrium curves for ω₀ = 0 .. 0.5  (step 0.01)
# ------------------------------------------------------------
omega0_vals = np.arange(0.0, 0.51, 0.01)
rows = []

for w0 in omega0_vals:
    if w0 < 1e-12:
        rows.append((w0, 0.0, 0.0, 0.0))
        continue
    # coarse grid search
    omegas = np.linspace(1e-4, 0.5, 2000)
    fgrid = [fe(o, w0) for o in omegas]
    f0 = 0.5 * w0**2
    idx_min = np.argmin(fgrid)
    if fgrid[idx_min] >= f0 - 1e-10:
        rows.append((w0, 0.0, 0.0, 0.0))
        continue
    # local refinement via bounded minimisation
    low = max(1e-4, omegas[idx_min] - 0.05)
    high = min(0.5, omegas[idx_min] + 0.05)
    res = minimize_scalar(fe, bounds=(low, high), method='bounded', args=(w0,))
    if not res.success:
        rows.append((w0, 0.0, 0.0, 0.0))
        continue
    w_eq = res.x
    x_eq = get_x(w_eq)
    if x_eq is None or x_eq <= 0:
        rows.append((w0, 0.0, 0.0, 0.0))
        continue
    a_eq = alpha_spline(w_eq)
    R_eq_norm = x_eq**(-2/3) * a_eq**(-1/3)
    rows.append((w0, w_eq, x_eq, R_eq_norm))

# ------------------------------------------------------------
# 4.  Write CSV
# ------------------------------------------------------------
outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, 'equilibrium_curves.csv')
with open(path, 'w') as f:
    f.write('omega0,omega_eq,x_eq,R_eq_norm\n')
    for r in rows:
        f.write(','.join(f'{v:.10f}' for v in r) + '\n')
PYEOF
