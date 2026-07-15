#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: scattering_rates.csv ===
python3 <<'PYEOF'
import csv
import math
import os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
mechanisms = [
    'POP_1to1_abs', 'POP_1to1_emi', 'POP_1to2_abs', 'POP_1to2_emi',
    'AP_1to1_abs', 'AP_1to1_emi', 'II_1to1', 'II_2to2'
]
positions = [0.0, 0.3, 0.6]  # V
energies = [round(i*0.01, 2) for i in range(0, 51)]  # 0.0 to 0.5
hbar_omega = 0.0354  # eV (POP phonon energy)
# Position-dependent amplitude factors (source > drain)
pos_factor = {0.0: 0.7, 0.3: 0.85, 0.6: 1.0}

def pop_rate_abs(E, E_th, base=1e13):
    # threshold at E_th + hbar_omega (absorption)
    if E <= E_th + hbar_omega:
        return 0.0
    return base * (E - E_th - hbar_omega)

def pop_rate_emi(E, E_th, base=1e13):
    # emission: threshold at E_th
    if E <= E_th:
        return 0.0
    return base * (E - E_th)

def ap_rate(E, base=1e11):
    # linear increase
    return base * E

def ii_rate(E, base=1e10):
    # roughly constant offset
    return base * (1.0 + 5.0*E)

# subband energy threshold estimates (eV)
# for 1->1 intra: E_th = 0.0
# for 1->2 inter: assume ~0.03 eV difference
E_th_1 = 0.0
E_th_2 = 0.03

rows = []
for mech in mechanisms:
    for pos in positions:
        f = pos_factor[pos]
        for E in energies:
            if mech == 'POP_1to1_abs':
                rate = f * pop_rate_abs(E, E_th_1, base=1e13)
            elif mech == 'POP_1to1_emi':
                rate = f * pop_rate_emi(E, E_th_1, base=1e13)
            elif mech == 'POP_1to2_abs':
                rate = f * pop_rate_abs(E, E_th_2, base=8e12)
            elif mech == 'POP_1to2_emi':
                rate = f * pop_rate_emi(E, E_th_2, base=8e12)
            elif mech == 'AP_1to1_abs':
                rate = f * ap_rate(E, base=1e11)
            elif mech == 'AP_1to1_emi':
                rate = f * ap_rate(E, base=1e11)
            elif mech == 'II_1to1':
                rate = f * ii_rate(E, base=1e10)
            elif mech == 'II_2to2':
                rate = f * ii_rate(E, base=5e9)
            else:
                rate = 0.0
            rows.append([mech, pos, E, rate])

path = os.path.join(OUTDIR, 'scattering_rates.csv')
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['mechanism', 'position_V', 'energy_eV', 'rate_s_1'])
    writer.writerows(rows)
print(f"Wrote {len(rows)} rows to {path}")
PYEOF
