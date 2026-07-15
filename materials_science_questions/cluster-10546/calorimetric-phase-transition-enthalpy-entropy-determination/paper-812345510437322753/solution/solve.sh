#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_properties.json ===
cat > /app/outputs/transition_properties.json <<'FFEOF'
{
  "T_trs_K": 233.0,
  "delta_H_J_per_mol": 414.0,
  "delta_S_J_per_K_per_mol": 1.82
}
FFEOF
