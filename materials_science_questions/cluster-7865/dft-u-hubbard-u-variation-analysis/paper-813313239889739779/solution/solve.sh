#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_data.csv ===
cat > /app/outputs/magnetic_data.csv <<'EOF'
Delta_E_eV,MM_V1_emu,MM_V2_emu,MM_supercell_emu,configuration
0.255,2.14,2.14,4.0,I
EOF

# === solve block: optical_spectra.csv ===
python3 /solution/generate_optical.py
