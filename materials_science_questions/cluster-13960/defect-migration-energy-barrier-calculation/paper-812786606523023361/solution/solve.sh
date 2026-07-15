#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: prefactor.json ===
cat > /app/outputs/prefactor.json <<'EOF'
[5.2, 8.7, 9.8]
EOF
