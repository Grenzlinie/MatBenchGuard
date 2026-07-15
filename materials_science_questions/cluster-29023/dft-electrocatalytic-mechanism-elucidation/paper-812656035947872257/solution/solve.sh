#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: limiting_potential_differences.json ===
cat > /app/outputs/limiting_potential_differences.json <<'FFEOF'
{
  "NiN4C": 0.46,
  "NC": -0.38,
  "Ni4NC": -0.17
}
FFEOF
echo '[solve] wrote limiting_potential_differences.json'
