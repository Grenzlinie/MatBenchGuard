#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: young_moduli.csv ===
cat > "$OUTDIR/young_moduli.csv" <<'FFEOF'
Model,Temperature(K),YoungsModulus(GPa)
Model-1,25,119
Model-1,50,112
Model-1,75,110
Model-1,100,101
Model-1,125,94
Model-1,150,85
Model-1,175,84
Model-1,200,79
Model-2,25,115
Model-2,50,109
Model-2,75,109
Model-2,100,99
Model-2,125,85
Model-2,150,86
Model-2,175,78
Model-2,200,77
FFEOF
