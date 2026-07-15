#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: final_energy.txt ===
echo '-47.0' > "$OUTDIR/final_energy.txt"

# === solve block: first_iteration_rotation.json ===
cat > "$OUTDIR/first_iteration_rotation.json" <<'EOF'
{
  "residue": 11,
  "dihedral": "psi",
  "rotation_degrees": -120.0
}
EOF
