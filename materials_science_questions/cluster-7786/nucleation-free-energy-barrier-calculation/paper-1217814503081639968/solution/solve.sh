#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nucleation_temperatures.csv ===
cat > /app/outputs/nucleation_temperatures.csv <<'CSVEOF'
substrate_type,orientation,mismatch_delta,T_n_K
rigid,pII,5,254.6
rigid,pII,7,244.4
rigid,pII,8,241.4
wells,pII,5,255.8
wells,pII,7,245.1
wells,pII,8,242.9
wells,basal,5,255.5
wells,pI,5,257.0
wells,pII,5,256.0
wells,basal,7,245.5
wells,pI,7,247.0
wells,pII,7,246.0
wells,basal,8,243.0
wells,pI,8,244.0
wells,pII,8,243.5
CSVEOF
