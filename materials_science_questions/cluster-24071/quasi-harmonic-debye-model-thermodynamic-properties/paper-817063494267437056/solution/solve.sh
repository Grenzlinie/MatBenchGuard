#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: cv_curves.csv ===
cat > /tmp/compute_cv.py << 'PYEOF'
import numpy as np
from scipy.integrate import quad
from scipy.constants import hbar, k, R
import csv
import sys

output_path = sys.argv[1]

eV_to_J = 1.602176634e-19

materials = [
    ('diamond', 2239.6, 2.932e14, 3.68, 75),
    ('silicon', 648.9, 0.850e14, 2.32, 165),
    ('germanium', 373.4, 0.489e14, 1.94, 240)
]

ranges = {
    'diamond': (0.1, 2000.0, 10.0),
    'silicon': (0.1, 1500.0, 10.0),
    'germanium': (0.1, 1500.0, 10.0)
}

def compute_cv(mat_name, theta_D, omega_D, D_eV, N_given, T_min, T_max, step):
    D_J = D_eV * eV_to_J
    N = N_given

    def E_n_omega(n, omega):
        return hbar * omega * (n + 0.5) - (hbar**2 * omega**2) / (4 * D_J) * (n + 0.5)**2

    def Z_omega_T(omega, T):
        # scalar version for quad
        s = 0.0
        for n in range(N+1):
            arg = E_n_omega(n, omega) / (k * T)
            # cap large values to avoid overflow (not strictly necessary)
            if arg > 700:
                continue
            s += np.exp(-arg)
        return s

    def integrand(omega, T):
        Z_val = Z_omega_T(omega, T)
        if Z_val <= 0:
            return 0.0
        return omega**2 * np.log(Z_val)

    def F_single(T):
        if T == 0.0:
            return 0.0
        integral, _ = quad(integrand, 0, omega_D, args=(T,), limit=200)
        return - (9 * R * T / omega_D**3) * integral

    Ts = np.arange(T_min, T_max + step, step)
    h = 1.0
    Ts_out = [0.0]
    Cv_out = [0.0]

    for T in Ts:
        if T < h:
            Cv_val = 0.0
        else:
            Fp = F_single(T + h)
            Fm = F_single(T - h)
            F0 = F_single(T)
            d2F = (Fp - 2*F0 + Fm) / (h**2)
            Cv_val = - T * d2F
        Ts_out.append(T)
        Cv_out.append(Cv_val)
    return Ts_out, Cv_out

all_rows = []
for mat_name, theta_D, omega_D, D_eV, N in materials:
    T_min, T_max, step = ranges[mat_name]
    Ts, Cv = compute_cv(mat_name, theta_D, omega_D, D_eV, N, T_min, T_max, step)
    for t, c in zip(Ts, Cv):
        all_rows.append([mat_name, t, c])

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['material', 'temperature_K', 'Cv_J_per_mol_K'])
    writer.writerows(all_rows)
PYEOF
python3 /tmp/compute_cv.py "$OUTDIR/cv_curves.csv"
