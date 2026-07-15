#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'EOF'
compound,band_gap_direct,band_gap_type
Li,3.78,direct
Na,3.81,direct
K,3.88,direct
Rb,3.89,direct
Cs,3.85,direct
La1/3,3.17,direct
EOF

# === solve block: cbm_dominance.json ===
cat > "$OUTDIR/cbm_dominance.json" <<'EOF'
{
  "Li": "La5d(6h)",
  "Na": "La5d(6h)",
  "K": "La5d(4f)",
  "Rb": "La5d(4f)",
  "Cs": "La5d(4f)",
  "La1/3": "equal"
}
EOF
