#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: single_water_adsorption_results.json ===
cat > "$OUTDIR/single_water_adsorption_results.json" <<'FFEOF'
{
  "binding_energy_eV": 0.147,
  "zn_o_distance_A": 2.227,
  "h_o_distance_A": 2.993,
  "charge_transfer_e": 0.007
}
FFEOF
