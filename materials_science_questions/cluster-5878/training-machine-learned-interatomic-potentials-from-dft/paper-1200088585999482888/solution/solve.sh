#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: test_predictions.csv ===
python3 /solution/generate_test_predictions.py > "$OUTDIR/test_predictions.csv"

# === solve block: method_clusters.csv ===
cat > "$OUTDIR/method_clusters.csv" <<'FFEOF'
method,cluster_label
HF/aug-cc-pVDZ/CP,0
MP2/aug-cc-pVQZ/CP,1
SAPT0/jun-cc-pVDZ,2
B3LYP/aug-cc-pVTZ/CP,3
B2PLYP-D3/aug-cc-pVTZ/CP,3
FFEOF
