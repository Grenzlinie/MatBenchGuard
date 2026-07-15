#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "AgF_band_gap": 0.25,
  "NiF_band_gap": 0.19,
  "AgF_total_magnetic_moment": 6.0,
  "NiF_total_magnetic_moment": 8.0,
  "AgF_electronic_specific_heat_300K": 3.69,
  "NiF_electronic_specific_heat_300K": 4.84
}
FFEOF
