#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: stress_strain_data.json ===
python3 /solution/generate_stress_strain.py

# === solve block: young_moduli.json ===
cat > /app/outputs/young_moduli.json <<'FFEOF'
{
  "2": 90.2,
  "3": 103.6,
  "4": 112.4,
  "6": 124.5
}
FFEOF
