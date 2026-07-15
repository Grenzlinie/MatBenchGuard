#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: intensity_ratios.json ===
cat > "$OUTDIR/intensity_ratios.json" <<'EOF'
{
  "v1": 6.32,
  "v2": 2.13,
  "v3": 0.958,
  "v4": 0.495,
  "v5": 0.282
}
EOF
