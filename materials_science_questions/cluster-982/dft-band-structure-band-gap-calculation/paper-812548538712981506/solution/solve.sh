#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "uni_-2": {
    "Bader_charge": -0.140,
    "interlayer_distance": 3.206,
    "Re_center": -4.298,
    "Ox_center": -7.283,
    "PDS_ph0": 0.585,
    "EDF_ph0": 1.553,
    "PDS_ph7": 0.172,
    "EDF_ph7": 1.966,
    "m_e/m0": 0.132,
    "m_h/m0": 0.590,
    "band_type": "Z-scheme",
    "feasible_ph0": true,
    "feasible_ph7": true
  },
  "uni_-4": {
    "Bader_charge": -0.140,
    "interlayer_distance": 3.192,
    "Re_center": -4.574,
    "Ox_center": -7.144,
    "PDS_ph0": 0.639,
    "EDF_ph0": 1.414,
    "PDS_ph7": 0.226,
    "EDF_ph7": 1.827,
    "m_e/m0": 0.183,
    "m_h/m0": 0.770,
    "band_type": "Z-scheme",
    "feasible_ph0": true,
    "feasible_ph7": true
  },
  "bi_-2": {
    "Bader_charge": -0.136,
    "interlayer_distance": 3.191,
    "Re_center": -3.615,
    "Ox_center": -7.288,
    "PDS_ph0": 0.610,
    "EDF_ph0": 1.558,
    "PDS_ph7": 0.197,
    "EDF_ph7": 1.971,
    "m_e/m0": 0.354,
    "m_h/m0": 0.314,
    "band_type": "Z-scheme",
    "feasible_ph0": true,
    "feasible_ph7": true
  },
  "bi_-6": {
    "Bader_charge": -0.124,
    "interlayer_distance": 3.248,
    "Re_center": -4.899,
    "Ox_center": -5.816,
    "PDS_ph0": 0.527,
    "EDF_ph0": 0.086,
    "PDS_ph7": 0.114,
    "EDF_ph7": 0.499,
    "m_e/m0": 0.162,
    "m_h/m0": 0.970,
    "band_type": "type-II",
    "feasible_ph0": false,
    "feasible_ph7": true
  },
  "bi_-8": {
    "Bader_charge": -0.121,
    "interlayer_distance": 3.225,
    "Re_center": -5.216,
    "Ox_center": -5.923,
    "PDS_ph0": 0.607,
    "EDF_ph0": 0.193,
    "PDS_ph7": 0.194,
    "EDF_ph7": 0.606,
    "m_e/m0": 0.150,
    "m_h/m0": 0.177,
    "band_type": "type-II",
    "feasible_ph0": false,
    "feasible_ph7": true
  }
}
FFEOF
