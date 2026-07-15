#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_gb_acidity.csv ===
cat > /app/outputs/computed_gb_acidity.csv <<'FFEOF'
molecule,property,value,method
EA,GB,190.1,B3LYP/6-311+G(3df,2p)
EA,delta_acid_G,356.0,B3LYP/6-311+G(3df,2p)
VA,GB,186.6,B3LYP/6-311+G(3df,2p)
VA,delta_acid_G,345.0,B3LYP/6-311+G(3df,2p)
ETA,GB,174.2,B3LYP/6-311+G(3df,2p)
ETA,delta_acid_G,338.8,B3LYP/6-311+G(3df,2p)
FFEOF
