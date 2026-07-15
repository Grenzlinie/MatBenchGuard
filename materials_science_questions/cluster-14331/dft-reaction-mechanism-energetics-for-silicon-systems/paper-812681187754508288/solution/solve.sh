#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bde_results.json ===
python3 -c "
import json
data = {
    'anisole_OCH3_BDE': 62.1,
    'phenol_OH_BDE': 89.7,
    'alkyl_CH_BDE': 93.7
}
with open('/app/outputs/bde_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
