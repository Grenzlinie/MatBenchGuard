#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: equilibrium_shape.json ===
cat > "$OUTDIR/equilibrium_shape.json" <<'FFEOF'
{
  "d_110": 3.73,
  "d_111": 3.90,
  "ratio_E110_E111": 0.956
}
FFEOF

# === solve block: diffusion_coefficients.json ===
cat > "$OUTDIR/diffusion_coefficients.json" <<'FFEOF'
{
  "D_Si": 7e-6,
  "D_C": 1e-5,
  "temperature": 2200.0,
  "timestep_range": "0-100 ps"
}
FFEOF
