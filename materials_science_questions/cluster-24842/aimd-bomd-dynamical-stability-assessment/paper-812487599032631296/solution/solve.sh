#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: stability_assessment.json ===
cat > "/app/outputs/stability_assessment.json" <<'FFEOF'
{
  "G4": {
    "max_charge_transfer": 0.1,
    "bond_cleavage_observed": false
  },
  "CaCB11H12": {
    "max_charge_transfer": 0.0,
    "bond_cleavage_observed": false
  },
  "CaPF6": {
    "max_charge_transfer": 8.0,
    "bond_cleavage_observed": true
  }
}
FFEOF
