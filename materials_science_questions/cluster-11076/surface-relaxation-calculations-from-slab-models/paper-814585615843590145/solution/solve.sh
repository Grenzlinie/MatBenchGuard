#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relaxed_parameters.json ===
cat > "$OUTDIR/relaxed_parameters.json" <<'FFEOF'
{
  "delta_1_perp": 0.775,
  "delta_1_y": 4.593,
  "d_12_y": 4.036,
  "d_12_perp": 0.639,
  "delta_2_perp": 0.065,
  "omega_1": 17.7
}
FFEOF

# === solve block: surface_band_structure.json ===
cat > "$OUTDIR/surface_band_structure.json" <<'FFEOF'
{
  "s1_energy_M_point": -0.3,
  "surface_state_exists": true
}
FFEOF
