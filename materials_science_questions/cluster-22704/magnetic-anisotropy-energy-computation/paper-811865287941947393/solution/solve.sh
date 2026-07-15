#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_properties.csv ===
cat > /app/outputs/magnetic_properties.csv <<'EOF'
system,Ms,ML,EMAE
MnPc,3.0,0.19,2.72
FePc,2.0,0.15,-1.18
CoPc,1.0,0.20,-1.45
NiPc,0.0,0.0,0.0
EOF
