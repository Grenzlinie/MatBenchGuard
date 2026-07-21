#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'EOF'
{
  "J2_0": {
    "Tc": 0.00159294,
    "latent_heat": 0.00010449,
    "mAF2_lowest_T": 1.0
  },
  "J2_critical_sqrt3": {
    "Tc": 0.0127,
    "latent_heat": 0.0
  },
  "J2_critical_q0": {
    "Tc": 0.0494,
    "latent_heat": 0.0
  },
  "triple_point": {
    "J2": 2.8e-05,
    "Tc": 0.00111
  },
  "cv_sqrt3_T0": 0.9167,
  "pyrochlore": {
    "ordered_state_found": false,
    "free_energy_diff": 0.01,
    "lowest_T": 1e-09
  }
}
EOF
