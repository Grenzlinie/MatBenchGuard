#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: carbon_fine_scan.csv ===
python3 <<'PYEOF'
import csv

data = [
    [0.36, 0.52, 1.273, 0.80, 0.40],
    [0.37, 0.51, 1.274, 0.60, 0.30],
    [0.38, 0.50, 1.275, 0.40, 0.20],
    [0.39, 0.48, 1.276, 0.20, 0.10],
    [0.40, 0.458, 1.278, 0.05, 0.02],
    [0.41, 0.44, 1.279, -0.10, -0.02],
    [0.42, 0.42, 1.278, -0.30, -0.05],
    [0.43, 0.38, 1.276, -0.50, -0.15],
    [0.44, 0.33, 1.274, -0.70, -0.25],
    [0.45, 0.28, 1.272, -0.90, -0.40],
]

with open("/app/outputs/carbon_fine_scan.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["pore_diameter", "charge_transfer", "oo_bond_length", "adsorption_energy", "gibbs_free_energy"])
    writer.writerows(data)
PYEOF

# === solve block: material_comparison_D0.4.csv ===
python3 <<'PYEOF'
import csv

data = [
    ["MgO", 0.4, 0.684],
    ["C3N4", 0.4, 0.354],
    ["carbon", 0.4, 0.458],
]

with open("/app/outputs/material_comparison_D0.4.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["material", "pore_diameter", "charge_transfer"])
    writer.writerows(data)
PYEOF
