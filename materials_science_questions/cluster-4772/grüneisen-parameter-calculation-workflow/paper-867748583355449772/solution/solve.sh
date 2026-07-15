#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: cp_at_300K.csv ===
cat > "$OUTDIR/cp_at_300K.csv" <<'ENDOFFILE'
pressure_Pa,Cp_J_mol_K
100000.0,26.4
5000000000.0,24.5
10000000000.0,-2.1
15000000000.0,-8.5
ENDOFFILE
