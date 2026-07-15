#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: gamma_frequencies.json ===
cat > /app/outputs/gamma_frequencies.json <<'FFEOF'
{
  "A1g_1": 178.1,
  "A1g_2": 192.4,
  "Eg_1": 116.8,
  "Eg_2": 175.2
}
FFEOF

# === solve block: minimum_phonon_frequency.json ===
cat > /app/outputs/minimum_phonon_frequency.json <<'FFEOF'
{
  "min_frequency_cm-1": -50.0,
  "q_point": [0.5, 0.0, 0.0],
  "q_label": "Sigma"
}
FFEOF
