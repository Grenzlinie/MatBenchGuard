#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_05_binding_energies.csv ===
cat > /app/outputs/step_05_binding_energies.csv <<'FFEOF'
surface,method,binding_energy_kJmol,Co_O_bond_A,O_O_lattice_bond_A
100-A,PBE+U,282,1.64,
100-A,HSE06,276,1.64,
100-B,PBE+U,260,1.84,1.39
100-B,HSE06,264,1.84,1.39
110-A,PBE+U,401,1.88,
110-A,HSE06,402,1.88,
FFEOF
