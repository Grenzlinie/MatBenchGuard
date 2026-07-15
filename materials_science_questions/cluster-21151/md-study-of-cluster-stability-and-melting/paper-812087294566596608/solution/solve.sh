#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: lattice_params.csv ===
cat > "$OUTDIR/lattice_params.csv" <<'EOF'
cluster_size,a,b,c
256,9.6,9.6,9.1
EOF

# === solve block: tilt_angle.csv ===
cat > "$OUTDIR/tilt_angle.csv" <<'EOF'
cluster_size,tilt_angle
256,4.0
EOF
