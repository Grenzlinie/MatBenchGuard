#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: si_h_dissociation_energies.json ===
cat > /app/outputs/si_h_dissociation_energies.json <<'FFEOF'
{
  "lateral_nlsd": 87.92,
  "internal_nlsd": 84.63
}
FFEOF
