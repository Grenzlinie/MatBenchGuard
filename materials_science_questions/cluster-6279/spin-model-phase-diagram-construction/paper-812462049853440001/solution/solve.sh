#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "gamma0_beta_c": 4.0,
  "gamma0003_beta1": 3.5330,
  "gamma0003_beta2": 3.6475,
  "gamma_c": 0.0002
}
FFEOF
