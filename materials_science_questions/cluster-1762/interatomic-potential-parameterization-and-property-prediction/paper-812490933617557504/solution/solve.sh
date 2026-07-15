#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: madelung_energies.csv ===
cat > /app/outputs/madelung_energies.csv <<'FFEOF'
compound,structure_type,lattice_param_A,Madelung_energy_eV
BaCeO3,simple,4.377,-162.88
BaPrO3,simple,4.360,-163.52
BaZrO3,simple,4.193,-170.03
BaTiO3,simple,4.031,-176.86
ABO3,simple,4.304,-165.64
ABO3,simple,4.162,-171.29
BaEr1/2Nb1/2O3,mixed_ordered,4.304,-166.94
BaEr1/2Nb1/2O3,mixed_disordered,4.304,-166.31
BaEr1/2Ta1/2O3,mixed_ordered,4.302,-166.99
BaEr1/2Ta1/2O3,mixed_disordered,4.302,-166.36
BaGd1/2Nb1/2O3,mixed_ordered,4.342,-165.47
BaGd1/2Nb1/2O3,mixed_disordered,4.342,-164.83
BaGd1/2Ta1/2O3,mixed_ordered,4.339,-165.59
BaGd1/2Ta1/2O3,mixed_disordered,4.339,-164.99
BaLa1/2Nb1/2O3,mixed_ordered,4.395,-163.48
BaLa1/2Nb1/2O3,mixed_disordered,4.395,-162.87
BaLa1/2Ta1/2O3,mixed_ordered,4.340,-165.53
BaLa1/2Ta1/2O3,mixed_disordered,4.340,-164.92
BaYb1/2Nb1/2O3,mixed_ordered,4.286,-167.64
BaYb1/2Nb1/2O3,mixed_disordered,4.286,-167.03
BaYb1/2Ta1/2O3,mixed_ordered,4.337,-165.67
BaYb1/2Ta1/2O3,mixed_disordered,4.337,-165.05
BaCa1/2Mo1/2O3,mixed_ordered,4.162,-176.63
BaCa1/2Mo1/2O3,mixed_disordered,4.162,-174.9
BaCa1/2Te1/2O3,mixed_ordered,4.186,-175.62
BaCa1/2Te1/2O3,mixed_disordered,4.186,-173.8
BaCa1/3Nb2/3O3,mixed_disordered,4.210,-171.31
FFEOF
