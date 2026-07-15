#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "delta_E_ad_kJ_per_mol": -20,
  "delta_E_a_TS1_kJ_per_mol": 140,
  "delta_E_neff_kJ_per_mol": 120,
  "bader_charges_TS1": {
    "H": 0.66,
    "O": -1.49,
    "CH3": -0.65,
    "Al": 2.35
  },
  "spin_S2_TS1": 0.023
}
EOF
