#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
python3 -c "
import json
data = {
    'cubic': {'c11': 831, 'c12': 144, 'c44': 110, 'B': 373, 'G': 203},
    'hexagonal': {'c11': 864, 'c12': 380, 'c13': 204, 'c33': 1249, 'c44': 426, 'c66': 242, 'B': 345, 'G': 365}
}
with open('$OUTDIR/elastic_constants.json', 'w') as f:
    json.dump(data, f, indent=2)
"
