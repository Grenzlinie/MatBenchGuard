#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 <<'PYEOF'
import json
import math

alpha_c = 0.25
# angle of b = Fe2 = alpha*e1 + e2
b_angle_deg = math.degrees(math.atan(alpha_c))

result = {
    "alpha_c_stability": alpha_c,
    "alpha_c_simulation": alpha_c,
    "stability_modes": [
        {
            "zeta_angle_deg": 0.0,
            "eta_angle_deg": b_angle_deg
        },
        {
            "zeta_angle_deg": b_angle_deg,
            "eta_angle_deg": 0.0
        }
    ]
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)

print("results.json written")
PYEOF

# === solve finalize ===
echo "All oracle outputs written."
