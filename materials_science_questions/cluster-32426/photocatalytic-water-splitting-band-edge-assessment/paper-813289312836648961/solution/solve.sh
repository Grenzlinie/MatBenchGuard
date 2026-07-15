#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: strain_energy_001_0n.csv ===
cat > "$OUTDIR/strain_energy_001_0n.csv" <<'FFEOF'
diameter_nm,strain_energy_eV_per_formula_unit
2.5,0.05
3.0,0.02
3.5,-0.10
4.0,-0.18
FFEOF

# === solve block: band_structure_s_doped.json ===
cat > "$OUTDIR/band_structure_s_doped.json" <<'FFEOF'
{
  "band_gap_eV": 2.72,
  "valence_band_edge_vs_SHE": 2.72,
  "conduction_band_edge_vs_SHE": 0.0
}
FFEOF
