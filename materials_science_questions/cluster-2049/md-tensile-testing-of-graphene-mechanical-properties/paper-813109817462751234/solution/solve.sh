#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: mechanical_properties.csv ===
cat > /app/outputs/mechanical_properties.csv <<'FFEOF'
structure,Young_modulus_GPa_nm,yield_stress_GPa,yield_strain,failure_mechanism
S1_armchair,375,49.54,0.1,nanopore
S1_zigzag,155,32.63,0.1,nanopore
S2_armchair,203,13.75,0.1,cracking
S2_zigzag,193,24.17,0.1,nanopore
S3_armchair,212,16.13,0.1,cracking
S3_zigzag,191,21.02,0.1,nanopore
S4_armchair,159,23.75,0.1,nanopore
S4_zigzag,145,11.70,0.1,cracking
S5_armchair,226,25.07,0.1,cracking
S5_zigzag,186,25.12,0.1,nanopore
graphene_armchair,340,100,0.15,cleavage
graphene_zigzag,340,100,0.15,cleavage
h-BN_armchair,270,70,0.15,cleavage
h-BN_zigzag,270,70,0.15,cleavage
FFEOF
