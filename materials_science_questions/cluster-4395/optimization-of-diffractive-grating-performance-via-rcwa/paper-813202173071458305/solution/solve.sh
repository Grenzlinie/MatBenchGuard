#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimal_parameters.json ===
cat > "$OUTDIR/optimal_parameters.json" <<'FFEOF'
{
  "ridge_height_um": 0.6,
  "grating_depth_um": 0.1,
  "grating_width_um": 0.3,
  "period_um": 0.73,
  "threshold_gain_per_um": 0.616,
  "Qw_confinement_factor": 16.3
}
FFEOF
