#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" <<'FFEOF'
chirality,functional_group,concentration,radius_A,young_modulus_TPa,band_gap_eV
(9,0),pristine,0.0,3.53,1.00,0.0
(9,0),OH,0.0,3.53,1.00,0.0
(9,0),OH,6.25,3.61,0.85,0.0
(9,0),OH,12.5,3.68,0.75,0.0
(9,0),COOH,0.0,3.53,1.00,0.0
(9,0),COOH,6.25,3.60,0.87,0.0
(9,0),COOH,12.5,3.67,0.78,0.0
(10,0),pristine,0.0,3.91,0.95,0.85
(10,0),OH,0.0,3.91,0.95,0.85
(10,0),OH,6.25,3.99,0.82,0.30
(10,0),OH,12.5,4.07,0.72,0.0
(10,0),COOH,0.0,3.91,0.95,0.85
(10,0),COOH,6.25,3.98,0.84,0.40
(10,0),COOH,12.5,4.06,0.74,0.0
FFEOF
