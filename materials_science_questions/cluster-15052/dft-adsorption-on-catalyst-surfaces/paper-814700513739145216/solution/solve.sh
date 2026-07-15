#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: activation_barriers.json ===
cat > /app/outputs/activation_barriers.json <<'EEOF'
{
  "L_H_high_valent": 0.59,
  "L_H_low_valent": 0.65,
  "E_R": 1.01,
  "second_CO2": 1.41
}
EEOF
