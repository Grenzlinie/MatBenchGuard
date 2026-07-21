#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > /app/outputs/adsorption_energies.json <<'EOF'
{
  "surface": -0.548,
  "edge": -3.298,
  "heterojunction": -1.306
}
EOF
