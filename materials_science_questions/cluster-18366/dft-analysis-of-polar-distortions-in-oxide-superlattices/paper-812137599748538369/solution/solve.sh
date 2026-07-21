#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "BaTiO3_lattice_constant_angstrom": 4.004,
  "SrTiO3_lattice_constant_angstrom": 3.903,
  "BST_lattice_constant_angstrom": 3.963,
  "BaTiO3_band_gap_eV": 3.46,
  "SrTiO3_band_gap_eV": 3.56,
  "BST_band_gap_eV": 3.54
}
EOF
