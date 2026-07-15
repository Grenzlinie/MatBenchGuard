#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_properties.csv ===
cat > /app/outputs/transition_properties.csv <<'FFEOF'
composition,transition_pressure_GPa,volume_collapse_percent
ZnTe,10,8.1
ZnSe0.2Te0.8,11,8.5
ZnSe0.55Te0.45,12.2,7.8
ZnSe0.81Te0.19,12.8,8.4
ZnSe0.93Te0.07,13,8.3
ZnSe,13.8,7.6
FFEOF

# === solve block: elastic_constants_b3.csv ===
cat > /app/outputs/elastic_constants_b3.csv <<'FFEOF'
composition,bulk_modulus_BT_GPa,shear_modulus_C44_GPa,tetragonal_modulus_Cs_GPa
ZnTe,129.8,103.1,39.9
ZnSe0.2Te0.8,132,104,40.9
ZnSe0.55Te0.45,146.5,114.2,41.1
ZnSe0.81Te0.19,154.9,118.8,41.4
ZnSe0.93Te0.07,163.3,122.6,41.7
ZnSe,156.5,104.2,52.5
FFEOF
