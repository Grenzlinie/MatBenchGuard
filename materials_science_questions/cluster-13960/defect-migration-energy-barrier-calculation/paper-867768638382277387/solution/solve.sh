#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_formation_energy.txt ===
cat > "$OUTDIR/step_01_formation_energy.txt" <<'FFEOF'
E_form = 3.1 eV
FFEOF

# === solve block: step_02_migration_barrier.txt ===
cat > "$OUTDIR/step_02_migration_barrier.txt" <<'FFEOF'
E_barrier_hop = 0.40 eV
FFEOF

# === solve block: step_03_reorientation_barrier.txt ===
cat > "$OUTDIR/step_03_reorientation_barrier.txt" <<'FFEOF'
E_barrier_reorient = 0.20 eV
FFEOF
