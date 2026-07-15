#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'HEREDOC'
{
  "pristine_band_gap_eV": 3.46,
  "ovacancy_GS_to_CB_eV": 2.6,
  "Nidoped_band_gap_eV": 2.3
}
HEREDOC

# === solve finalize ===
true
