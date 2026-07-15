#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: exchange_couplings.csv ===
# Write the scored CSV directly from the paper's ΔE per ion values
python3 << 'PYEOF'
import csv

with open('/app/outputs/exchange_couplings.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['impurity','coupling_type','supercell','U_value_eV','delta_E_per_bond_meV','J_meV'])
    
    # (impurity, coupling_type, supercell, U, Delta_E_per_ion_meV)
    rows = [
        ('Co', 'in-plane',        'A', 0,  22),
        ('Co', 'out-of-plane',    'B', 0, -31),
        ('Co', 'in-plane',        'A', 6,  24),
        ('Co', 'out-of-plane',    'B', 6,  12),
        ('Mn', 'in-plane',        'A', 0, 147),
        ('Mn', 'out-of-plane',    'B', 0, 122),
        ('Mn', 'in-plane',        'A', 6,  59),
        ('Mn', 'out-of-plane',    'B', 6,  40),
    ]
    for imp, ctype, sc, U, dE in rows:
        dE_bond = dE / 2.0
        denom = 12.0 if imp == 'Co' else 30.0
        J = -2.0 * dE_bond / denom
        J = round(J, 1)
        if J == -0.0:
            J = 0.0
        w.writerow([imp, ctype, sc, U, round(dE_bond, 1), J])
PYEOF
