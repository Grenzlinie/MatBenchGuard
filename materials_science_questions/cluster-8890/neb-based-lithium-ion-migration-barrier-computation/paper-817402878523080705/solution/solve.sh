#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reproduced_results.json ===
cat > /app/outputs/reproduced_results.json <<'FFEOF'
{
  "band_gap_MnO2": 1.079,
  "band_gap_composite": 0.0,
  "diffusion_barrier_Li_MnO2": 1.09,
  "diffusion_barrier_Li_composite": 0.76,
  "diffusion_barrier_Li_graphene": 0.058,
  "diffusion_barrier_Na_MnO2": 1.31,
  "diffusion_barrier_Na_composite": 0.91,
  "diffusion_barrier_Mg_MnO2": 1.53,
  "diffusion_barrier_Mg_composite": 1.15,
  "diffusion_ordering_pure": ["Li", "Na", "Mg"],
  "diffusion_ordering_composite": ["Li", "Na", "Mg"]
}
FFEOF
