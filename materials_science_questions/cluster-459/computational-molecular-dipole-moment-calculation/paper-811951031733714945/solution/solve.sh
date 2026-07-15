#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dipole_results.csv ===
cat > "$OUTDIR/dipole_results.csv" << 'CSVEOF'
system,conformation,solvent,total_energy,dipole_moment
SA,gauche,gas,-454.4457889,6.1544
SA,gauche,THF,-454.4534150,6.9407
SA,trans,gas,-454.4457889,6.1563
SA,trans,THF,-454.0295712,6.4588
MA,MA,gas,-453.2410527,6.0764
MA,MA,THF,-453.2167701,2.8543
CSVEOF
