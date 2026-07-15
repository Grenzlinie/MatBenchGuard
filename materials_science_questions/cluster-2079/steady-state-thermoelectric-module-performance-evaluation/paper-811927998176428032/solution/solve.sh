#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: cold_side_gamma.txt ===
cat > "$OUTDIR/cold_side_gamma.txt" <<'FFEOF'
3000.0
FFEOF

# === solve block: hot_side_gamma.txt ===
cat > "$OUTDIR/hot_side_gamma.txt" <<'FFEOF'
15.0
FFEOF
