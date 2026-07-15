#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_symmetry.json ===
cat > /app/outputs/phonon_symmetry.json <<'FFEOF'
{
  "infrared_active_count": 5,
  "irreducible_representation": "2A+2E+5T"
}
FFEOF
