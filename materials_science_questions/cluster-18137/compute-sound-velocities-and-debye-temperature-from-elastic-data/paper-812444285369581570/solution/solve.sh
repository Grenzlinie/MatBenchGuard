#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_parameters.csv ===
python3 <<'PYEOF'
import csv

rows = [
    ["material","I_t","I_l","I","Omega_t","Omega_l","Omega","Theta_t","Theta_l","Theta"],
    ["Te","14.66","7.816","12.38","1.896","2.339","2.007","144.8","178.7","153.3"],
    ["Sb","3.812","5.381","4.315","2.971","2.649","2.847","226.9","202.3","214.6"],
]

with open("/app/outputs/computed_parameters.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF

# === solve block: recoilless_fractions.csv ===
python3 <<'PYEOF'
import csv, math

k_B = 8.617333262e-5  # eV/K
# (material, R_eV, Theta_t_K, Theta_l_K, temps_K)
materials = [
    ("Te", 5.44e-3, 144.8, 178.7, [0, 80, 300]),
    ("Sb", 6.72e-3, 226.9, 202.3, [0, 90, 300]),
]

def integral(y, steps=100000):
    if y <= 0:
        return 0.0
    h = y / steps
    total = 0.0
    for i in range(steps):
        x = (i + 0.5) * h
        total += x / (math.exp(x) - 1.0)
    return total * h

def W_alpha(T, Theta, R):
    if T == 0.0:
        return math.exp(-3*R / (2*k_B*Theta))
    y = Theta / T
    term = 1.0 + 4.0 * (T/Theta)**2 * integral(y)
    exponent = (3*R) / (2*k_B*Theta) * term
    return math.exp(-exponent)

with open("/app/outputs/recoilless_fractions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["material","temperature","W_t","W_l","A"])
    for mat, R, Theta_t, Theta_l, temps in materials:
        for T in temps:
            wt = W_alpha(T, Theta_t, R)
            wl = W_alpha(T, Theta_l, R)
            A = wt / wl if wl != 0 else float('inf')
            writer.writerow([mat, T, wt, wl, A])
PYEOF
