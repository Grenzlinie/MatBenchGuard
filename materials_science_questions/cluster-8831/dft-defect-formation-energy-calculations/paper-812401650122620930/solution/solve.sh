#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bega_bond_lengths.json ===
cat > "$OUTDIR/bega_bond_lengths.json" <<'EOF'
{
  "basis": ["Ga3d", "nlcc", "nlcc"],
  "charge": [0, 0, -1],
  "N-Be_a": [1.797, 1.811, 1.805],
  "Be-N_b": [1.775, 1.781, 1.802],
  "N-Ga_c": [1.929, 1.951, 1.943],
  "Ga-N_d": [1.933, 1.955, 1.954]
}
EOF

# === solve block: bega_formation_energies.json ===
cat > "$OUTDIR/bega_formation_energies.json" <<'EOF'
{
  "Ga_rich_Ef0": 2.45,
  "N_rich_Ef0": 2.03
}
EOF

# === solve block: bega_lvm.json ===
cat > "$OUTDIR/bega_lvm.json" <<'EOF'
{
  "basis": "nlcc",
  "charge": 0,
  "frequencies": [445, 562, 593, 663]
}
EOF

# === solve block: bebe_ga_lvm.json ===
cat > "$OUTDIR/bebe_ga_lvm.json" <<'EOF'
{
  "charge": 0,
  "frequencies": [1041, 789, 738]
}
EOF
