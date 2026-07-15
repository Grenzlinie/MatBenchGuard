#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: intrinsic_bandgap.txt ===
echo "1.4144" > "$OUTDIR/intrinsic_bandgap.txt"

# === solve block: hybrid_bandgap.txt ===
echo "0.5618" > "$OUTDIR/hybrid_bandgap.txt"

# === solve finalize ===
echo "Oracle artifacts written."
