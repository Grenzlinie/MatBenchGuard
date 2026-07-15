#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.csv ===
cat > "/app/outputs/dft_results.csv" <<'FFEOF'
E_a,system,ΔG_H2,ΔG_H2O2
0.508,NaNbO3,0.924,1.80
0.360,V-NaNbO3,0.670,1.20
FFEOF
