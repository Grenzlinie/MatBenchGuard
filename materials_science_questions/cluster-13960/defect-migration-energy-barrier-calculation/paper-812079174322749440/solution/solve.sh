#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduction_results.json ===
cat > /app/outputs/reproduction_results.json << 'FFEOF'
{
  "max_coverage": {
    "pristine": 4,
    "-CH3": 4,
    "-F": 6,
    "-SH": 9
  },
  "capacity_mAh_g": {
    "pristine": 1061,
    "-CH3": 831.3,
    "-F": 1174.2,
    "-SH": 1462.4
  },
  "average_OCV_V": {
    "-CH3": 1.34,
    "-F": 0.64,
    "-SH": 0.68
  },
  "pristine_stepwise_OCV_V": [
    1.81,
    1.65,
    1.58,
    1.50
  ],
  "GYCTF_SH_diffusion_barrier_eV": 0.354
}
FFEOF
