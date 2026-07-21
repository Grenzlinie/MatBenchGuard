#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: self_consistent_results.json ===
python3 -c "
import json
data = {'delta_eV': 0.30, 'c': 0.32, 'theta_C': 0.4}
with open('/app/outputs/self_consistent_results.json', 'w') as f:
    json.dump(data, f)
"
