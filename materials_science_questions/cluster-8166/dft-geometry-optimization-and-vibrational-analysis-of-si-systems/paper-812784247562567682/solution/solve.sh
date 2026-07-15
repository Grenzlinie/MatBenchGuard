#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_energies.json ===
cat > /app/outputs/step_01_energies.json <<'FFEOF'
{
  "adamantane_energy_Ry": -4161.84177,
  "energy_difference_eV": 1.543,
  "fluorite_energy_Ry": -4161.95519
}
FFEOF
