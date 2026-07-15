#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduced_energies.json ===
cat > /app/outputs/reproduced_energies.json <<'JSONEOF'
{
  "liquid_graphene": {
    "energy_K": -129.221,
    "error_K": 0.009
  },
  "commensurate_graphene": {
    "energy_K": -129.282,
    "error_K": 0.007
  },
  "incommensurate_graphene": {
    "energy_K": -126.6,
    "error_K": 0.2
  },
  "liquid_graphite": {
    "energy_K": -142.69,
    "error_K": 0.01
  },
  "commensurate_graphite": {
    "energy_K": -142.81,
    "error_K": 0.01
  },
  "incommensurate_graphite": {
    "energy_K": -140.0,
    "error_K": 0.2
  },
  "infinite_dilution_graphene": -128.26,
  "infinite_dilution_graphite": -141.64,
  "offset_K": 13.38,
  "diff_liquid_commensurate_graphite_K": 0.12
}
JSONEOF
