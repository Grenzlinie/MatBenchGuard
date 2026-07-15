#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "fe_n_eps": 2.05,
  "fe_n_p": 2.03,
  "delta_e_hs_ls_fe2": 9.0,
  "delta_e_hs_ls_fe3": 7.0,
  "delta_e_q_fe2_singlet": 0.92,
  "delta_e_q_fe3_doublet": 2.78
}
FFEOF
