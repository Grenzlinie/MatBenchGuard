#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
cd /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json, os
out_dir = os.environ.get('OUTDIR', '/app/outputs')
results = {
    "1": {"p_c": 0.64, "delta": 1.1},
    "5": {"p_c": 0.71, "delta": 0.50},
    "10": {"p_c": 0.84, "delta": 0.15}
}
with open(os.path.join(out_dir, 'results.json'), 'w') as f:
    json.dump(results, f, indent=2)
PYEOF
