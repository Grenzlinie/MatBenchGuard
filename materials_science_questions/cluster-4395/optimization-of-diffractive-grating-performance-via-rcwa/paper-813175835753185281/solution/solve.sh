#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: enhancement_factor.json ===
cat > "$OUTDIR/enhancement_factor.json" <<'FFEOF'
{
  "wavelength_nm": 540,
  "enhancement_factor": 2.8
}
FFEOF

# === solve block: absorption_loss.json ===
cat > "$OUTDIR/absorption_loss.json" <<'FFEOF'
{
  "wavelength_nm": 540,
  "ungrated_loss": 93,
  "grated_loss": 77
}
FFEOF
