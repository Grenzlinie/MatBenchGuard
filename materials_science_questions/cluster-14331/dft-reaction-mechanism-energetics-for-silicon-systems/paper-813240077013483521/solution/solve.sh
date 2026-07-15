#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: energy_profile.json ===
cat > /app/outputs/energy_profile.json <<'EOF'
{
  "reactants": 0.0,
  "TS1": 19.6,
  "Int1": -20.0,
  "TS2": -10.9,
  "Int2": -50.0,
  "TS3": -41.0,
  "product": -79.3
}
EOF
