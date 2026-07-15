#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimized_structures.json ===
cat > "$OUTDIR/optimized_structures.json" << 'EOF'
{
  "M585": {
    "space_group": "P21/M (No.11)",
    "lattice_a": 14.64,
    "lattice_b": 3.814,
    "lattice_c": 6.772,
    "mass_density": 2.311,
    "relative_energy": 25
  },
  "S": {
    "space_group": "CMCM (No.63)",
    "lattice_a": 3.825,
    "lattice_b": 17.41,
    "lattice_c": 7.399,
    "mass_density": 2.307,
    "relative_energy": 42
  },
  "Z-CACB": {
    "space_group": "IMMA (No.74)",
    "lattice_a": 3.833,
    "lattice_b": 7.289,
    "lattice_c": 17.41,
    "mass_density": 2.302,
    "relative_energy": 70
  },
  "H": {
    "space_group": "PBAM (No.55)",
    "lattice_a": 11.832,
    "lattice_b": 7.234,
    "lattice_c": 3.812,
    "mass_density": 2.284,
    "relative_energy": 61
  },
  "Z-ACA": {
    "space_group": "PMMN (No.59)",
    "lattice_a": 3.807,
    "lattice_b": 7.055,
    "lattice_c": 12.002,
    "mass_density": 2.315,
    "relative_energy": 78
  }
}
EOF

# === solve block: phonon_stability.json ===
cat > "$OUTDIR/phonon_stability.json" << 'EOF'
{
  "M585": { "stable": true },
  "S": { "stable": true },
  "Z-CACB": { "stable": true },
  "H": { "stable": true },
  "Z-ACA": { "stable": true }
}
EOF

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" << 'EOF'
{
  "M585": {
    "indirect_band_gap": 1.51,
    "direct_band_gap": 1.51
  },
  "S": {
    "indirect_band_gap": 1.41,
    "direct_band_gap": 1.53
  },
  "Z-CACB": {
    "indirect_band_gap": 1.33,
    "direct_band_gap": 1.38
  },
  "H": {
    "indirect_band_gap": 1.52,
    "direct_band_gap": 1.63
  },
  "Z-ACA": {
    "indirect_band_gap": 1.29,
    "direct_band_gap": 1.43
  }
}
EOF
