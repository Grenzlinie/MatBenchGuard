#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap_dirac.json ===
cat > "$OUTDIR/band_gap_dirac.json" <<'FFEOF'
{
  "materials": {
    "alpha_graphyne": { "band_gap_ev": 0.0, "dirac_points": ["K", "K'"] },
    "beta_graphyne": { "band_gap_ev": 0.0, "dirac_points": ["Γ→M"] },
    "gamma_graphyne": { "band_gap_ev": 0.5, "dirac_points": [] },
    "6-6-12_graphyne": { "band_gap_ev": 0.0, "dirac_points": ["Γ→X", "M→X'"] },
    "graphene": { "band_gap_ev": 0.0, "dirac_points": ["K", "K'"] }
  }
}
FFEOF

# === solve block: ZT_gamma_graphyne.json ===
cat > "$OUTDIR/ZT_gamma_graphyne.json" <<'FFEOF'
{
  "max_ZT_300K": 0.45
}
FFEOF

# === solve finalize ===
echo "All scored artifacts written."
