#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: yield_strength_estimate.json ===
cat > "$OUTDIR/yield_strength_estimate.json" <<'FFEOF'
{
  "nominal_yield_strength_GPa": 1.55,
  "computed_average_stress_factor": 1.16
}
FFEOF
