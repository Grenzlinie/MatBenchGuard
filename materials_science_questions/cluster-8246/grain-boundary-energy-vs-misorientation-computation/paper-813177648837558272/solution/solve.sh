#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: grain_boundary_energies.csv ===
cat > "$OUTDIR/grain_boundary_energies.csv" <<'EOF'
Boundary,Energy_J_m2
Σ=11{113},1.78
Σ=3{111},2.12
Σ=9{221},3.01
EOF

# === solve block: coordination_deficient_site_densities.csv ===
cat > "$OUTDIR/coordination_deficient_site_densities.csv" <<'EOF'
Boundary,Density_per_nm2
Σ=11{113},2.0
Σ=3{111},3.5
Σ=9{221},6.0
EOF
