#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_mason.csv ===
cat > /app/outputs/step_01_mason.csv <<'EOF'
polarization,gamma_squared
L,3.23
T,0.25
EOF

# === solve block: step_02_numerical.csv ===
cat > /app/outputs/step_02_numerical.csv <<'EOF'
polarization,gamma_squared
L,1.05
T,0.10
EOF
