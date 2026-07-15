#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relative_energies.csv ===
cat > /app/outputs/relative_energies.csv <<'EOF'
structure,energy_rel_alpha_Si
SA,27.3
SB,21.9
SC,14.0
SD,13.7
EOF
