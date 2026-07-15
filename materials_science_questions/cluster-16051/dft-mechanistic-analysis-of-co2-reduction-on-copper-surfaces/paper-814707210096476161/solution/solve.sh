#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: activation_barriers.csv ===
cat > "$OUTDIR/activation_barriers.csv" << 'EOF'
catalyst,barrier_kJ_mol
CuIIY,78.32
CuIICuIIaY,64.59
CuIICuI'aY,138.96
CuIICsIIa*Y,55.57
EOF
