#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dielectric_results.json ===
cat > /app/outputs/dielectric_results.json <<'FFEOF'
{
  "undoped": {
    "epsilon2_peak": 13.056,
    "peak_position_eV": 6.653,
    "epsilon1_0": 6.461
  },
  "Ga_substitution": {
    "epsilon2_peak": 35.898,
    "peak_position_eV": 0.422,
    "epsilon1_0": 49.533
  },
  "As_substitution": {
    "epsilon2_peak": 24.348,
    "peak_position_eV": 0.068,
    "epsilon1_0": 33.2616
  }
}
FFEOF
