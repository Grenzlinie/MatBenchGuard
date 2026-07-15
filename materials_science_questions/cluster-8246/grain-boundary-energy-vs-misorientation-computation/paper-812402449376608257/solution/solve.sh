#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_noZ_results.csv ===
cat > /app/outputs/step_01_noZ_results.csv <<'EOF'
condition,excess_volume,max_interstitial_diameter
no_Z,0.39,0.753
EOF

# === solve block: step_02_withZ_results.csv ===
cat > /app/outputs/step_02_withZ_results.csv <<'EOF'
condition,excess_volume,max_interstitial_diameter
with_Z,0.32,0.567
EOF

# === solve block: step_03_substitutional.csv ===
cat > /app/outputs/step_03_substitutional.csv <<'EOF'
condition,max_substitutional_diameter
with_Z,0.95
EOF
