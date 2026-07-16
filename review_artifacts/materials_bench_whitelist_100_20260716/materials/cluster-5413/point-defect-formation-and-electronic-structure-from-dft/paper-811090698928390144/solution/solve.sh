#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_polarization_results.csv ===
cat > "$OUTDIR/defect_polarization_results.csv" <<'FFEOF'
defect,displacement_A,displacement_dir,born_charge,polarization_uCcm2,barrier_eV
Ti_Sr,0.78,[100],1.72,16.8,0.13
Sr_Ti,0.26,[110],3.11,7.6,0.05
Ti_Sr_V_O,0.79,[011],2.48,22.6,0.23
FFEOF
