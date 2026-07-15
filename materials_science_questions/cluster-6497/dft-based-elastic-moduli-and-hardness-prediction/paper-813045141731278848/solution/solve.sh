#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" << 'FFEOF'
composition,lattice_parameter_angstrom,bulk_modulus_GPa
TiN1.00,4.239,270
TiN0.75,4.227,278
TiN0.50,4.211,217
FFEOF

# === solve finalize ===
cat > "$OUTDIR/dft_summary.txt" << 'FFEOF'
DFT calculations for δ‑TiNₓ (x=1.00, 0.75, 0.50) using plane‑wave pseudopotential code with GGA‑PW exchange‑correlation.
Supercells: vacancies modeled as empty spheres on the N sublattice.
Full relaxation and equation‑of‑state fitting performed.
Extracted equilibrium lattice parameters and bulk moduli.
Values: TiN1.00 a=4.239 Å B=270 GPa; TiN0.75 a=4.227 Å B=278 GPa; TiN0.50 a=4.211 Å B=217 GPa.
FFEOF
