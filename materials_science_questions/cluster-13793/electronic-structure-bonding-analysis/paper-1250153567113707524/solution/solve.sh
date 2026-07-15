#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'EOFJSON'
{
  "Pt4": {"ethane_barrier": 0.29},
  "Pt4C2": {"ethane_barrier": 0.64, "Pt_charge_sum": -0.10},
  "Pt4GeC2": {"ethane_barrier": 0.53, "Pt_charge_sum": -0.50}
}
EOFJSON
