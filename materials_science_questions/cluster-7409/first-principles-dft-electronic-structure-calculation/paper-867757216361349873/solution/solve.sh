#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_rotation_angle.txt ===
cat > /app/outputs/step_01_rotation_angle.txt <<'FFEOF'
6.3
FFEOF

# === solve block: step_02_formation_energy_diff.txt ===
cat > /app/outputs/step_02_formation_energy_diff.txt <<'FFEOF'
0.075
FFEOF
