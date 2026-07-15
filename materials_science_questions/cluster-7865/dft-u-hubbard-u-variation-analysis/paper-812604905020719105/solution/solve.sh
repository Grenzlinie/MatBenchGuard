#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap.txt ===
echo "3.0" > "$OUTDIR/band_gap.txt"

# === solve block: orbital_character.json ===
cat > "$OUTDIR/orbital_character.json" <<'FFEOF'
{
  "highest_valence_band_orbital": "Cr d_{z^2} spin-up",
  "lowest_conduction_band_orbital": "Cr d_{x^2-y^2} spin-up",
  "paramagnetic_gap_consistent": true
}
FFEOF
