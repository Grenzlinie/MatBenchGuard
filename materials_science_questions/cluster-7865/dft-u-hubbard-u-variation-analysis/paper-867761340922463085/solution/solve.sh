#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_bulk_properties.json ===
cat > "$OUTDIR/step_01_bulk_properties.json" <<'EOF'
{
  "alpha-Ce": {
    "lattice_constant_angstrom": 4.808,
    "total_magnetic_moment_muB": 0.0
  },
  "gamma-Ce": {
    "lattice_constant_angstrom": 5.169,
    "total_magnetic_moment_muB": 1.142
  }
}
EOF

# === solve block: step_02_surface_moments.csv ===
cat > "$OUTDIR/step_02_surface_moments.csv" <<'EOF'
phase,layer,spin_moment_muB,orbital_moment_muB,total_moment_muB
alpha-Ce,1,0.98,-0.21,0.77
alpha-Ce,2,1.79,-0.45,1.34
alpha-Ce,3,0.96,-0.22,0.74
alpha-Ce,4,0.85,-0.23,0.63
alpha-Ce,5,1.03,-0.39,0.64
gamma-Ce,1,0.0,0.0,0.0
gamma-Ce,2,0.0,0.0,0.0
gamma-Ce,3,0.0,0.0,0.0
gamma-Ce,4,0.0,0.0,0.0
gamma-Ce,5,0.0,0.0,0.0
EOF
