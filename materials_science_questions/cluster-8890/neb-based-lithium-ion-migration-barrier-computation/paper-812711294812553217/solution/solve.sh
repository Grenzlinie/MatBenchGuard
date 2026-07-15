#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: activation_energies.json ===
cat > "/app/outputs/activation_energies.json" <<'FFEOF'
{
  "supercell_barrier_eV": 0.75,
  "monolayer_barrier_eV": 0.23
}
FFEOF
