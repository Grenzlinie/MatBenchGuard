#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dG_results.json ===
cat > /app/outputs/dG_results.json <<'FFEOF'
{
  "Pt_100_dG": -0.54,
  "Pt_110_dG": -0.46,
  "Pt3Sn_100_dG": -0.48,
  "Pt3Sn_110_dG": -0.15,
  "ordering": ["Pt3Sn(110)", "Pt(110)", "Pt3Sn(100)", "Pt(100)"]
}
FFEOF
