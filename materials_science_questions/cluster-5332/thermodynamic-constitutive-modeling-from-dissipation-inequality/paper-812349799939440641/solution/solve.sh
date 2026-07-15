#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: opt_design.json ===
python3 -c "
import json, math
s1 = 5.0
s2 = 5.525
area = 2500 - math.pi * s1 * s2
data = {'s1': s1, 's2': s2, 'final_area': area}
with open('$OUTDIR/opt_design.json', 'w') as f:
    json.dump(data, f, indent=2)
"
