#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_overlap_results.json ===
cat > /app/outputs/step_01_overlap_results.json << 'FFEOF'
{
  "electron_0.2": {
    "extended_s": 0.048,
    "d_wave": 0.03,
    "ratio": 1.6
  },
  "half_filling": {
    "extended_s": 0.06,
    "d_wave": 0.03,
    "ratio": 2.0
  },
  "hole_0.28": {
    "extended_s": 0.15,
    "d_wave": 0.03,
    "ratio": 5.0
  }
}
FFEOF
