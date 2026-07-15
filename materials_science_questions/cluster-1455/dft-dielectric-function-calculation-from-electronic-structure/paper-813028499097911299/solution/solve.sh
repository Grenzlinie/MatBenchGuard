#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gap_vs_strain.csv ===
cat > "$OUTDIR/band_gap_vs_strain.csv" << 'EOF'
strain_percent,band_gap_eV
-8,0.75
0,1.82
8,1.85
EOF

# === solve block: dielectric_function.csv ===
python3 /solution/generate_dielectric.py > "$OUTDIR/dielectric_function.csv"
