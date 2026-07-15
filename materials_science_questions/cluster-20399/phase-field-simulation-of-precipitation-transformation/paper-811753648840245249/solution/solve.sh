#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: alpha_case_depths.csv ===
# Write the reference alpha-case depths from the paper
cat > "$OUTDIR/alpha_case_depths.csv" <<'CSVEOF'
stress_MPa,max_depth_um
0,16.0
605,16.0
610,16.0
611,16.0
612,45.0
613,45.0
614,45.0
615,45.0
CSVEOF
