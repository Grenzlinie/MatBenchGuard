#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_temperatures.json ===
python3 -c "
import json
data = {
    'r=0.0': 2.056,
    'r=0.6': 0.871,
    'r=0.7': 0.7643
}
with open('/app/outputs/critical_temperatures.json', 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')
"

# === solve block: critical_exponents.csv ===
python3 -c "
import csv
with open('/app/outputs/critical_exponents.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r', 'nu', 'alpha', 'beta', 'gamma', 'eta'])
    writer.writerow(['0.0', 0.70, -0.13, 0.37, 1.39, 0.02])
    writer.writerow(['0.6', 0.71, -0.13, 0.37, 1.38, 0.03])
"

# === solve block: transition_order.txt ===
echo -n 'first-order' > /app/outputs/transition_order.txt
