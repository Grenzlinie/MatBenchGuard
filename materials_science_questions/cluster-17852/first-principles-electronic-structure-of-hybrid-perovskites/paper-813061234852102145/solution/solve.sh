#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies.json ===
cat > /app/outputs/binding_energies.json <<'FFEOF'
{
  "MAI/R": -0.1419,
  "MAI/A": -0.1467,
  "SnI2/R": -0.1646,
  "SnI2/A": -0.1789
}
FFEOF

# === solve block: potential_drops.json ===
cat > /app/outputs/potential_drops.json <<'FFEOF'
{
  "MAI/R": 0.12,
  "MAI/A": 0.14,
  "SnI2/R": 0.28,
  "SnI2/A": 0.45
}
FFEOF
