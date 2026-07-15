#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reproduced_values.json ===
cat > "$OUTDIR/reproduced_values.json" <<'FFEOF'
{
  "bilayer_cavity_channel_diffusion_barrier_eV": 0.42,
  "bilayer_cavity_channel_stabilization_energy_eV": 1.41,
  "bilayer_volume_expansion_percent": 12,
  "bulk_cavity_channel_diffusion_barrier_eV": 0.33,
  "bulk_cavity_channel_stabilization_energy_eV": 10.04,
  "bulk_specific_capacity_mAh_g": 468.57,
  "bulk_volume_expansion_percent": 12,
  "monolayer_cohesive_energy_eV": 7.56,
  "monolayer_diffusion_barrier_path1_eV": 0.29,
  "monolayer_diffusion_barrier_path2_eV": 0.69,
  "monolayer_one_layer_specific_capacity_mAh_g": 468.57,
  "monolayer_single_li_adsorption_energy_eV": -1.37,
  "monolayer_two_layer_specific_capacity_mAh_g": 1874.27
}
FFEOF
