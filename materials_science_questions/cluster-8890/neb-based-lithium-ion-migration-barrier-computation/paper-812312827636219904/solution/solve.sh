#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gap_results.csv ===
cat > /app/outputs/band_gap_results.csv <<'EOF'
system,band_gap_eV
LTO,2.0
LMTZO,1.9
LMTZO-Ov,1.5
EOF

# === solve block: migration_barriers.csv ===
cat > /app/outputs/migration_barriers.csv <<'EOF'
system,barrier_eV
LMTZO,0.415
LMTZO-Ov,0.345
EOF
