#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_tensors.json ===
cat > "$OUTDIR/computed_tensors.json" <<'JSONEOF'
{
  "vacancy_dipole": [
    [-2.52, 0.0, 0.0],
    [0.0, -2.52, 0.0],
    [0.0, 0.0, -2.52]
  ],
  "transition_dipole": [
    [-2.12, -0.19, 0.0],
    [-0.19, -2.12, 0.0],
    [0.0, 0.0, 1.89]
  ],
  "migration_volume_tensor": [
    [-5.89, -0.47, 0.0],
    [-0.47, -5.89, 0.0],
    [0.0, 0.0, 10.18]
  ]
}
JSONEOF
