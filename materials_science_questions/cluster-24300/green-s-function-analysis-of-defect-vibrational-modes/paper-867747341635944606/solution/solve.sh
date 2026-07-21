#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dos_tau.csv ===
python3 << 'PYEOF'
import csv, math

def n_tau(E):
    A = 0.1  # per K per impurity
    if E < 0.2:
        return A * 0.9  # weak dip from tau-tau interactions
    else:
        return A

# 200 logarithmically-spaced energies from 0.01 K to 20 K
Es = [0.01 * (20.0/0.01)**(i/199.0) for i in range(200)]

with open('/app/outputs/dos_tau.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy_K', 'density'])
    for E in Es:
        writer.writerow([E, n_tau(E)])
PYEOF

# === solve block: dos_s.csv ===
python3 << 'PYEOF'
import csv, math

def n_S(E):
    A = 0.002  # 1/J_o per K per impurity
    if E > 10.0:
        return A
    else:
        return A * (E/10.0)**3.25

# 200 logarithmically-spaced energies from 0.01 K to 20 K
Es = [0.01 * (20.0/0.01)**(i/199.0) for i in range(200)]

with open('/app/outputs/dos_s.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy_K', 'density'])
    for E in Es:
        writer.writerow([E, n_S(E)])
PYEOF

# === solve block: universality_params.json ===
python3 << 'PYEOF'
import json

params = {
    "C_o": 0.002,
    "T_U_K": 3.0,
    "J_o_K": 500.0,
    "g": 0.02
}

with open('/app/outputs/universality_params.json', 'w') as f:
    json.dump(params, f)
PYEOF
