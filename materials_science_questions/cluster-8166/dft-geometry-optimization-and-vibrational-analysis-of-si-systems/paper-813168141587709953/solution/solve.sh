#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: na_insertion_data.json ===
cat > /app/outputs/na_insertion_data.json <<'FFEOF'
{
  "bulk_Si_Na_Eb": 0.60,
  "polysilane_Na_Eb": -0.57,
  "silicene_Na_Eb": -0.32,
  "bulk_Si_Na_barrier": 1.06,
  "polysilane_Na_barrier": 0.41
}
FFEOF
