#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: computed_ddG_ddH.csv ===
cat > "$OUTDIR/computed_ddG_ddH.csv" <<'EOF'
triene,DeltaDeltaH_dagger,DeltaDeltaG_dagger
1,-0.96,-0.57
2,0.05,0.47
3,-0.12,-0.48
EOF
