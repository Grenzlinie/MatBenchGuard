#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: rel_enthalpy.json ===
cat > "$OUTDIR/rel_enthalpy.json" <<'ENDJSON'
{
  "P": 100,
  "H_rel_bcc": 0.07
}
ENDJSON

# === solve block: phonon_dispersion.json ===
python3 /solution/generate_phonon.py > "$OUTDIR/phonon_dispersion.json"

# === solve block: pnma_elastic_constants.json ===
cat > "$OUTDIR/pnma_elastic_constants.json" <<'ENDJSON'
{
  "pressure": 100,
  "C11": 834.6,
  "C22": 865.1,
  "C33": 875.3,
  "C44": 196.9,
  "C55": 150.1,
  "C66": 224.8,
  "C12": 351.0,
  "C13": 276.3,
  "C23": 292.0,
  "unit": "GPa"
}
ENDJSON

# === solve block: pnma_sound_velocity.json ===
cat > "$OUTDIR/pnma_sound_velocity.json" <<'ENDJSON'
{
  "pressure": 100,
  "C_l": 4.2,
  "C_b": 7.3,
  "unit": "km/s"
}
ENDJSON

# === solve block: omega_elastic_constants.json ===
cat > "$OUTDIR/omega_elastic_constants.json" <<'ENDJSON'
[
  {
    "pressure": 80,
    "C11": 900,
    "C12": 600,
    "C13": 500,
    "C33": 1100,
    "C44": -60
  },
  {
    "pressure": 100,
    "C11": 1000,
    "C12": 650,
    "C13": 550,
    "C33": 1200,
    "C44": -80
  },
  {
    "pressure": 120,
    "C11": 1100,
    "C12": 700,
    "C13": 600,
    "C33": 1300,
    "C44": -100
  }
]
ENDJSON
