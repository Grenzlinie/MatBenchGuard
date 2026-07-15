#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: p2_dissociation_equilibrium.json ===
python3 << 'PYEOF'
import json
data = {
    "units": "K_atmos dimensionless, lnK dimensionless",
    "entries": [
        {"T_K": 1073, "K_atmos": 7.4e-21, "lnK": -46.35},
        {"T_K": 1173, "K_atmos": 9.1e-19, "lnK": -41.54},
        {"T_K": 1273, "K_atmos": 5.4e-17, "lnK": -37.47},
        {"T_K": 1373, "K_atmos": 1.7e-15, "lnK": -33.99},
        {"T_K": 1473, "K_atmos": 3.6e-14, "lnK": -30.96}
    ]
}
with open("/app/outputs/p2_dissociation_equilibrium.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
