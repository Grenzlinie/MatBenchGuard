#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_energies.json ===
cat > "$OUTDIR/step_01_formation_energies.json" <<'FFEOF'
{
  "B2_MoAl": -5.934,
  "D03_Mo3Al": -9.1045,
  "B32_MoAl": -29.6044,
  "D03_MoAl3": 0.6236
}
FFEOF

# === solve block: step_02_interaction_parameters.json ===
cat > "$OUTDIR/step_02_interaction_parameters.json" <<'FFEOF'
{
  "w1": -178.42,
  "w2": -492.10,
  "wtilde_MoAlMoAl": -287.89,
  "wtilde_MoAlAlAl": 195.0
}
FFEOF
