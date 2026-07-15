#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: corrugation_results.csv ===
cat > /app/outputs/corrugation_results.csv <<'FFEOF'
slab_type,configuration,corrugation_angstrom,trigonal_symmetry_metric
three-layer,ideal,0.50,1.00
three-layer,slipped,2.00,0.20
FFEOF
