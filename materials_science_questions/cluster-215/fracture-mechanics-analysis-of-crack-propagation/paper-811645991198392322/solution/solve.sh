#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_predictions.csv ===
mkdir -p /app/outputs
python3 << 'PYEOF'
import math, csv
gammas = [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
with open('/app/outputs/step_01_predictions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['gamma', 'bending_predicted_ratio', 'torsion_predicted_ratio'])
    for g in gammas:
        if g > 0.65:
            br = 1.0
        else:
            br = (9*math.pi/32) * (1 - g**4) / (1 - g**3)
        writer.writerow([g, br, 1.0])
PYEOF
