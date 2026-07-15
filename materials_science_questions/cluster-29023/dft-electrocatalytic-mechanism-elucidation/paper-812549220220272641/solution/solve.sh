#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.csv ===
python3 -c "
import csv
rows = [
    ('PY_DHBD_COF', 1, -8.96),
    ('PY_DHBD_COF', 2, -7.00),
    ('PY_DHBD_COF', 3, -6.00),
    ('PY_BPY_COF', 1, -6.72),
    ('PY_BPY_COF', 2, -5.50),
    ('PY_BPY_COF', 3, -4.50),
    ('PY_BP_COF', 1, -5.83),
    ('PY_BP_COF', 2, -4.50),
    ('PY_BP_COF', 3, -3.50),
]
with open('/app/outputs/adsorption_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Fragment','Site','DeltaE_ads_kcal_mol'])
    writer.writerows(rows)
"

# === solve block: hole_electron_metrics.csv ===
python3 -c "
import csv
rows = [
    ('PY_DHBD_COF', 'S1', 0.53, 1.27),
    ('PY_BPY_COF', 'S1', 0.27, 0.0),
    ('PY_BP_COF', 'S1', 0.53, 0.55),
]
with open('/app/outputs/hole_electron_metrics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Fragment','State','S','D'])
    writer.writerows(rows)
"
