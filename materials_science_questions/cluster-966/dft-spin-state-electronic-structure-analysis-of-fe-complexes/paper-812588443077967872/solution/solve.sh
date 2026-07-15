#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: activation_energies_and_bond_orders.csv ===
cat > "$OUTDIR/activation_energies_and_bond_orders.csv" <<'EOF'
system,activation_energy_kJ_per_mol,c5n_bond_order
C(N),349.87,1.14438
Fe@H1,357.89,1.24941
Fe@H2,354.97,1.223759
Fe@H3,402.91,1.272091
Fe@H4,363.83,1.256351
Fe@H5,353.50,1.179537
Fe@H6,356.27,1.238715
Fe@H7,140.36,0.951271
EOF
