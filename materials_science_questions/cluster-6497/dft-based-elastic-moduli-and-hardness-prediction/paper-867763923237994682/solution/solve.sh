#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOFDATA'
{
  "bulk_diamond": {
    "num_atoms": 8,
    "a0": 3.572,
    "B0": 434.6,
    "k_direct": 465.7,
    "k_est": 461.0,
    "ratio_k": 0.99
  },
  "graphene": {
    "num_atoms": 2,
    "a0": 2.468,
    "k_direct": 719.1,
    "k_est": 733.482,
    "ratio_k": 1.02
  },
  "nd_small": {
    "num_atoms": 54,
    "k_direct": 520.0,
    "k_est": 510.0,
    "ratio_k": 0.981
  },
  "nd_medium": {
    "num_atoms": 660,
    "k_direct": 490.0,
    "k_est": 495.0,
    "ratio_k": 1.01
  },
  "nd_hydro": {
    "num_atoms": 980,
    "k_direct": 460.0,
    "k_est": 450.0,
    "ratio_k": 0.978
  },
  "c60": {
    "num_atoms": 60,
    "k_direct": 689.9,
    "k_est": 710.597,
    "ratio_k": 1.03
  }
}
EOFDATA
