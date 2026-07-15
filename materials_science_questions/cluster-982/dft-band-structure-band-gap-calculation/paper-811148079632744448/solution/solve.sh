#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'FFEOF'
{
  "indirect_gap_eV": 2.52,
  "direct_gap_eV": 2.64
}
FFEOF

# === solve block: band_edge_character.json ===
cat > "$OUTDIR/band_edge_character.json" <<'FFEOF'
{
  "vbm_character": "Bi 6s + Br 4p",
  "cbm_character": "Bi p"
}
FFEOF
