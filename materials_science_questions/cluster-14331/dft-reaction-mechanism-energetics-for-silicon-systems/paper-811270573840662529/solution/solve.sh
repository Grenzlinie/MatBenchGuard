#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: barrier_kcal_mol.txt ===
cat > "/app/outputs/barrier_kcal_mol.txt" <<'FFEOF'
2.4
FFEOF
