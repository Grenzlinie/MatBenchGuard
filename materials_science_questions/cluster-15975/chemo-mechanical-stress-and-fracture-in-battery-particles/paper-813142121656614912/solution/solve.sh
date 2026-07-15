#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p $OUTDIR

# === solve block: stress_contributions.json ===
cat > $OUTDIR/stress_contributions.json <<'FFEOF'
{
  "planar_contribution_eV": 0.042,
  "perturbation_elastic_contribution_eV": 1.38
}
FFEOF
