#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_heats.json ===
cat > /app/outputs/formation_heats.json <<'FFEOF'
{
  "sub1": 1.45,
  "sub2": 1.54,
  "interstitial": 5.73,
  "two_sub_far": 2.90,
  "two_sub_near": 2.71,
  "interaction_energy": 0.19,
  "complex_1+1_per_Al": 1.50,
  "complex_2+1_per_Al": 0.75,
  "complex_3+1_per_Al": 0.315
}
FFEOF

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'FFEOF'
{
  "pure": 4.61,
  "complex_1+1": 2.10
}
FFEOF
