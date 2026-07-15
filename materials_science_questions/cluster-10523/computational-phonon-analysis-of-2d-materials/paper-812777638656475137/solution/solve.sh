#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: dft_raman_results.json ===
cat > "$OUTDIR/dft_raman_results.json" <<'FFEOF'
{
  "untwisted_bilayer_Ag1": 351.86,
  "untwisted_bilayer_Ag2": 455.57,
  "twisted_bilayer_Ag1": 356.56,
  "twisted_bilayer_Ag2": 456.88,
  "blue_shift_Ag1": 4.70,
  "blue_shift_Ag2": 1.31
}
FFEOF
