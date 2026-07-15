#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_moments.csv ===
OUTDIR=${OUTDIR:-/app/outputs}
mkdir -p "$OUTDIR"
cat > "$OUTDIR/magnetic_moments.csv" <<'FFEOF'
slab_layers,layer_index,moment
2,1,0.31
2,2,0.31
3,1,0.30
3,2,0.50
3,3,0.30
4,1,0.12
4,2,0.21
4,3,0.21
4,4,0.12
5,1,0.02
5,2,0.03
5,3,0.04
5,4,0.03
5,5,0.02
FFEOF
