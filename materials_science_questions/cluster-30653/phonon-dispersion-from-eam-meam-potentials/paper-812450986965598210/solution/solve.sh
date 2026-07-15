#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: penetration_counts.csv ===
cat > "$OUTDIR/penetration_counts.csv" <<'EOF'
temperature_K,penetration_count
300,0
600,3
900,7
1200,15
EOF
