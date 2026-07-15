#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: entropy_cyclohexane.json ===
cat > /app/outputs/entropy_cyclohexane.json <<'FFEOF'
{"entropy_298_16": 48.84}
FFEOF
