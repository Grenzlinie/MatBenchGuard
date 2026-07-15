#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_delta_e.json ===
cat > "$OUTDIR/dft_delta_e.json" <<'FFEOF'
{
  "Li2V0.5Fe0.5O2F": 147.0,
  "Li2V0.5Ti0.5O2F": 144.0,
  "Li2VO2F": 179.0
}
FFEOF
