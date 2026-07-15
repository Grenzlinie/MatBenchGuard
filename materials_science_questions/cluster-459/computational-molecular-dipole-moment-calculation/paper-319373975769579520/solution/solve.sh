#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_complex_dipoles.csv ===
cat > "$OUTDIR/step_01_complex_dipoles.csv" <<'FFEOF'
complex,dipole_moment_D
C6H5SnCl3·2CH3OH,6.36
C6H5SnCl3·2C2H5OH,6.47
C6H5SnCl3·2C4H8O,6.29
FFEOF
