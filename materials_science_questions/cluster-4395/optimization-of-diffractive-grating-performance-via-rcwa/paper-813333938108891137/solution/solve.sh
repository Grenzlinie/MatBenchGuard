#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: sbc_efficiencies.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 <<'PYEOF'
import json
data = {
    "two_channel": [
        {"w": 0.1, "eta_T": 99.0, "eta_D": 99.7, "eta": 98.65},
        {"w": 0.3, "eta_T": 96.8, "eta_D": 89.0, "eta": 92.16}
    ],
    "three_channel": [
        {"w": 0.1, "eta_1D": 99.7, "eta_2T_prime": 99.0, "eta_1T": 99.0, "eta_1T_prime": 99.1, "eta_2D": 99.7, "eta": 97.37},
        {"w": 0.3, "eta_1D": 89.0, "eta_2T_prime": 96.8, "eta_1T": 96.8, "eta_1T_prime": 99.1, "eta_2D": 89.0, "eta": 88.98}
    ]
}
with open('/app/outputs/sbc_efficiencies.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
