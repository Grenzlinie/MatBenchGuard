#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_barriers.json ===
cat > /app/outputs/computed_barriers.json <<'FFEOF'
{
  "surface_diffusion_barrier_eV": 0.97,
  "schwoebel_barrier_211_eV": 0.61,
  "schwoebel_barrier_112_eV": 0.16
}
FFEOF
