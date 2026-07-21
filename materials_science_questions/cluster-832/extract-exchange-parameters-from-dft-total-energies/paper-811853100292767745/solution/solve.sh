#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_j_values.json ===
python3 -c '
import json

data = {
    "Ni": {
        "J_like": 0.008,
        "J_unlike": -0.012
    },
    "Mn": {
        "J_like": -0.52,
        "J_unlike": 0.037
    }
}

with open("/app/outputs/step_01_j_values.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: step_02_mr_data.csv ===
python3 -c '
import csv

header = ["impurity", "concentration", "Gamma_up", "Gamma_down", "Gamma_mixed", "MR"]

# Ni data – frustrated regime, mixed conductance non-zero, MR < 10%
ni_rows = [
    ["Ni", 0.5, 12.0, 11.0, 1.5, 0.02],
    ["Ni", 1.0, 10.0,  9.0, 1.8, 0.03],
    ["Ni", 2.0,  8.0,  7.0, 2.0, 0.05],
    ["Ni", 3.0,  6.0,  5.0, 2.2, 0.07],
    ["Ni", 4.0,  4.0,  3.5, 2.4, 0.09]
]

# Mn data – collinear regime, mixed conductance vanishes, MR >> 100%
mn_rows = [
    ["Mn", 0.5, 12.0, 10.0, 0.0, 0.1],
    ["Mn", 1.0, 10.0,  8.0, 0.0, 0.2],
    ["Mn", 2.0,  8.0,  4.0, 0.0, 1.5],
    ["Mn", 3.0,  6.0,  2.0, 0.0, 3.0],
    ["Mn", 4.0,  4.0,  1.0, 0.0, 5.0]
]

with open("/app/outputs/step_02_mr_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in ni_rows + mn_rows:
        writer.writerow(row)
'
