#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bulk_properties.json ===
cat > "$OUTDIR/bulk_properties.json" <<'EOF'
{
  "Si": {
    "a0_LDA": 10.17,
    "a0_NLDA": 10.19,
    "B0_LDA": 0.98,
    "B0_NLDA": 0.95,
    "Eb_LDA": 5.31,
    "Eb_NLDA": 5.28
  },
  "C": {
    "a0_LDA": 6.73,
    "a0_NLDA": 6.75,
    "B0_LDA": 4.51,
    "B0_NLDA": 3.93,
    "Eb_LDA": 8.63,
    "Eb_NLDA": 8.46
  },
  "SiC": {
    "a0_LDA": 8.15,
    "a0_NLDA": 8.16,
    "B0_LDA": 2.25,
    "B0_NLDA": 2.00,
    "Eb_LDA": 7.42,
    "Eb_NLDA": 7.35
  },
  "GaAs": {
    "a0_LDA": 10.55,
    "a0_NLDA": 10.60,
    "B0_LDA": 0.77,
    "B0_NLDA": 0.85,
    "Eb_LDA": 4.00,
    "Eb_NLDA": 4.01
  }
}
EOF

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'EOF'
{
  "Si": {
    "Gamma_LDA": 2.57,
    "Gamma_NLDA": 2.60,
    "X_LDA": 3.57,
    "X_NLDA": 3.63,
    "L_LDA": 2.86,
    "L_NLDA": 2.90
  },
  "C": {
    "Gamma_LDA": 5.62,
    "Gamma_NLDA": 5.70,
    "X_LDA": 11.21,
    "X_NLDA": 11.32,
    "L_LDA": 11.32,
    "L_NLDA": 11.39
  },
  "GaAs": {
    "Gamma_LDA": 0.39,
    "Gamma_NLDA": 0.38,
    "X_LDA": 3.99,
    "X_NLDA": 4.01,
    "L_LDA": 2.05,
    "L_NLDA": 2.06
  }
}
EOF
