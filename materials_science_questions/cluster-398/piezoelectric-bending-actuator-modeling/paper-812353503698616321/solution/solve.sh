#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: model_predictions.csv ===
python3 <<'PYEOF'
import csv, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(outdir, exist_ok=True)
rows = [
    ["Device 1", "9.0", "933.75", "8.3", "0.2075", "328.27"],
    ["Device 2", "10.0", "264.0", "5.28", "0.132", "208.82"],
]
with open(os.path.join(outdir, "model_predictions.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["device_id","voltage_V","membrane_displacement_nm","period_change_nm","strain_percent","angular_change_urad"])
    w.writerows(rows)
PYEOF
