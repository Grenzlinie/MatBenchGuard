#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "total_free_energy": 64.93,
  "surface_tension": 18.3,
  "excess_internal_energy": 38.9,
  "stages": {
    "Fb_minus_Fa": 96.72,
    "Fc_minus_Fb": 55.73,
    "Fd_minus_Fc": -69.69,
    "Fe_minus_Fd": -9.97,
    "Ff_minus_Fe": -7.86
  }
}
EOF
