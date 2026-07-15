#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: activation_energies.json ===
cat > "$OUTDIR/activation_energies.json" << 'FFEOF'
{
  "Ea_mech1": 2.52,
  "Ea_mech2": 1.34
}
FFEOF
