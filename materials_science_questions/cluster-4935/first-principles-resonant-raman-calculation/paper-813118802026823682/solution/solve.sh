#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ct_contribution.json ===
python3 << 'PYEOF'
import json
out = {
    "dx_dq": -2.5e-12,
    "drho_dx": 4e7,
    "dalpha_A_drhoA": 33e-25,
    "dalpha_D_drhoD": 5e-25,
    "CT_contribution": 2.8e-28
}
with open("/app/outputs/ct_contribution.json", "w") as f:
    json.dump(out, f, indent=2)
PYEOF
