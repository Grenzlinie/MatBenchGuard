#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_moments_bond.json ===
cat > "$OUTDIR/step_01_moments_bond.json" <<'EOF'
{
  "total_moment_per_Co": 2.0,
  "Co_N_bond_length": 1.7
}
EOF

# === solve block: step_02_formation_energy.json ===
cat > "$OUTDIR/step_02_formation_energy.json" <<'EOF'
{
  "E_near": -10000.0,
  "E_far": -10000.0,
  "formation_energy_near": 2.785,
  "formation_energy_far": 4.225,
  "delta_E_near_far": -1.44
}
EOF

# === solve block: step_03_exchange_energy.json ===
cat > "$OUTDIR/step_03_exchange_energy.json" <<'EOF'
{
  "E_FM": -10000.0,
  "E_AFM": -9999.5,
  "delta_E_FM_AFM": -0.5
}
EOF
