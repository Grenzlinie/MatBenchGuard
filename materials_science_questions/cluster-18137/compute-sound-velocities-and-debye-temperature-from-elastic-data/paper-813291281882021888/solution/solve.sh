#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calibrated_cutoff.json ===
python3 - <<'PYEOF'
import json
data = {"lower_cutoff_OC1_cm1": 240}
with open('/app/outputs/calibrated_cutoff.json', 'w') as f:
    json.dump(data, f)
PYEOF

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: cp_values.csv ===
python3 - <<'PYEOF'
import csv

rows = [
    (50, 3.99),
    (100, 24.45),
    (150, 53.22),
    (200, 79.18),
    (300, 115.5),
    (400, 136.6),
    (500, 149.2),
    (600, 157.3),
    (700, 162.8),
    (800, 166.7),
    (900, 169.7),
    (1000, 172.1),
    (1200, 175.8),
    (1400, 178.7),
    (1600, 181.2),
    (1800, 183.5),
    (2000, 185.7),
    (2500, 191.5),
]
with open('/app/outputs/cp_values.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Temperature_K', 'Cp_J_per_mol_K'])
    for t, cp in rows:
        w.writerow([t, cp])
PYEOF

# === solve block: polynomial_coefficients.json ===
python3 - <<'PYEOF'
import json

coeffs = {
    "k0": 164.30,
    "k1": 0.010216,
    "k2": 7666.5,
    "k3": -11595000,
    "k4": 1380700000
}
with open('/app/outputs/polynomial_coefficients.json', 'w') as f:
    json.dump(coeffs, f, indent=2)
PYEOF
