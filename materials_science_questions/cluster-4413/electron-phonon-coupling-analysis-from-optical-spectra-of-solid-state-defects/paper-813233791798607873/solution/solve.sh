#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: evi_parameters.csv ===
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import csv

k_B = 0.69503476  # cm⁻¹/K
T = 300.0

compounds = [
    ("LiMgBF6", 7296.0, 5636.0),
    ("Li2NaBF6", 9063.0, 6300.0),
    ("Li3BF6", 11906.0, 5853.0),
]

def equations(vars, deltaE, gammaT):
    S, hw = vars
    eq1 = (2*S - 1)*hw - deltaE
    eq2 = np.sqrt(8*np.log(2)) * hw * np.sqrt(S / np.tanh(hw/(2*k_B*T))) - gammaT
    return [eq1, eq2]

results = []
for name, deltaE, gammaT in compounds:
    initial_guess = np.array([3.0, 1300.0])
    sol = fsolve(equations, initial_guess, args=(deltaE, gammaT), maxfev=1000)
    S_val, hw_val = sol
    # Ensure physically sensible; retry if needed
    if S_val <= 0 or hw_val <= 0:
        initial_guess = np.array([5.0, 1000.0])
        sol = fsolve(equations, initial_guess, args=(deltaE, gammaT), maxfev=1000)
        S_val, hw_val = sol
    if S_val < 1:
        regime = "weak"
    elif 1 <= S_val <= 5:
        regime = "intermediate"
    else:
        regime = "strong"
    results.append((name, S_val, hw_val, regime))

with open("/app/outputs/evi_parameters.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["compound", "S", "hbar_omega", "regime"])
    for name, S_val, hw_val, regime in results:
        writer.writerow([name, S_val, hw_val, regime])
PYEOF
