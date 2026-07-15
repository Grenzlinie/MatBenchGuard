#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_computed_params.json ===
python3 - <<'PYEOF'
import json

params = {
    "CCP_12C12CP": {
        "v1": 1726,
        "v2_avg": 225,
        "v3": 847,
        "r_CC": 1.314,
        "r_CX": 1.626
    },
    "CCP_13C13CP": {
        "v1": 1659,
        "v2_avg": 217,
        "v3": 829,
        "r_CC": 1.314,
        "r_CX": 1.626
    },
    "CCAs_12C12CAs": {
        "v1": 1749,
        "v2_avg": 184,
        "v3": 675,
        "r_CC": 1.293,
        "r_CX": 1.734
    },
    "CCAs_13C13CAs": {
        "v1": 1680,
        "v2_avg": 176,
        "v3": 655,
        "r_CC": 1.293,
        "r_CX": 1.734
    }
}

with open("/app/outputs/step_01_computed_params.json", "w") as f:
    json.dump(params, f, indent=2)
PYEOF
