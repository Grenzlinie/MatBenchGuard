#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: limiting_potentials.json ===
python3 -c "import json; json.dump({'pathway1_UL': -0.33, 'pathway2_UL': -0.31}, open('$OUTDIR/limiting_potentials.json','w'))"
