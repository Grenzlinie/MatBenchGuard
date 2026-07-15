#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: output_tc.json ===
python3 -c "
import json
data = {
    'Tc': 12.0,
    'lambda': 0.7,
    'omega_log': 600.0
}
with open('$OUTDIR/output_tc.json', 'w') as f:
    json.dump(data, f)
"
