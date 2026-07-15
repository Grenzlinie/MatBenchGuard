#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_diagram_results.json ===
# ---- Write phase_diagram_results.json ----
cat > /app/outputs/phase_diagram_results.json <<'FFEOF'
{
  "eutectic_temperature_K": 1669.15,
  "eutectic_composition_mol_percent_SrO": 37.2,
  "solubility_SrO_in_NiO_mol_percent": 0.04
}
FFEOF
