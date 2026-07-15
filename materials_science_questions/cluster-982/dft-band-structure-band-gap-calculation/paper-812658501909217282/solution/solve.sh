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
# Write reference values from the paper into results.json
bluep_band_gap=2.64
pn_band_gap=1.86
hetero_band_gap=1.3
hetero_direct_gap=true
bluep_wf=7.5
pn_wf=6.8
delta_Q=0.0004
delta_V=7.99
vbm_layer='"BlueP"'
cbm_layer='"PN"'
her_bluep=2.21
her_pn=2.03
her_hetero=1.79
optical_enhancement=true

cat > "$OUTDIR/results.json" <<FFEOF
{
  "bluep_band_gap_hse06": $bluep_band_gap,
  "pn_band_gap_hse06": $pn_band_gap,
  "hetero_band_gap": $hetero_band_gap,
  "hetero_direct_gap": $hetero_direct_gap,
  "bluep_work_function": $bluep_wf,
  "pn_work_function": $pn_wf,
  "charge_transfer_delta_Q": $delta_Q,
  "potential_drop_delta_V_H": $delta_V,
  "vbm_layer": $vbm_layer,
  "cbm_layer": $cbm_layer,
  "her_delta_G_bluep": $her_bluep,
  "her_delta_G_pn": $her_pn,
  "her_delta_G_hetero": $her_hetero,
  "optical_absorption_enhancement": $optical_enhancement
}
FFEOF
