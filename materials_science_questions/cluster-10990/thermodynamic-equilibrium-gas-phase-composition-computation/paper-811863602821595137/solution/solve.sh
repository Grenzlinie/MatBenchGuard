#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_04_partial_pressures.csv ===
python3 << 'PYEOF'
import math
import csv

R = 8.314
T = 1400.0
RT = R * T
P0 = 100000.0   # 1 bar in Pa

conditions = [
    ("A", 1.01, 1.01e-3),
    ("B", 1010.0, 1.01e-3)
]

def calc_dG(A, B, C, D, E, T):
    return A + B*T + C*T*math.log(T) + D*T*T + E/T

def calc_partial(params, n_Bi, n_O2, P_Bi, P_O2):
    dG = calc_dG(*params, T)
    K = math.exp(-dG / RT)
    p_bi_atm = P_Bi / P0
    p_o2_atm = P_O2 / P0
    p_prod_atm = K * (p_bi_atm ** n_Bi) * (p_o2_atm ** n_O2)
    return p_prod_atm * P0

# pure bismuth species data: (name, n_Bi, n_O2, coefficients for formation reaction)
# formation dG_f = A + B*T (C=D=E=0)
pure_data = [
    ("Bi2", 2, 0, (-197360.0, -105.9, 0.0, 0.0, 0.0)),
    ("Bi3", 3, 0, (-319671.0, -231.1, 0.0, 0.0, 0.0)),
    ("Bi4", 4, 0, (-583571.0, -348.1, 0.0, 0.0, 0.0)),
]

# oxide species data: (name, n_Bi, n_O2, (A, B, C, D, E))
oxide_data = [
    ("BiO", 1, 0.5, (-97000.0, -84.0, 2.6, -0.22, 5.85e6)),
    ("Bi2O_linear", 2, 0.5, (-706200.0, 2533.0, -310.0, 0.06, 7.4e7)),
    ("Bi2O_angular", 2, 0.5, (2.9e6, -24175.0, 3290.0, -1.1, -5.0e8)),
    ("Bi2O2", 2, 1.0, (2.64e6, 65230.0, 3190.0, -1.1, -4.8e8)),
    ("Bi2O3", 2, 1.5, (8.8e6, -70770.0, 9590.0, -3.16, -1.5e9)),
    ("Bi3O4", 3, 2.0, (4.5e6, -43560.0, 6010.0, -2.21, -8.24e8)),
    ("Bi4O6", 4, 3.0, (-1.24e6, -4860.0, 818.0, -0.46, -27350.0)),
]

rows = []
for cond, P_Bi, P_O2 in conditions:
    # Bi monomer
    rows.append(("Bi", T, P_Bi, P_O2, P_Bi))
    # pure species
    for name, n_Bi, n_O2, coeff in pure_data:
        p = calc_partial(coeff, n_Bi, n_O2, P_Bi, P_O2)
        rows.append((name, T, P_Bi, P_O2, p))
    # oxide species
    for name, n_Bi, n_O2, coeff in oxide_data:
        p = calc_partial(coeff, n_Bi, n_O2, P_Bi, P_O2)
        rows.append((name, T, P_Bi, P_O2, p))

with open('/app/outputs/step_04_partial_pressures.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["species", "T", "P_Bi_set", "P_O2_set", "P_partial"])
    w.writerows(rows)
PYEOF
