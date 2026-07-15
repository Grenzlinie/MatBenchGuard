#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduced_quantities.json ===
cat > /app/outputs/reproduced_quantities.json <<'JSONEOF'
{
  "SQ-COP-1_band_gap_ev": 1.98,
  "SQ-COP-2_band_gap_ev": 2.14,
  "SQ-COP-3_band_gap_ev": 1.79,
  "SQ-COP-1_charge_transfer_n26_e": 3.0,
  "SQ-COP-2_charge_transfer_n26_e": 1.0,
  "SQ-COP-1_diffusion_barrier_DP2_ev": 0.002
}
JSONEOF
