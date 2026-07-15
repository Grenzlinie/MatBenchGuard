#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_results.csv ===
cat > "$OUTDIR/dft_results.csv" <<'FFEOF'
complex,functional,basis,binding_energy_kcal_mol,K_O_distance_angstrom
K+:DME,SVWN,aug-cc-pVDZ,-20.2,2.47
K+:DME,BP86,aug-cc-pVDZ,-18.0,2.58
K+:DME,BLYP,aug-cc-pVDZ,-16.4,2.64
K+:12c4,SVWN,cc-pVDZ,-49.6,2.79
K+:12c4,BP86,cc-pVDZ,-47.3,2.86
K+:12c4,BLYP,cc-pVDZ,-42.5,2.90
K+:18c6,SVWN,cc-pVDZ,-80.0,2.84
K+:18c6,BP86,cc-pVDZ,-78.5,2.91
K+:18c6,BLYP,cc-pVDZ,-73.5,2.95
FFEOF
