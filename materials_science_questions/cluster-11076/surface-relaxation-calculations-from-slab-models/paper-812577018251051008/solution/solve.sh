#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_properties.json ===
OUTDIR=${OUTDIR:-/app/outputs}
cat > "$OUTDIR/bulk_properties.json" << 'EOF'
{
  "equilibrium_lattice_constant_A": 6.657,
  "bulk_band_gap_majority_eV": 0.28,
  "total_magnetic_moment_mu_B": 2.00,
  "atomic_magnetic_moments": {
    "Zr1": -0.25,
    "Zr2": 0.13,
    "V": 1.82,
    "Ga": -0.01
  }
}
EOF

# === solve block: surface_results.json ===
python3 /solution/write_artifacts.py surface
