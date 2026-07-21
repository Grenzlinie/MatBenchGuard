#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_03_cyclotron_orbit_freq.csv ===
cat > "/app/outputs/step_03_cyclotron_orbit_freq.csv" <<'FFEOF'
orbit_label,frequency_T,mass_ratio_m0
α,477,4.0
β,438,3.7
γ,404,3.9
δ2,1340,6.2
ε5,5310,5310
ε8,7610,7610
FFEOF
