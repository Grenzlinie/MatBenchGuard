#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" <<'EOF'
material,band_gap_eV,magnetic_moment_mu_B
MnO,3.59,4.74
FeO,2.50,3.72
CoO,2.66,2.70
NiO,3.90,1.68
EOF
