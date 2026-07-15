#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: electronic_results.json ===
cat > "$OUTDIR/electronic_results.json" << 'EOF'
{
  "majority_band_gap": 6.70,
  "minority_metallic": true,
  "total_magnetic_moment": 4.15,
  "fe_magnetic_moment": 4.00
}
EOF
