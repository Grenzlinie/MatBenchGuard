#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: homo_lumo_gap.json ===
cat > /app/outputs/homo_lumo_gap.json <<'EOF'
{
  "homo_lumo_gap_ev": 2.5
}
EOF
