#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: surface_state_energy.txt ===
cat > "$OUTDIR/surface_state_energy.txt" <<'FFEOF'
2.85
FFEOF

# === solve block: layer_dos_gamma.csv ===
python3 /solution/generate_dos.py "$OUTDIR/layer_dos_gamma.csv"
