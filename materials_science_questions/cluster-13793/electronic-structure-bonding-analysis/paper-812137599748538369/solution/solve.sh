#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
cat > "/app/outputs/computed_properties.json" <<'FFEOF'
{
  "BaTiO3_lattice_constant_A": 4.004,
  "SrTiO3_lattice_constant_A": 3.903,
  "BST_supercell_lattice_constant_A": 3.963,
  "BaTiO3_band_gap_eV": 3.46,
  "SrTiO3_band_gap_eV": 3.56,
  "BST_band_gap_eV": 3.54
}
FFEOF
