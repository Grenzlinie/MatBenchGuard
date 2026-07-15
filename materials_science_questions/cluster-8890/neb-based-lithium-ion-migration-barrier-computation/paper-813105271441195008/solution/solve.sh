#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_hull_distances.csv ===
cat > /app/outputs/step_01_hull_distances.csv <<'EOF'
M,hull_distance_meV_per_atom
Ti,0.0
V,0.0
Mn,0.0
Fe,0.0
Ni,0.0
Ge,0.0
Zr,0.0
Mo,0.0
Ru,0.0
Rh,0.0
Pd,0.0
Sn,0.0
Ir,0.0
Pt,0.0
Pb,0.0
EOF
