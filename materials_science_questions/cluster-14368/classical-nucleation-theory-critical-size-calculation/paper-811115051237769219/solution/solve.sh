#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: growth_rates.csv ===
python3 << 'PYEOF'
import csv
data = [(6, 1e-7), (8, 3e-7), (10, 1e-6), (15, 8e-6), (20, 1.5e-5), (40, 2.8e-5), (160, 4e-5)]
with open('/app/outputs/growth_rates.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['width', 'growth_rate'])
    for w, r in data:
        writer.writerow([w, f'{r:.2e}'])
PYEOF

# === solve block: critical_supersaturation.csv ===
python3 << 'PYEOF'
import csv
data = [(8, 0.45), (15, 0.24)]
with open('/app/outputs/critical_supersaturation.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['width', 'critical_supersaturation'])
    for w, s in data:
        writer.writerow([w, f'{s:.2f}'])
PYEOF

# === solve finalize ===
echo 'Oracle solve completed.'
