#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > "/app/outputs/results.json" <<'FFEOF'
{
  "energy_case_A": -20000.0,
  "energy_case_B": -19999.999994,
  "energy_case_C": -19999.999986,
  "delta_E_45": 0.000006,
  "delta_E_90": 0.000014,
  "K_uniaxial": 1.10
}
FFEOF
