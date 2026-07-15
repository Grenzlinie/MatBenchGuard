#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ma_energies.csv ===
cat > "$OUTDIR/ma_energies.csv" <<'EOF'
configuration,MA_energy_meV_per_unit_area
FFFFFF/,1.34
CCCCCC/,-0.54
CCCCFF/,0.9
EOF

# === solve block: efield_modification.csv ===
cat > "$OUTDIR/efield_modification.csv" <<'EOF'
configuration,eta_MA_meV_per_V_per_Angstrom
CCCCFF/,0.5
EOF
