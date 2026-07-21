#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: resonance.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

python3 << 'PYEOF'
import json

data = {
    "epsilon_res": 0.56,
    "omega_res": 0.748331477    # sqrt(0.56)
}

with open("/app/outputs/resonance.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
