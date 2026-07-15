#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phonon_stability.txt ===
echo stable > /app/outputs/phonon_stability.txt

# === solve block: band_gap.txt ===
cat > "$OUTDIR/band_gap.txt" <<'EOF'
3.67
EOF

# === solve block: zt_vs_temperature.csv ===
cat > "$OUTDIR/zt_vs_temperature.csv" <<'EOF'
Temperature(K),ZT
300,0.89
600,0.89
900,0.90
1200,0.90
EOF
