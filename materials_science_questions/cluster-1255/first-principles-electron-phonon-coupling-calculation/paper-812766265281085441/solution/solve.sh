#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: N_EF_vs_doping.csv ===
python3 -c "
import csv
rows = [
    ('LiBeH', 0.0, 0.0),
    ('LiBeH', 0.05, 0.236),
    ('NaMgH', 0.0, 0.0),
    ('NaMgH', 0.05, 0.27),
    ('NaMgH', 0.10, 0.54),
    ('NaMgH', 0.20, 0.84),
    ('KCaH', 0.0, 0.0),
    ('KCaH', 0.05, 0.15),
    ('KCaH', 0.25, 0.50),
    ('KCaH', 0.45, 0.845),
]
with open('/app/outputs/N_EF_vs_doping.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'doping_x', 'N_EF'])
    w.writerows(rows)
"

# === solve block: lambda_Tc_results.json ===
python3 -c "
import json
data = {
    'LiBeH': {'lambda': 0.473, 'Tc': 2.1},
    'NaMgH': {'lambda': 1.26, 'Tc': 28.0},
    'KCaH': {'lambda': 1.69, 'Tc': 49.0},
}
with open('/app/outputs/lambda_Tc_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
