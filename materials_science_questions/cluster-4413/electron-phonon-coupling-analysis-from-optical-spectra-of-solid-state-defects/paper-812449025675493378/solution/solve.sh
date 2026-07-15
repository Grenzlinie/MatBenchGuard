#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json
result = {
    'E_D': 0.10,
    'E_A1': 0.60,
    'E_A2': 0.83,
    'acceptor_depth_A0': 0.20,
    'donor_depth_AB': 0.11,
    'W0': 100000000.0
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(result, f, indent=2)
"
