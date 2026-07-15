#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: corrected_cell_parameter.csv ===
cat > /tmp/gen_csv.py << 'PYEOF'
import math, csv

# constants
delta_meV = 3.5
kB_meV_K = 8.617333262e-2  # meV/K
a_RT = 4.0682  # Angstrom
alpha = 1.4e-5  # K^-1
T_room = 298.0
a0 = a_RT / (1.0 + alpha * T_room)  # zero-K lattice parameter
N_e = 10  # number of valence electrons in the discrete levels
g = 2  # spin degeneracy
levels = [i*delta_meV for i in range(10)]  # 10 equally spaced levels (n=0..9)

def f(E, mu, kBT):
    if kBT <= 0:
        return 1.0 if E < mu else 0.0
    return 1.0 / (1.0 + math.exp((E - mu) / kBT))

def total_electrons(mu, kBT):
    return sum(g * f(E, mu, kBT) for E in levels)

def find_mu(T):
    kBT = kB_meV_K * T
    if T < 1e-3:
        return 4.5 * delta_meV  # T≈0: place 10 e in first 5 levels
    lo = -10.0
    hi = 10.0 * delta_meV + 10.0
    for _ in range(100):
        mid = (lo + hi) * 0.5
        ne = total_electrons(mid, kBT)
        if ne < N_e:
            lo = mid
        else:
            hi = mid
    return (lo + hi) * 0.5

def compute_dU_v_dR(T):
    kBT = kB_meV_K * T
    if T < 1e-3:
        return 0.0  # dU_v/dR = 0 at T=0 (Fig.1)
    mu = find_mu(T)
    sum_S = 0.0
    for E in levels:
        f_val = f(E, mu, kBT)
        term = E * f_val - (E**2 * f_val * (1.0 - f_val)) / kBT
        sum_S += g * term
    dU = (3.0 * N_e / a0) * sum_S  # meV/Angstrom
    return dU

temps = [i*5.0 for i in range(int(390/5)+1)]  # 79 points

# precompute dU_v/dR
dU_dict = {}
for T in temps:
    dU_dict[T] = compute_dU_v_dR(T)

# derivative of -dU_v/dR at 125 K via 124/126 K
dU_124 = compute_dU_v_dR(124.0)
dU_126 = compute_dU_v_dR(126.0)
neg_dU_124 = -dU_124
neg_dU_126 = -dU_126
d_neg_dT = (neg_dU_126 - neg_dU_124) / 2.0  # meV/Angstrom/K

# C such that a*(T) = a0(1+alpha*T) + C * neg_dU has da*/dT = 0 at 125 K
C = - a0 * alpha / d_neg_dT  # Angstrom^2/meV

out_path = "/app/outputs/corrected_cell_parameter.csv"
with open(out_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["temperature_K", "a_star_Angstrom", "1_over_a_star_Angstrom-1"])
    for T in temps:
        dU = dU_dict[T]
        neg_dU = -dU
        delta_a = C * neg_dU
        a_star = a0 * (1.0 + alpha * T) + delta_a
        inv_a = 1.0 / a_star
        writer.writerow([T, a_star, inv_a])
PYEOF
python3 /tmp/gen_csv.py
