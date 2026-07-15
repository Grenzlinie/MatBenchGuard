#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: exchange_energies.csv ===
cat > "$OUTDIR/exchange_energies.csv" <<'EOF'
element,delta_E_eV
Sc,-1.55
Ti,-1.38
V,-1.21
Cr,-1.04
Mn,-0.89
Fe,-0.80
Co,-0.66
Ni,-0.52
Cu,-0.37
Zn,-0.25
Co_paramagnetic,-1.0
EOF

# === solve block: interaction_energies.csv ===
cat > "$OUTDIR/interaction_energies.csv" <<'EOF'
element,position,interaction_energy_eV
Sc,surface_adatom,0.06
Ti,surface_adatom,0.05
V,surface_adatom,0.04
Cr,surface_adatom,0.03
Mn,surface_adatom,0.03
Fe,surface_adatom,-0.01
Co,surface_adatom,-0.03
Ni,surface_adatom,0.02
Cu,surface_adatom,0.03
Zn,surface_adatom,0.04
Sc,surface_layer,0.12
Ti,surface_layer,0.10
V,surface_layer,0.08
Cr,surface_layer,0.07
Mn,surface_layer,0.06
Fe,surface_layer,0.05
Co,surface_layer,0.04
Ni,surface_layer,0.05
Cu,surface_layer,0.07
Zn,surface_layer,0.09
EOF
