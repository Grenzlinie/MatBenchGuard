#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'FFEOF'
{
  "CH3NH3PbI3": 1.544,
  "CH3NH3PbBr3": 2.233,
  "CsPbCl3": 2.829,
  "CsPbBr3": 2.228,
  "RbPbI3": 3.302,
  "CsPbI3_ortho": 3.330,
  "CsPbI3_cubic": 1.072
}
FFEOF
