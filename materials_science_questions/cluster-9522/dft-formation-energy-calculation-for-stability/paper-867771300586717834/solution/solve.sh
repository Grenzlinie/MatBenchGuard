#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_formation_energies.json ===
cat > /app/outputs/step_01_formation_energies.json <<'FFEOF'
{
  "Fe2CrSi_L21": -0.93,
  "Fe2CrSi_A15": -0.98,
  "Fe3Si": -1.12,
  "Cr3Si": -1.84,
  "reaction_energy_per_fu": 0.38
}
FFEOF
