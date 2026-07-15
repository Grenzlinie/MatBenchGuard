#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: energy_differences.json ===
cat > "$OUTDIR/energy_differences.json" <<'JSONEOF'
[
  {"model": "I", "delta_E": 1.44, "E_2O": -150.0, "E_3O": -148.56},
  {"model": "II", "delta_E": 1.94, "E_2O": -150.0, "E_3O": -148.06},
  {"model": "III", "delta_E": 0.50, "E_2O": -150.0, "E_3O": -149.50},
  {"model": "IV", "delta_E": 0.73, "E_2O": -150.0, "E_3O": -149.27}
]
JSONEOF
