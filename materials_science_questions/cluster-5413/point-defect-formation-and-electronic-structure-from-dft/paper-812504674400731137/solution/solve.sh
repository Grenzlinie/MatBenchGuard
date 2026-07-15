#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_formation_energies.json ===
cat > /app/outputs/step_01_formation_energies.json <<'FFEOF'
{
  "STO": 5.0,
  "Sr3Ti2O7": 6.0
}
FFEOF

# === solve block: step_02_diffusion_barriers.json ===
cat > /app/outputs/step_02_diffusion_barriers.json <<'FFEOF'
{
  "STO": 0.48,
  "Sr3Ti2O7": 1.34
}
FFEOF
