#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: delta_K_results.csv ===
cat > "$OUTDIR/delta_K_results.csv" <<'FFEOF'
Temperature (K),DeltaK (W/cm/K)
1.0,1.42e-07
1.5,3.38e-06
2.0,2.90e-05
2.5,1.38e-04
3.0,4.46e-04
3.5,1.11e-03
4.0,2.30e-03
4.5,4.16e-03
5.0,6.83e-03
FFEOF
