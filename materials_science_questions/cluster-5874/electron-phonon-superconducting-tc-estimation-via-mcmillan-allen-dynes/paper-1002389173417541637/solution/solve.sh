#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table_1.csv ===
cat > "$OUTDIR/table_1.csv" <<'FFEOF'
compound,lambda_Gamma,lambda
O,0.120,0.43
OH,0.134,0.46
FFEOF
