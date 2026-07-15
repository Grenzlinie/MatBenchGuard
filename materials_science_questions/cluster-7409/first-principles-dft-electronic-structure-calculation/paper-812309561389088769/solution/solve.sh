#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_gaps.json ===
cat > $OUTDIR/energy_gaps.json <<'FFEOF'
{
  "no_substitution": 0.5,
  "upper_Zr": 0.9,
  "lower_Zr": 1.2,
  "both": 1.5,
  "ordering": "no_substitution < upper_Zr < lower_Zr < both"
}
FFEOF
