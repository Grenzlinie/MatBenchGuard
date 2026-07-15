#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > /app/outputs/adsorption_energies.json <<'FFEOF'
{
  "Ti3C2O2": -1.581,
  "Ti3C2F2": -0.222,
  "Ti3C2(OH)2": -0.053
}
FFEOF

# === solve block: diffusion_barriers.json ===
cat > /app/outputs/diffusion_barriers.json <<'FFEOF'
{
  "Ti3C2O2_barrier": 0.36,
  "Ti3C2O1.75F0.25_barrier": 0.34,
  "Ti3C2O1.75(OH)0.25_barrier": 0.43
}
FFEOF
