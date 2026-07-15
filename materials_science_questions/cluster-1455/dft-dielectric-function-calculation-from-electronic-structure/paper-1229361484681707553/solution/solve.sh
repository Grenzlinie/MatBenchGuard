#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: se_rsh_band_gaps.json ===
cat > "$OUTDIR/se_rsh_band_gaps.json" << 'EOF'
{"Si": 1.10, "SiO2": 10.43, "BN": 6.56, "h-BN": 7.52}
EOF
