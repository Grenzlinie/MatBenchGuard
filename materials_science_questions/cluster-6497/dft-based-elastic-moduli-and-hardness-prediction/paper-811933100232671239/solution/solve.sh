#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step01_eos_properties.json ===
cat > "$OUTDIR/step01_eos_properties.json" << 'FFEOF'
{
  "a_angstrom": 4.138,
  "V0_angstrom3_per_fu": 70.855,
  "E_coh_eV": 29.527,
  "B_GPa": 154.9,
  "B_prime": 4.216
}
FFEOF

# === solve block: step02_elastic_moduli.json ===
cat > "$OUTDIR/step02_elastic_moduli.json" << 'FFEOF'
{
  "c11_GPa": 322.9,
  "c12_GPa": 70.7,
  "c44_GPa": 62.5,
  "B_el_GPa": 154.8,
  "G_GPa": 87.9,
  "E_GPa": 221.8
}
FFEOF

# === solve block: step03_band_gap.json ===
cat > "$OUTDIR/step03_band_gap.json" << 'FFEOF'
{
  "band_gap_eV": 3.30,
  "band_gap_type": "indirect"
}
FFEOF
