#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: heat_capacity.csv ===
python3 << 'PYEOF' | tee "$OUTDIR/heat_capacity.csv"
import numpy as np
from scipy import integrate
import csv, sys
h = 6.62607015e-34
k = 1.380649e-23
N_A = 6.02214076e23
nu_max = 2.5e11
temps = [0.2, 0.4, 0.6, 0.8, 1.0]
def g(nu):
    return 1.45e-13*nu**2 - 2.75e-37*nu**4
def integrand(nu, T):
    x = h*nu/(k*T)
    return g(nu) * x**2 * np.exp(x) / (np.exp(x)-1)**2
writer = csv.writer(sys.stdout)
writer.writerow(['temperature_K', 'C_v_over_3R'])
for T in temps:
    I, _ = integrate.quad(integrand, 0, nu_max, args=(T,), limit=200)
    cv_3R = I / (3 * N_A)
    writer.writerow([T, cv_3R])
PYEOF
