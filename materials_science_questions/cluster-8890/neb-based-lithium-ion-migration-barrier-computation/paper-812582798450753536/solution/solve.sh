#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: migration_barrier.json ===
cat > "$OUTDIR/migration_barrier.json" <<'EOF'
{
  "ground_state_energy": -3169.06,
  "transition_state_energy": -3140.11,
  "barrier_kJmol": 28.95,
  "barrier_eV": 0.30
}
EOF
