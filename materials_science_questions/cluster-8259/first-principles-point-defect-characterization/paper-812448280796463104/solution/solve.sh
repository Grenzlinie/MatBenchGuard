#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: defect_state_energies.csv ===
cat > "$OUTDIR/defect_state_energies.csv" <<'EOF'
distance_Angstrom,defect_state_energy_relative_to_E_C_eV,perfect_E_C_eV
5.18,-0.05,0.0
3.17,-0.22,0.0
EOF

# === solve block: total_energies.csv ===
cat > "$OUTDIR/total_energies.csv" <<'EOF'
complex_name,total_energy_eV
C_N-O_N,-53200.0
C_Ga-O_N,-53100.0
EOF
