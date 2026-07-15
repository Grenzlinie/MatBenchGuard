#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
# The oracle is self-contained; no external installs needed.

# === solve block: relative_energies.csv ===
cat > /app/outputs/relative_energies.csv << 'EOF'
complex,functional,relative_energy_kcal_mol
1,B3LYP,0.0
2,B3LYP,4.98
3,B3LYP,10.03
4,B3LYP,0.0
4',B3LYP,0.0
5,B3LYP,6.06
5',B3LYP,14.57
6,B3LYP,13.89
6',B3LYP,24.45
7,B3LYP,0.0
7',B3LYP,0.0
8,B3LYP,7.37
8',B3LYP,4.13
9,B3LYP,15.49
9',B3LYP,7.73
EOF

# === solve block: deltae_hs_ls.csv ===
cat > /app/outputs/deltae_hs_ls.csv << 'EOF'
complex,functional,deltae_hs_ls_kcal_mol
1,B3LYP,1.0
2,B3LYP,1.0
3,B3LYP,1.0
4,B3LYP,-1.0
4',B3LYP,-1.0
5,B3LYP,-1.0
5',B3LYP,-1.0
6,B3LYP,-1.0
6',B3LYP,1.0
7,B3LYP,-1.0
7',B3LYP,1.0
8,B3LYP,-1.0
8',B3LYP,1.0
9,B3LYP,-1.0
9',B3LYP,1.0
EOF

# === solve block: harmonic_frequencies.csv ===
python3 /solution/make_outputs.py harmonic_frequencies

# === solve block: geometry_bond_lengths.csv ===
python3 /solution/make_outputs.py geometry_bond_lengths

# === solve block: absorption_spectra.csv ===
python3 /solution/make_outputs.py absorption_spectra

# === solve finalize ===
# No additional steps needed.
