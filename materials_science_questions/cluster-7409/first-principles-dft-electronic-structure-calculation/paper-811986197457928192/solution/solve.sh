#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR="/app/outputs"

# === solve block: o_vacancy_magnetic_moments.csv ===
cat > "$OUTDIR/o_vacancy_magnetic_moments.csv" <<'EOF'
system,total_magnetic_moment_muB,energy_difference_sp_vs_nonsp_eV
SrTiO2.875,1.30,-0.10
EOF

# === solve block: ti_vacancy_magnetic_moment.csv ===
cat > "$OUTDIR/ti_vacancy_magnetic_moment.csv" <<'EOF'
system,total_magnetic_moment_muB
SrTi0.875O3,3.54
EOF

# === solve block: sr_vacancy_magnetic_moment.csv ===
cat > "$OUTDIR/sr_vacancy_magnetic_moment.csv" <<'EOF'
system,total_magnetic_moment_muB
Sr0.875TiO3,0.05
EOF
