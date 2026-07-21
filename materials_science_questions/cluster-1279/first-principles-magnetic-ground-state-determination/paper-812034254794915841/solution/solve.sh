#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "Fe_magnetic_energy_mRy": 0.001,
  "Fe_magnetic_moment_mub": 0.04,
  "Mn_magnetic_energy_mRy": 5.319,
  "Mn_magnetic_moment_mub": 1.84
}
FFEOF
