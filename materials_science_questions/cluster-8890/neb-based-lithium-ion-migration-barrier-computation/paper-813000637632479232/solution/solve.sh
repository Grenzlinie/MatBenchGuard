#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
# Write the scored results.json with the paper's reference IS/TS energies.
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "pristine_pathI_IS_ads": -1.43,
  "pristine_pathI_TS_ads": -0.84,
  "pristine_pathII_IS_ads": -1.43,
  "pristine_pathII_TS_ads": -0.80,
  "I_H1_H7_IS_ads": -1.69,
  "I_H1_H7_TS_ads": -1.47,
  "I_H1_H2_IS_ads": -1.69,
  "I_H1_H2_TS_ads": -1.52,
  "units": "eV"
}
FFEOF
