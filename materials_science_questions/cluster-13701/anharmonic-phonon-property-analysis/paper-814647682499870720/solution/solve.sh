#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ir_phonon_frequencies.json ===
cat > /app/outputs/ir_phonon_frequencies.json <<'FFEOF'
{
  "A_u": 89.0,
  "1E_u": 219.0,
  "2E_u": 361.8
}
FFEOF
