#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gap.json ===
cat > /app/outputs/band_gap.json <<'FFEOF'
{
  "direct_gap": 5.1,
  "method": "GGA-PBE",
  "code": "Quantum ESPRESSO",
  "cutoff_ry": 27.93
}
FFEOF

# === solve block: dos_analysis.json ===
cat > /app/outputs/dos_analysis.json <<'FFEOF'
{
  "homo_dominant_orbital": "O p",
  "lumo_dominant_orbital": "Si/Al s,p"
}
FFEOF
