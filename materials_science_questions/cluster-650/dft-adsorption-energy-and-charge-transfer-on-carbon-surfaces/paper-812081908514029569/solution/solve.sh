#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_melting_temperatures.json ===
cat > "$OUTDIR/step_01_melting_temperatures.json" <<'FFEOF'
{
  "MOM_melting_T": 116.0,
  "PRC1_melting_T": 122.0
}
FFEOF

# === solve block: step_02_min_energy_structure.json ===
cat > "$OUTDIR/step_02_min_energy_structure.json" <<'FFEOF'
{
  "MOM": {
    "a": 8.119,
    "b": 5.151,
    "alpha_cell": 50.6,
    "beta1": 84.3,
    "beta2": 17.0,
    "z": 3.178,
    "theta": 0.974,
    "energy_per_molecule": -3264
  },
  "PRC1": {
    "a": 8.240,
    "b": 5.826,
    "alpha_cell": 45.0,
    "beta1": 90.0,
    "beta2": 0.0,
    "z": 3.327,
    "theta": 0.927,
    "energy_per_molecule": -3170
  }
}
FFEOF
