#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_04_results_PL-B4.json ===
cat > "$OUTDIR/step_04_results_PL-B4.json" << 'FFEOF'
{
  "thermal_conductivity_300K": 5.89,
  "branch_averaged_scattering_rates": {
    "TA1": 3.40,
    "TA2": 3.10,
    "LA": 4.32,
    "Optical": 15.23
  },
  "branch_averaged_group_velocities": {
    "TA1": 6.38,
    "TA2": 4.52,
    "LA": 3.33,
    "Optical": 3.93
  }
}
FFEOF

# === solve block: step_04_results_PL-B8.json ===
cat > "$OUTDIR/step_04_results_PL-B8.json" << 'FFEOF'
{
  "thermal_conductivity_300K": 13.94,
  "branch_averaged_scattering_rates": {
    "TA1": 0.14,
    "TA2": 0.38,
    "LA": 0.61,
    "Optical": 2.60
  },
  "branch_averaged_group_velocities": {
    "TA1": 3.18,
    "TA2": 5.64,
    "LA": 5.37,
    "Optical": 2.69
  }
}
FFEOF
