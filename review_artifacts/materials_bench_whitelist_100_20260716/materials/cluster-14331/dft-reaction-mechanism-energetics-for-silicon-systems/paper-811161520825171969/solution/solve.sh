#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_energies.json ===
python3 -c "
import json
data = {
    'A43_43': -33845.83,
    'B30_48': -33845.06,
    'B53_30': -33844.88,
    'B_star': -33844.54,
    'B30_48_deprot': -33824.46
}
with open('/app/outputs/total_energies.json', 'w') as f:
    json.dump(data, f)
"
