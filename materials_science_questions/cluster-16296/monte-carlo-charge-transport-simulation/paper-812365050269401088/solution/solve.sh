#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: threshold_fields.json ===
cat > "$OUTDIR/threshold_fields.json" << 'EOF'
{"threshold_77K": 4.0, "threshold_300K": 5.5}
EOF
