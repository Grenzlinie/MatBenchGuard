#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dynamical_stability.json ===
cat > /app/outputs/dynamical_stability.json << 'FFEOF'
{
  "m11": false,
  "m14": true,
  "m12": true,
  "o70": true,
  "t139": false
}
FFEOF

# === solve block: cohesive_energies.json ===
cat > /app/outputs/cohesive_energies.json << 'FFEOF'
{
  "m14": -17.500,
  "m12": -17.521,
  "o70": -17.226
}
FFEOF
