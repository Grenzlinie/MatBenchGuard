#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_frequencies_16GPa.json ===
cat > /app/outputs/phonon_frequencies_16GPa.json <<'FFEOF'
{
  "minimum_frequency": -100.0
}
FFEOF

# === solve block: force_on_K_16GPa.json ===
cat > /app/outputs/force_on_K_16GPa.json <<'FFEOF'
{
  "force": 0.05
}
FFEOF
