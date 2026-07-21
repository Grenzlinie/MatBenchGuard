#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'CSV'
binding_site,delta_E,delta_G_383
μ-OH,4.95,4.64
OH,16.9,16.2
HB,0.27,1.16
H2O,0,0
CSV

# === solve block: single_zn_geometry.txt ===
cat > "$OUTDIR/single_zn_geometry.txt" <<'TXT'
coordination_number=4
geometry=tetrahedral
avg_Zn_O_distance=1.97
TXT

# === solve block: four_zn_pathway.json ===
cat > "$OUTDIR/four_zn_pathway.json" <<'JSON'
{
  "one_per_face_unhydrated": -152.6,
  "two_per_face_unhydrated": -140.0,
  "one_per_face_hydrated": -192.8,
  "two_per_face_hydrated": -218.4,
  "preferred_structure": "one_per_face"
}
JSON
