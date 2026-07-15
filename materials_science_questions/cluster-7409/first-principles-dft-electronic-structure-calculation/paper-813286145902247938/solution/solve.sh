#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: band_positions.json ===
cat > "$OUTDIR/band_positions.json" <<'EOF'
{
  "U-J_3.2": 2.9,
  "U-J_7.2": 3.3
}
EOF

# === solve block: formation_energy.json ===
cat > "$OUTDIR/formation_energy.json" <<'EOF'
{
  "Bi_plus3_defect_formation_energy_eV": 14.54
}
EOF
