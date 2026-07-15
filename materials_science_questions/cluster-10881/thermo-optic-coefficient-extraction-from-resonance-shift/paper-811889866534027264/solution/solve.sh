#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dispersion_fit_1.5K.json ===
cat > "$OUTDIR/dispersion_fit_1.5K.json" << 'FFEOF'
{
  "resonance1": {
    "sigma0": 131.3,
    "S": 0.0027,
    "gamma": 0.0045
  },
  "resonance2": {
    "sigma0": 264.4,
    "S": 0.049,
    "gamma": 0.025
  }
}
FFEOF
