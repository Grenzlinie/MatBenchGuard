#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_shallow_grating_results.json ===
cat > /app/outputs/step_01_shallow_grating_results.json <<'EOF'
{"alpha_cm1": 2.0, "gamma": 0.4}
EOF
