#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: h_trapping_maxima.json ===
cat > "$OUTDIR/h_trapping_maxima.json" <<'EOF'
{
  "V-O": 1,
  "2V-O": 4,
  "2V-2O": 3,
  "2V-O-He": 2
}
EOF
