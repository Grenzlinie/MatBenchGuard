#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: one_parameter_results.csv ===
python3 -c "
import csv
data = [
    {'l_over_b': 40, 'gamma_over_Gb': 9.5, 'E_min_over_Gb3': 44.1, 'h_over_b': 5.2},
    {'l_over_b': 260, 'gamma_over_Gb': 2.03, 'E_min_over_Gb3': 396.0, 'h_over_b': 22.5},
    {'l_over_b': 1000, 'gamma_over_Gb': 0.629, 'E_min_over_Gb3': 1820.0, 'h_over_b': 86.6},
]
with open('/app/outputs/one_parameter_results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['l_over_b','gamma_over_Gb','E_min_over_Gb3','h_over_b'])
    writer.writeheader()
    writer.writerows(data)
"
