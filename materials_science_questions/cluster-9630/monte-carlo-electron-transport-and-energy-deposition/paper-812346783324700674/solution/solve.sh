#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: yields.json ===
cat > /app/outputs/yields.json <<'FFEOF'
{
  "ionization_yield_per_100eV": 4.11,
  "excitation_yield_per_100eV": 2.19
}
FFEOF
