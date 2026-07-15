#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_properties.json ===
cat > $OUTDIR/phonon_properties.json <<'FFEOF'
{
  "C11_GPa": 481.8,
  "C12_GPa": 221.9,
  "C44_GPa": 205.6,
  "Bulk_modulus_GPa": 308.5,
  "X_longitudinal_THz": 7.25,
  "X_transverse_THz": 5.80
}
FFEOF

# === solve block: anomaly_data.csv ===
python3 /solution/gen_anomaly.py /app/outputs/anomaly_data.csv
