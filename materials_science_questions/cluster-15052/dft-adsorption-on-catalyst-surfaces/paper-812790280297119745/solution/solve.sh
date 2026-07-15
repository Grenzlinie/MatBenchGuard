#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.csv ===
cat > "$OUTDIR/adsorption_energies.csv" <<'EOF'
configuration,adsorption_energy_kcal_mol,hirshfeld_charge_transfer_e,bond_length_si_x_A
NO(N-site),-36.13,-0.14,1.77
NO(O-site),-7.52,-0.12,1.80
CO(C-site),-15.57,0.14,1.91
CO(O-site),-0.70,-0.01,3.00
EOF

# === solve block: dimer_dissociation_barrier.txt ===
cat > "$OUTDIR/dimer_dissociation_barrier.txt" <<'EOF'
10.58
EOF

# === solve block: o_removal_barrier.txt ===
cat > "$OUTDIR/o_removal_barrier.txt" <<'EOF'
6.68
EOF
