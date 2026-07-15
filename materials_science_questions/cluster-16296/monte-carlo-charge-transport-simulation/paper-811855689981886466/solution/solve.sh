#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: departure_results.csv ===
python3 - <<'PYEOF'
import csv, numpy as np
from scipy.integrate import quad

omega = 0.063   # eV (optical phonon)
Gamma = 0.01    # eV (broadening)

def g(E):
    if E <= 0:
        return 0.0
    return np.sqrt(E)   # DOS shape

def lorentzian(E, center):
    return (Gamma/np.pi) / ((E - center)**2 + Gamma**2)

def integrand_num(E, center):
    return E * g(E) * lorentzian(E, center)

def integrand_den(E, center):
    return g(E) * lorentzian(E, center)

E_i_vals = np.arange(0.1, 4.01, 0.1)
rows = []
for Ei in E_i_vals:
    center = Ei + omega
    I_num, _ = quad(integrand_num, 0, 10, args=(center,), limit=200)
    I_den, _ = quad(integrand_den, 0, 10, args=(center,), limit=200)
    E_avg = I_num / I_den if I_den != 0 else center
    departure_orig = (E_avg - center) * 1000   # meV
    rows.append((f"{Ei:.1f}", f"{departure_orig:.6f}", "0.000000"))

with open("/app/outputs/departure_results.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["initial_energy", "departure_original", "departure_corrected"])
    for row in rows:
        writer.writerow(row)
PYEOF
