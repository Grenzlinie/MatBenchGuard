#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: monolayer_spin_splitting.json ===
cat > /app/outputs/monolayer_spin_splitting.json <<'FFEOF'
{
  "delta_soc_mev": 129,
  "band_gap_indirect_ev": 1.775
}
FFEOF

# === solve block: bilayer_ez_splitting.csv ===
cat > /app/outputs/bilayer_ez_splitting.csv <<'FFEOF'
Ez,Delta_intra,Delta_inter
0,129,0
0.005,129,53.75
0.01,129,107.5
0.012,129,129.0
0.015,129,161.25
0.02,129,215.0
0.025,129,268.75
0.03,129,322.5
FFEOF
