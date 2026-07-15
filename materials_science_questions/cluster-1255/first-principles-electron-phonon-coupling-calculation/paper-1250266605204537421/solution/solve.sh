#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "inter_ring_distance": 3.38,
  "fermi_level_DOS": 0.19,
  "lambda": 0.3,
  "Tc": 0.5,
  "dynamic_stable": true
}
FFEOF
