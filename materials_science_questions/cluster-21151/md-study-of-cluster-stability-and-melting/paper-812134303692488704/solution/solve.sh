#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: diffusion_activation_parameters.json ===
cat > "$OUTDIR/diffusion_activation_parameters.json" <<'FFEOF'
{
  "Ea_melt_eV": 1.05,
  "D0_melt_m2_per_s": 5.25e-6,
  "Ea_glass_eV": 1.2,
  "D0_glass_m2_per_s": 2.05e-5
}
FFEOF
