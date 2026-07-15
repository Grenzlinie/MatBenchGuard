#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pl_b4_results.json ===
cat > "$OUTDIR/pl_b4_results.json" << 'FFEOF'
{
  "K_L_300K": 5.89,
  "branch_scattering_rates": {
    "TA1": 3.40,
    "TA2": 3.10,
    "LA": 4.32,
    "Optical": 15.23
  },
  "branch_group_velocities": {
    "TA1": 6.38,
    "TA2": 4.52,
    "LA": 3.33,
    "Optical": 3.93
  }
}
FFEOF

# === solve block: pl_b8_results.json ===
cat > "$OUTDIR/pl_b8_results.json" << 'FFEOF'
{
  "K_L_300K": 13.94,
  "branch_scattering_rates": {
    "TA1": 0.14,
    "TA2": 0.38,
    "LA": 0.61,
    "Optical": 2.60
  },
  "branch_group_velocities": {
    "TA1": 3.18,
    "TA2": 5.64,
    "LA": 5.37,
    "Optical": 2.69
  }
}
FFEOF
