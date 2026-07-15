#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR='/app/outputs'
mkdir -p "$OUTDIR"

# === solve block: specific_interfacial_energy.csv ===
python3 << 'PYEOF'
import math, csv, os

nu = 0.29
alpha = 2.21e-5
T_ref = 298.15
T_700 = 973.15

alloys = [
    ("25Cr-20Ni-Nb-N", 3.59798, 10.65841),
    ("22Cr-25Ni-Mo-Nb-N", 3.59450, 10.68570),
]

def E(T):
    return 254680 - 114.76 * T

def expand(a, T):
    return a * (1 + alpha * (T - T_ref))

def compute_sigma(a_gamma_rt, a_m23c6_rt, T):
    a_gamma = expand(a_gamma_rt, T)
    a_m23c6 = expand(a_m23c6_rt, T)
    E_mod = E(T)
    delta = abs(a_m23c6 - 3*a_gamma) / a_m23c6
    if delta == 0:
        return 0.0
    two_delta = 2*delta
    term1 = 2.0 / (1 + 1.0/(4*delta**2))
    term2 = math.log(two_delta)
    f = delta * (term1 - term2)
    denom = 4 * math.sqrt(2) * (1 - nu**2)
    sigma_MPa_A = (E_mod * a_gamma) / denom * f
    sigma_Jm2 = sigma_MPa_A * 1e-4
    return sigma_Jm2

rows = []
for name, ag, am in alloys:
    rows.append((name, 25, compute_sigma(ag, am, T_ref)))
    rows.append((name, 700, compute_sigma(ag, am, T_700)))

path = os.path.join(os.environ["OUTDIR"], "specific_interfacial_energy.csv")
with open(path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["alloy", "temperature_C", "sigma"])
    for row in rows:
        writer.writerow([row[0], row[1], f"{row[2]:.6f}"])
PYEOF
