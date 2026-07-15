#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: edge_energies.csv ===
cat > /app/outputs/edge_energies.csv <<'FFEOF'
Crystal,kappa
NaF,4.91
NaCl,2.85
NaBr,2.40
NaI,1.87
KF,3.27
KCl,2.11
KBr,1.84
KI,1.49
FFEOF
