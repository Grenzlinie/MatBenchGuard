#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: segregation_enthalpies.csv ===
python3 <<'PYEOF'
import csv

data = [
    {"dopant": "Fe", "site_type": 1, "dH": -0.08},
    {"dopant": "Fe", "site_type": 2, "dH":  0.10},
    {"dopant": "Fe", "site_type": 3, "dH":  0.10},
    {"dopant": "Yb", "site_type": 1, "dH": -0.70},
    {"dopant": "Yb", "site_type": 2, "dH": -0.10},
    {"dopant": "Yb", "site_type": 3, "dH":  0.50},
    {"dopant": "Eu", "site_type": 1, "dH": -1.07},
    {"dopant": "Eu", "site_type": 2, "dH": -0.40},
    {"dopant": "Eu", "site_type": 3, "dH":  0.70},
    {"dopant": "La", "site_type": 1, "dH": -1.56},
    {"dopant": "La", "site_type": 2, "dH": -0.70},
    {"dopant": "La", "site_type": 3, "dH":  0.90},
]

with open("/app/outputs/segregation_enthalpies.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["dopant", "site_type", "dH"])
    writer.writeheader()
    writer.writerows(data)
PYEOF
