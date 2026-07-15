#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: summary.json ===
cat > /app/outputs/summary.json <<'FFEOF'
{
  "stress_concentration_factor": 6.0,
  "implied_strength_GPa": 20.0
}
FFEOF
