#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: activation_energies.csv ===
python3 << 'PYEOF'
import csv
rows = [
    ('1', 15.8),
    ('2', 20.7),
    ('3', 20.9),
    ('4', 22.3),
    ('5', 22.7),
    ('6', 26.8),
    ('7', 33.3),
    ('8', 33.4),
    ('tetrakis', 33.5),
]
with open('/app/outputs/activation_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Ea_kcal_mol', 'ethylene_id'])
    for eid, ea in rows:
        writer.writerow([ea, eid])
PYEOF
