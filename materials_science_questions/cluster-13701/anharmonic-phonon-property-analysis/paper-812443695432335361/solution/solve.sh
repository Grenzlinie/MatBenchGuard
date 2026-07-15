#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: computed_energies.csv ===
cat > "$OUTDIR/computed_energies.csv" <<'EOF'
state_label,energy_MeV
2+,0.5585
2'+,1.23
2''+,1.86
0'+,0.92
0''+,2.14
4+,1.09
4'+,1.91
EOF

# === solve block: electromagnetic_observables.csv ===
cat > "$OUTDIR/electromagnetic_observables.csv" <<'EOF'
observable,value
B(E2,2'→0)/B(E2,2→0),0.016
B(E2,2'→2)/B(E2,2→0),0.96
B(E2,0'→2)/B(E2,2→0),1.13
Q22/Q20,0.63
EOF
