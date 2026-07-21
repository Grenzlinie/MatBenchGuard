#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structure_results.json ===
cat > /app/outputs/structure_results.json <<'FFEOF'
{
  "DT_alpha": 14.5,
  "ODT_alpha": 18.5,
  "DT_gauche_pct": 0.9,
  "ODT_gauche_pct": 1.0,
  "beta_DT": 50.0,
  "beta_ODT": 51.0
}
FFEOF
