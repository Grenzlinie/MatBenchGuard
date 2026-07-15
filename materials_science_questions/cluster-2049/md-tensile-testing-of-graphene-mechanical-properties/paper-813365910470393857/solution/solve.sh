#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_02_2D_frequencies.csv ===
# Write CSV with 2D Raman peak frequencies for two cases
cat > "$OUTDIR/step_02_2D_frequencies.csv" <<'FFEOF'
strain,frequency,case
0.0,2678.0,no_bandstructure
-0.2,2691.2,no_bandstructure
-0.4,2704.4,no_bandstructure
-0.6,2717.6,no_bandstructure
-0.8,2730.8,no_bandstructure
-1.0,2744.0,no_bandstructure
0.0,2678.0,with_bandstructure
-0.2,2693.8,with_bandstructure
-0.4,2709.6,with_bandstructure
-0.6,2725.4,with_bandstructure
-0.8,2741.2,with_bandstructure
-1.0,2757.0,with_bandstructure
FFEOF
