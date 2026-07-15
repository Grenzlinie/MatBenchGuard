#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_strains.json ===
cat > /app/outputs/critical_strains.json <<'FFEOF'
{
  "epsilon_c0": 2.97e-3,
  "epsilon_c0_s": 3.17e-3,
  "epsilon_c1": 3.68e-3,
  "epsilon_c2": 1.11e-2
}
FFEOF
