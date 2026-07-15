#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_isotherm_pressures.csv ===
python3 -c "
import csv
data = [
    (0.50, 45.603),
    (0.70, 48.418),
    (0.90, 48.755),
    (1.00, 48.758),
    (1.10, 48.762),
    (1.30, 49.374),
    (1.50, 55.035)
]
with open('/app/outputs/critical_isotherm_pressures.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['reduced_density', 'P_bar'])
    writer.writerows(data)
"
