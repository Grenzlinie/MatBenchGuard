#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: mobility_results.json ===
python3 -c "
import json
d = {
    'phonon_limited_mobility': 220.0,
    'realistic_mobility': 20.0,
    'mobility_ratio': 0.09090909090909091
}
with open('$OUTDIR/mobility_results.json', 'w') as f:
    json.dump(d, f, indent=2)
"
