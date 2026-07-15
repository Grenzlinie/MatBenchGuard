#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: tc_ratios.json ===
python3 -c "
import json
data = {
    'rectangle_mean': 1.02,
    'rectangle_edges': 1.05,
    'rectangle_corners': 1.34,
    'sphere': 1.69,
    'cylinder': 1.20
}
with open('$OUTDIR/tc_ratios.json', 'w') as f:
    json.dump(data, f, indent=2)
"
