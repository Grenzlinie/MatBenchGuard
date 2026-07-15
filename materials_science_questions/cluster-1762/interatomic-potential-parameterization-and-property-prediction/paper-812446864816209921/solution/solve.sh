#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: solubility_limit.txt ===
cat > /app/outputs/solubility_limit.txt <<'FFEOF'
0.20
FFEOF

# === solve block: effective_valence.txt ===
cat > /app/outputs/effective_valence.txt <<'FFEOF'
0.86
FFEOF
