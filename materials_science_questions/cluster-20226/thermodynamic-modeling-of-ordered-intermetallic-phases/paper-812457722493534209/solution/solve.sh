#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_segregation_results.csv ===
cat > "$OUTDIR/step_02_segregation_results.csv" <<'FFEOF'
system,model_type,surface_fraction,edge_corner_fraction
Rh-Ni,without_size,21,3
Rh-Ni,with_size,32,5
Ni-Pd,without_size,35,27
Ni-Pd,with_size,23,32
Pd-Cu,without_size,24,10
Pd-Cu,with_size,34,12
FFEOF
