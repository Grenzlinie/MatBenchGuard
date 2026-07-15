#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_youngs_modulus.csv ===
python3 << 'PYEOF'
import csv
import math

# Force constants (N/m^3) and lattice parameter (m)
kbSi0 = 6.187e20
kthetaSi0 = 1.813e20
kbP0 = 7.897e20
kthetaP0 = 1.561e20
a0 = 1.3575e-10   # 1.3575 Å in metres

# Temperature‑dependent lattice parameter a(T) = a0 * (1 + 2.6e-6 * T)
def a_temp(T):
    return a0 * (1.0 + 2.6e-6 * T)

N_values = [1,2,3,4,5,6,7,8,9,10,20,50,100]
alpha_values = [0.0, 0.01, 0.1, 1.0]
T_values = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

with open('/app/outputs/step_01_youngs_modulus.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['N','alpha','T','E'])  # E in GPa
    for N in N_values:
        Nf = float(N)
        geom = 8.0 * Nf**2 / (4.0*Nf + 1.0)**2
        for alpha in alpha_values:
            for T in T_values:
                aT = a_temp(T)
                # scaling factors
                ratio = a0 / aT
                s4 = ratio ** 4
                s7 = ratio ** 7
                # temperature‑dependent summed constants
                sumSi = 2.0 * kbSi0 * s4 + 3.0 * kthetaSi0 * s7
                sumP  = 2.0 * kbP0  * s4 + 3.0 * kthetaP0  * s7
                # Young's modulus in Pa via Eq. 2
                E_Pa = geom * aT * sumSi + 8.0 * alpha * (aT**4) * (sumP - sumSi)
                E_GPa = E_Pa * 1e-9
                w.writerow([N, alpha, T, round(E_GPa, 6)])
PYEOF
