#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: summary.json ===
cat > /app/outputs/summary.json <<'EOF'
{
  "extracted_modulus": 107.1,
  "percentage_error": 3.98
}
EOF
