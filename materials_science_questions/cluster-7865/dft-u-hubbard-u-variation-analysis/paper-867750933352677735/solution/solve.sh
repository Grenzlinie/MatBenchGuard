#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: step_01_model_LS.csv ===
python3 <<'PYEOF'
import csv

points = [
    (0.0, 1.0, 0.5),
    (0.5, 1.05, 0.55),
    (1.0, 1.1, 0.6),
    (1.5, 1.15, 0.65),
    (2.0, 1.2, 0.7),
    (2.5, 1.25, 0.75),
    (3.0, 1.3, 0.8),
    (3.5, 1.35, 0.85),
    (4.0, 1.4, 0.9),
    (4.5, 1.45, 0.95),
    (5.0, 1.5, 1.0),
]

with open('/app/outputs/step_01_model_LS.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['10Dq', 'LS_J', 'LS_jeff'])
    for row in points:
        w.writerow(list(row))
PYEOF

# === solve block: step_02_material_results.json ===
python3 <<'PYEOF'
import json

data = {
    "Sr2IrO4_x=0": {
        "LS": -1.8,
        "n_h": 4.254
    },
    "Sr2MgIrO6": {
        "LS": -1.35,
        "n_h": 5.03
    }
}

for key in data:
    r = data[key]["LS"] / data[key]["n_h"]
    data[key]["branching_ratio"] = round((2 - r) / (1 + r), 6)

with open('/app/outputs/step_02_material_results.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
