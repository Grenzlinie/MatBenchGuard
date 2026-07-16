#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import math, json

nu = 1.0 / 3
D_over_b = 500
M = 2
lam = 3.0 / 2

Q = (2 * math.pi * (1 - nu**2) * D_over_b) / (3 * M * lam)
ln_Q = math.log(Q)
X_c_rad = ln_Q / Q
Phi_min_rad = 1.0 / Q
X_c_deg = math.degrees(X_c_rad)
Phi_min_deg = math.degrees(Phi_min_rad)
ratio_X_Phi = ln_Q

data = {
    "Q": Q,
    "X_c_rad": X_c_rad,
    "Phi_min_rad": Phi_min_rad,
    "X_c_deg": X_c_deg,
    "Phi_min_deg": Phi_min_deg,
    "ratio_X_Phi": ratio_X_Phi
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
