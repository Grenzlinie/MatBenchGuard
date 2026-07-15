#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: molecular_calculations_results.csv ===
cat > "$OUTDIR/molecular_calculations_results.csv" <<'CSVEOF'
COSMO_excitation_eV,HOMO_LUMO_gap_eV,adiabatic_correction_eV,gas_phase_excitation_eV,molecule
3.38,2.58,0.53,3.71,I
2.41,1.55,failed,2.61,II
3.16,2.49,0.78,3.63,IIIa
2.23,1.45,failed,2.46,IIIb
3.05,2.40,0.73,3.47,IV
CSVEOF
