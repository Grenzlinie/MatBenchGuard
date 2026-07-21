#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relaxation_parameters.json ===
cat > "$OUTDIR/relaxation_parameters.json" <<'FFEOF'
{
  "delta1_perp": 0.775,
  "delta1_y": 4.593,
  "d12_y": 4.036,
  "d12_perp": 0.639,
  "delta2_perp": 0.065,
  "omega1": 17.7
}
FFEOF
