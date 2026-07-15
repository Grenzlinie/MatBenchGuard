#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_05_rate_constants.json ===
cat > "$OUTDIR/step_05_rate_constants.json" <<'JSONEOF'
[
  {
    "MOF": "MIL-53(Al)-BDC",
    "barrier_kJ_per_mol": 169,
    "reaction_energy_kJ_per_mol": 115,
    "rate_constant": -4.9e-9
  },
  {
    "MOF": "MIL-53(Al)-FA",
    "barrier_kJ_per_mol": 165,
    "reaction_energy_kJ_per_mol": 102,
    "rate_constant": -1.4e-9
  },
  {
    "MOF": "MIL-53(Al)-TDC",
    "barrier_kJ_per_mol": 126,
    "reaction_energy_kJ_per_mol": 103,
    "rate_constant": -1.1e-3
  }
]
JSONEOF
