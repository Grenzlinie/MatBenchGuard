#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "power_reflection": 0.161,
  "beam_reflection": 0.29,
  "electron_penetration_depth_um": 2.1,
  "heat_penetration_depth_um": 1.4,
  "ratio_heat_to_electron": 0.6666666666666666
}
FFEOF
