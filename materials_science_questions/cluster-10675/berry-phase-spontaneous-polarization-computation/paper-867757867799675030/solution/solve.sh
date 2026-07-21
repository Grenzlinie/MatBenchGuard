#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'JSONEOF'
{
  "HT_formation_energy_mJ_m2": 4.4,
  "HH_formation_energy_mJ_m2": -1.2,
  "HT_thickness_nm": 1.0,
  "HH_thickness_nm": 1.0,
  "HT_peak_polarization_muC_cm2": 1.8,
  "HH_peak_polarization_muC_cm2": 6.0
}
JSONEOF
