#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_params.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ["Nb6Ti", 76.9, 1073, 13.9, 288.6, 277.8, 0.83],
    ["Nb6Zr", 58.8, 615, 10.4, 659.7, 258.2, 0.92],
    ["Nb6Hf", 75.6, 975, 12.9, 325.6, 239.5, 0.89]
]
with open("/app/outputs/computed_params.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["alloy","xi_GL_A","lambda_GL_A","k_GL","H_c_mT","theta_D_K","lambda_e_ph"])
    w.writerows(rows)
PYEOF
