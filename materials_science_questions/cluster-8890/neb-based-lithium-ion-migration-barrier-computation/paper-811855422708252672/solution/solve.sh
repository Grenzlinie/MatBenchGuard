#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_profiles.csv ===
python3 << 'PYEOF'
import csv

header = ['model', 'x', 'total_energy']
rows = []

models = {
    'A': {'xmin': 0.25, 'barrier': 0.3},
    'B': {'xmin': 0.15, 'barrier': 0.5},
    'C': {'xmin': 0.0,  'barrier': 0.7},
}

for model_name, params in models.items():
    xmin = params['xmin']
    barrier = params['barrier']
    # sample x from 0.0 to 0.5 in steps of 0.01
    for i in range(0, 51):
        x = i / 100.0  # 0.00, 0.01, ..., 0.50
        # E(x) = barrier * ((x - xmin)^2 / (0.5 - xmin)^2)
        if xmin == 0.5:
            E = 0.0  # not used
        else:
            E = barrier * ((x - xmin) ** 2) / ((0.5 - xmin) ** 2)
        rows.append([model_name, f'{x:.2f}', f'{E:.6f}'])

with open('/app/outputs/energy_profiles.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
PYEOF
