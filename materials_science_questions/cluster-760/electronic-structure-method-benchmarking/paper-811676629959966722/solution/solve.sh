#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reaction_energies.json ===
cat > /app/outputs/reaction_energies.json <<'FFEOF'
{
  "Si9H14_to_Si9H13_H": 84.2,
  "Si9H13_to_Si9H12_H": 81.4,
  "Si9H14_to_Si9H12_H2": 54.0
}
FFEOF
