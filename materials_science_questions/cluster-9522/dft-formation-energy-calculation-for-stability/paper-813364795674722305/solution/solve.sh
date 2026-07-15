#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_enthalpies.csv ===
cat > /app/outputs/formation_enthalpies.csv <<'EOF'
M_element,x,Delta_Hf
None,0,-0.10
Sc,1,-0.25
Ti,1,-0.24
Zn,1,-0.15
Y,1,-0.28
Zr,1,-0.30
Hf,1,-0.32
La,1,-0.20
Al,1,-0.18
Mg,1,-0.22
EOF
