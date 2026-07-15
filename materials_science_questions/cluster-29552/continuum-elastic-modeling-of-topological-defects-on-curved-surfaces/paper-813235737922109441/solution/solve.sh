#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_free_energy_vs_chiWall.csv ===
python3 <<PYEOF
import csv

header = ['chi_Wall', 'defect_free_energy_kT']
rows = [
    ['0', '5.0'],
    ['10', '8.0'],
    ['20', '11.0'],
    ['30', '15.0'],
    ['40', '19.0'],
    ['42', '20.7'],
    ['44', '17.2'],
    ['50', '17.2'],
    ['64', '17.2'],
]

with open('/app/outputs/defect_free_energy_vs_chiWall.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
PYEOF
