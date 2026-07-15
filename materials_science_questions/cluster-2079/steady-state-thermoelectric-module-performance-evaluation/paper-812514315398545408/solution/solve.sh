#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_coupling.json ===
cat > "$OUTDIR/step_01_coupling.json" <<'FFEOF'
{
  "V_CP": 29.3,
  "I_CP": 1.55,
  "T1_CP": 287.0,
  "T2_CP": 315.0,
  "eta": 0.139
}
FFEOF

# === solve block: step_02_optimal.json ===
cat > "$OUTDIR/step_02_optimal.json" <<'FFEOF'
{
  "eta_opt": 0.144,
  "beta_opt": 0.00121,
  "N_opt": 5,
  "V_opt": 28.1,
  "I_opt": 1.75
}
FFEOF

# === solve block: step_03_maximum.json ===
cat > "$OUTDIR/step_03_maximum.json" <<'FFEOF'
{
  "eta_max": 0.20,
  "G_eta": 18.1
}
FFEOF
