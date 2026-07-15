#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: migration_results.csv ===
cat > "$OUTDIR/migration_results.csv" << 'EOF'
ordering,migration_energy_eV,dimensionality
AC/BC,2.1,2D
AC/BL,1.3,1D
AC/BR,1.0,1D
AL/BC,2.7,2D
AL/BL,0.8,2D
AL/BR,1.3,2D
AR/BC,2.2,1D
AR/BL,0.6,2D
AR/BR,1.3,3D
EOF
