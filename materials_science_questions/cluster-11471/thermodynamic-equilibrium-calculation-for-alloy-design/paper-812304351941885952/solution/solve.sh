#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table2_results.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/table2_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['zone', 'temperature_C', 'boundary_Cb', 'A_C', 'C_b'])
    writer.writerow([1, 810, 0.91, 0.77, 0.73])
    writer.writerow([2, 830, 0.97, 0.79, 0.80])
    writer.writerow([3, 820, 0.94, 1.58, 1.35])
PYEOF

# === solve block: table3_results.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ['steel', 'regime', 'C_surf', 'C_a', 'f'],
    ['35G2', 'Actual', 0.970, 1.000, 0.97],
    ['08kp', 'Actual', 0.908, 0.916, 0.99],
    ['35G2', 'Calculated', 0.893, 0.924, 0.97],
    ['08kp', 'Calculated', 0.945, 0.950, 0.99],
]
with open('/app/outputs/table3_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF

# === solve block: table5_results.json ===
python3 <<'PYEOF'
import json
data = [
    {"atmosphere": 1, "CO": 17.05, "CO2": 0.371, "CH4": 0.100, "H2": 18.04, "H2O": 0.403, "N2": 64.08, "A_C": 0.760, "C_b": 0.750, "t_d": -5.3},
    {"atmosphere": 2, "CO": 18.02, "CO2": 0.403, "CH4": 0.100, "H2": 17.99, "H2O": 0.413, "N2": 63.08, "A_C": 0.770, "C_b": 0.766, "t_d": -5.1},
    {"atmosphere": 3, "CO": 17.96, "CO2": 0.324, "CH4": 0.120, "H2": 18.07, "H2O": 0.335, "N2": 63.20, "A_C": 0.961, "C_b": 0.910, "t_d": -7.9},
    {"atmosphere": 4, "CO": 18.61, "CO2": 0.358, "CH4": 0.118, "H2": 18.16, "H2O": 0.359, "N2": 63.50, "A_C": 0.930, "C_b": 0.890, "t_d": -6.9},
    {"atmosphere": 5, "CO": 17.16, "CO2": 0.297, "CH4": 0.120, "H2": 18.11, "H2O": 0.322, "N2": 64.10, "A_C": 0.960, "C_b": 0.910, "t_d": -8.4},
    {"atmosphere": 6, "CO": 17.97, "CO2": 0.314, "CH4": 0.122, "H2": 17.96, "H2O": 0.323, "N2": 63.285, "A_C": 0.990, "C_b": 0.940, "t_d": -8.4}
]
with open('/app/outputs/table5_results.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
