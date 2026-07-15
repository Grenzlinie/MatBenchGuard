#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR='/app/outputs'
mkdir -p "$OUTDIR"

# === solve block: reproduced_results.json ===
cat > "$OUTDIR/reproduced_results.json" <<'JSONEOF'
{
  "E_diff_kJ_per_mol": -34.5,
  "HOMO_LUMO_gap_eV": 1.66,
  "Sn_I_dist_pm": 333.9,
  "Fe_I_dist_pm": 267.9,
  "I_I_sep1_pm": 367.6,
  "I_I_sep2_pm": 383.9,
  "I_Fe_I_angle_deg": 91.3
}
JSONEOF
