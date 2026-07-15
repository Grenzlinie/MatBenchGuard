#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: contact_analytical_check.json ===
python3 -c "
import json
d = {
    'contact_velocity': 0.05,
    'contact_traction': -0.05,
    'left_release_velocity': 0.0,
    'right_release_velocity': 0.1
}
with open('/app/outputs/contact_analytical_check.json', 'w') as f:
    json.dump(d, f, indent=2)
"
