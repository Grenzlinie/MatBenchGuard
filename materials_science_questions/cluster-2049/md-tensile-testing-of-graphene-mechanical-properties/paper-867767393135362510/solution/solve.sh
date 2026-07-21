#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: stress_strain.csv ===
python3 <<'PYEOF'
import csv

ribbons = [
    ('AGNR', 720, 83, 0.16),
    ('CGNR', 714, 85, 0.175),
    ('ZGNR', 710, 98, 0.24),
]
step = 0.0005

with open('/app/outputs/stress_strain.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ribbon_type', 'strain', 'stress'])
    for name, E, sig_y, eps_b in ribbons:
        yield_strain = sig_y / E
        strain = 0.0
        while strain <= eps_b + step:
            if strain <= yield_strain:
                stress = E * strain
            elif strain < eps_b:
                stress = sig_y
            else:
                stress = 0.0
            writer.writerow([name, f'{strain:.4f}', f'{stress:.6f}'])
            strain = round(strain + step, 10)
PYEOF
