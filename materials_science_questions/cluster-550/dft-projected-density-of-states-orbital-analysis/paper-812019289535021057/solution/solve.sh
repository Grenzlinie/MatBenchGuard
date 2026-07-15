#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_table.csv ===
python3 <<'PYEOF'
import csv
rows = [
    {"config": "Best-1", "a": 2.87, "V0": 1281.82, "E0": -827.44, "EF": 6.76, "mu_Mag": 160.53, "Phi": 3.421},
    {"config": "Best-2", "a": 2.86, "V0": 1263.26, "E0": -827.25, "EF": 6.80, "mu_Mag": 156.19, "Phi": 3.429},
    {"config": "Best-3", "a": 2.88, "V0": 1284.91, "E0": -825.28, "EF": 6.73, "mu_Mag": 159.04, "Phi": 3.420},
    {"config": "Best-4", "a": 2.81, "V0": 1200.69, "E0": -816.69, "EF": 7.43, "mu_Mag": 74.67, "Phi": 3.458},
    {"config": "Best-5", "a": 2.86, "V0": 1256.86, "E0": -815.71, "EF": 7.83, "mu_Mag": 88.32, "Phi": 3.432},
]
with open("/app/outputs/step_01_table.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["config","a","V0","E0","EF","mu_Mag","Phi"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
