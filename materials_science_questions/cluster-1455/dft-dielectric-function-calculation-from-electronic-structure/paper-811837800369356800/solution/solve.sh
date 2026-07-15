#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: structural_properties.json ===
cat > "$OUTDIR/structural_properties.json" << 'FFEOF'
{
  "a0": 7.9285,
  "u": 0.2541,
  "B0_EOS": 283.9,
  "Bprime_EOS": 3.81
}
FFEOF

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" << 'FFEOF'
{
  "C11": 494.0,
  "C12": 172.0,
  "C44": 288.0
}
FFEOF

# === solve block: electronic_properties.json ===
cat > "$OUTDIR/electronic_properties.json" << 'FFEOF'
{
  "direct_band_gap_Gamma_Gamma": 2.14
}
FFEOF

# === solve block: optical_properties.json ===
cat > "$OUTDIR/optical_properties.json" << 'FFEOF'
{
  "static_dielectric_constant_epsilon0": 5.84,
  "static_refractive_index_n0": 2.42
}
FFEOF

# === solve block: thermal_properties_300K.json ===
cat > "$OUTDIR/thermal_properties_300K.json" << 'FFEOF'
{
  "bulk_modulus_300K": 272.0,
  "heat_capacity_300K": 99.0,
  "debye_temperature_300K": 1079.0
}
FFEOF
