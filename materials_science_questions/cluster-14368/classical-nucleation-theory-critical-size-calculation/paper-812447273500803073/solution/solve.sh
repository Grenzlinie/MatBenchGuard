#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_values.json ===
python3 << 'PYEOF'
import json
data = {
    "R_crit": 3.869e6,
    "T_s": 1.48e-4,
    "n_0star": 575.0,
    "n_c": 575.0 / 3.595e15,
    "S": 3.595e15,
    "Delta_Gv": -1.278e23,
    "r_star": 1.4e-8,
    "gamma_cv": 8.9e14,
    "Delta_Gstar": 0.2487,
    "phi": 0.339,
    "theta": 78.0
}
with open('/app/outputs/computed_values.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
