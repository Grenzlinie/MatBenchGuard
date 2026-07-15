#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: quadrupole_transition_results.json ===
cat > "$OUTDIR/quadrupole_transition_results.json" <<'FFEOF'
{
  "T_star_K": 11.5,
  "discontinuity_ratio": 0.5
}
FFEOF

# === solve block: spin_only_ordering_temperature.json ===
cat > "$OUTDIR/spin_only_ordering_temperature.json" <<'FFEOF'
{
  "T_N_bilinear_K": 5.0
}
FFEOF
