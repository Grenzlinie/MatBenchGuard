#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "delta_ass_G_AI_kJ_per_mol": 212.7,
  "delta_ass_G_AII_kJ_per_mol": -184.1,
  "delta_ass_G_AIII_kJ_per_mol": 28.6,
  "delta_ass_g_G_kJ_per_mol": -486.7
}
FFEOF
