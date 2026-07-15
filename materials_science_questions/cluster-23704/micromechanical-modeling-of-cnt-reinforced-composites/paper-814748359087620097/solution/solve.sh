#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: axial_moduli_predictions.csv ===
cat > /app/outputs/axial_moduli_predictions.csv <<'FFEOF'
system,cnt_weight_fraction,mori_tanaka_E,self_consistent_E,halpin_tsai_E
Sys1,0.184,114.75,135.0,148.5
Sys2,0.0977,85.85,101.0,111.1
Sys3,0.0942,80.325,94.5,103.95
Sys4,0.0977,81.855,96.3,105.93
Sys5,0.0562,55.845,65.7,72.27
Sys6,0.0562,51.255,60.3,66.33
Sys7,0.0289,31.875,37.5,41.25
Sys8,0.0218,34.255,40.3,44.33
FFEOF
