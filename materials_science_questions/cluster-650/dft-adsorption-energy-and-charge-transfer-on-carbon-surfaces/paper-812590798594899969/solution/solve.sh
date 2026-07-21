#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: cbn_band_gap.json ===
cat > "$OUTDIR/cbn_band_gap.json" <<'CHEOF'
{
  "band_gap": 3.029,
  "unit": "eV"
}
CHEOF

# === solve block: single_adsorption_results.csv ===
cat > "$OUTDIR/single_adsorption_results.csv" <<'CHEOF'
E_ads,charge_transfer,gas
-0.47,0.06,SO2
-0.15,0.01,N2
-0.12,0.01,O2
-0.10,0.01,CO2
-0.38,0.04,H2O
-0.35,0.05,NO
-0.39,0.05,NO2
-0.08,0.01,CO
CHEOF

# === solve block: coadsorption_results.csv ===
cat > "$OUTDIR/coadsorption_results.csv" <<'CHEOF'
E_ads,charge_transfer,gas
-0.44,0.06,SO2
-0.15,0.02,H2O
CHEOF
