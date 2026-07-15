#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_migration_results.csv ===
cat > "$OUTDIR/step_01_migration_results.csv" <<'EOF'
A_order,B_order,dimensionality,migration_energy_eV
C,C,2D,2.1
C,L,1D,1.3
C,R,1D,1.0
L,C,2D,2.7
L,L,2D,0.8
L,R,2D,1.3
R,C,1D,2.2
R,L,2D,0.6
R,R,3D,1.3
EOF
