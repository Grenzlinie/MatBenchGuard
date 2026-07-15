#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: absorption_results.json ===
cat > "$OUTDIR/absorption_results.json" << 'EOF'
{
  "planar_absorbed_power_W_m2": 200.0,
  "textured_absorbed_power_W_m2": 280.0,
  "enhancement_ratio": 1.4
}
EOF
