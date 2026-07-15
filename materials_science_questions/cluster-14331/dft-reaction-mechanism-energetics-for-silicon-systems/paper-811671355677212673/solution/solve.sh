#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_data.json ===
cat > "$OUTDIR/computed_data.json" << 'JSONEOF'
{
  "pathway_A_relative_energy": 3.0,
  "pathway_B_relative_energy": 0.0,
  "syn_TS_barrier_H": 15.0,
  "anti_TS_barrier_H": 16.1,
  "syn_TS_barrier_G": 16.0,
  "anti_TS_barrier_G": 16.9,
  "DeltaDeltaH_dagger": 1.1,
  "DeltaDeltaG_dagger": 0.9,
  "predicted_ratio_from_H": "84:16",
  "predicted_ratio_from_G": "88:12",
  "pathway_preference": "B_favored"
}
JSONEOF
