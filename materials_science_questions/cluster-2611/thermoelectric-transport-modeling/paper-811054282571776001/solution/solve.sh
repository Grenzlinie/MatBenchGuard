#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predictions.csv ===
# Write the correct predictions for the seven compounds listed in the task
cat > /app/outputs/predictions.csv <<'EOF'
compound,prediction
Ca5Sn2As6,unbridged
Sr5Sn2As6,unbridged
Sr5Sn2P6,unbridged
Ca5Ga2Sb6,bridged
Ca5In2Sb6,bridged
Ca5Ga2As6,bridged
Ca5Al2Sb6,bridged
EOF
