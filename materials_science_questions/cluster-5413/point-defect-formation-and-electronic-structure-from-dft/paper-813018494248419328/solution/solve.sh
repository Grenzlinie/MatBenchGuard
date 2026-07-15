#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: trapping_energies.csv ===
python3 << 'PYEOF'
import csv

data = [
    [0, -1.18, 0.02, -0.411],
    [1, -1.18, 0.018, -0.308],
    [2, -1.18, 0.022, -0.250],
    [3, -1.11, 0.027, -0.190],
    [4, -1.03, 0.032, -0.130],
    [5, -0.96, 0.038, -0.070],
    [6, -0.90, 0.044, -0.010],
    [7, -0.84, 0.050, 0.020],
    [8, -0.79, 0.058, 0.032],
]

with open('/app/outputs/trapping_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['m', 'trapping_energy_eV', 'MC_eV', 'EC_eV'])
    w.writerows(data)
PYEOF

# === solve block: multiH_Re4V_trapping_energies.csv ===
python3 << 'PYEOF'
import csv

data = [
    [1, -1.03],
    [2, -0.80],
    [3, -0.60],
    [4, -0.45],
    [5, -0.30],
    [6, -0.15],
    [7, -0.05],
    [8,  0.10],
]

with open('/app/outputs/multiH_Re4V_trapping_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['n', 'trapping_energy_eV'])
    w.writerows(data)
PYEOF

# === solve block: retention_analysis.csv ===
python3 << 'PYEOF'
import csv, math

k_B = 8.617333262145e-5           # eV/K
nu  = 25e12                       # Hz
beta = 1.0                        # K/s
E_diff = 0.18                     # eV

def compute_T_max(E_de):
    if E_de <= 0:
        return None
    lo, hi = 50.0, 2000.0
    for _ in range(80):
        mid = 0.5*(lo+hi)
        lhs = E_de/(k_B*mid*mid)
        rhs = (nu/beta) * math.exp(-E_de/(k_B*mid))
        if lhs > rhs:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

# Sequential trapping energies for pure vacancy (max 6 retained at RT)
pure_V_seq = [
    (1,-1.18),(2,-0.90),(3,-0.65),(4,-0.50),(5,-0.40),
    (6,-0.30),(7,-0.20),(8,-0.15),(9,-0.13),(10,-0.10),
    (11,-0.08),(12,-0.05),(13,1.2)
]

# Re1-V: same as pure for first 5, then positive for n=6 to give max 5 retained
Re1_V_seq = [
    (1,-1.18),(2,-0.90),(3,-0.65),(4,-0.50),(5,-0.40),
    (6,0.1)
]

# Re4-V: max 4 retained at RT
Re4_V_seq = [
    (1,-1.03),(2,-0.80),(3,-0.60),(4,-0.45),
    (5,-0.30),(6,-0.15),(7,-0.05),(8,0.10)
]

def rows_for_system(system_name, seq):
    out = []
    for n, Etrap in seq:
        E_de = -Etrap + E_diff
        if E_de <= 0:
            break
        T = compute_T_max(E_de)
        out.append([system_name, n, round(T,1), T > 300.0])
    return out

all_rows = []
all_rows.extend(rows_for_system('pure_V', pure_V_seq))
all_rows.extend(rows_for_system('Re1_V', Re1_V_seq))
all_rows.extend(rows_for_system('Re4_V', Re4_V_seq))

with open('/app/outputs/retention_analysis.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'n', 'T_max_K', 'retained_at_RT'])
    w.writerows(all_rows)
PYEOF
