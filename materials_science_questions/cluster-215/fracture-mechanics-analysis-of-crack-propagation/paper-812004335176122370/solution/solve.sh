#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table1.csv ===
cat > "$OUTDIR/table1.csv" <<'FFEOF'
b_over_a,nu,A,compressive_strength_ratio,transition_stress_ratio,shear_stress_ratio_at_minus35
0.8,0.1,1.883,-7.32,-2.54,11.300
1.0,0.3,1.399,-4.75,-0.96,8.399
1.0,0.4,1.200,-3.84,-0.44,7.199
FFEOF
