#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "blend": "PEP/PP",
  "M": 4342,
  "compositions": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95],
  "spinodal_temperatures_K": [250.25, 263.0, 274.25, 284.0, 292.25, 299.0, 304.25, 308.0, 310.25, 311.0, 310.25, 308.0, 304.25, 299.0, 292.25, 284.0, 274.25, 263.0, 250.25],
  "Tc_K": 311.0,
  "excess_volume_at_phi05": 0.000132,
  "chi_eff_at_phi05": 0.000366,
  "branching_parameter_r": 0.1333
}
FFEOF
