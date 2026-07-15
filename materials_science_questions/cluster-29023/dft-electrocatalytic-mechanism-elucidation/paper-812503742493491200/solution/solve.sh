#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reproduced_results.json ===
cat > "$OUTDIR/reproduced_results.json" <<'FFEOF'
{
  "CO_sink_Gr": 0.85,
  "CO_sink_N_Gr": 3.33,
  "CO_sink_S_N_Gr": 0.68,
  "Pt1Cu2_adsorption_energy_S_N_CNT": -4.17,
  "Pt1Cu2_adsorption_energy_S_N_Gr": -6.81,
  "highest_barrier_Gr": 1.04,
  "highest_barrier_N_Gr": 1.60,
  "highest_barrier_S_N_Gr": 0.96,
  "overall_delta_G_Gr": -0.80,
  "overall_delta_G_N_Gr": -3.31,
  "overall_delta_G_S_N_Gr": -6.72
}
FFEOF
