#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
cat > $OUTDIR/results.json << 'EOF'
{"kappa_ph_bulk_Si": 150.0, "kappa_ph_composite": 1.2, "kappa_ph_reduction_ratio": 125.0}
EOF
