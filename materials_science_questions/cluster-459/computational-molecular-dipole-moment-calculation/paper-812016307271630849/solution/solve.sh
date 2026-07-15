#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: df_results.json ===
cat > "$OUTDIR/df_results.json" <<'FFEOF'
{
  "VEA_OAA": 0.20,
  "VEA_CA": -1.52,
  "Gibbs_M_H_OAA": 0.19,
  "Gibbs_M_H_CA": 0.17,
  "Gibbs_M_HCOOH_OAA": -0.73,
  "Gibbs_M_HCOOH_CA": -0.80
}
FFEOF
