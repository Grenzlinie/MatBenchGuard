#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_constants.json ===
cat > /app/outputs/lattice_constants.json <<'EOF'
{
  "BaTiO3": 4.004,
  "SrTiO3": 3.903
}
EOF

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'EOF'
{
  "BaTiO3": 3.46,
  "SrTiO3": 3.56,
  "BST": 3.54
}
EOF

# === solve block: partial_dos_BST.csv ===
python3 /solution/generate_pdos.py > /app/outputs/partial_dos_BST.csv
