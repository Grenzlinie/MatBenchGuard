#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_predictions.csv ===
cat > /app/outputs/step_01_predictions.csv <<'EOF'
l,graphite,ferrite,pearlite,iron_carbide
10,11.4,44.2,16.2,28.2
15,11.7,69.2,13.3,5.8
35,10.3,62.8,26.9,0.0
55,12.3,55.0,32.7,0.0
95,10.5,47.2,42.3,0.0
EOF
