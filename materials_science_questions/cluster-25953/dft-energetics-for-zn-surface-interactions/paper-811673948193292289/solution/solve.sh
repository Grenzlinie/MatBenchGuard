#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: h2o_adsorption_energies.csv ===
cat > "$OUTDIR/h2o_adsorption_energies.csv" << 'CSVEOF'
model,site_label,delta_E_ads_kcal_mol
AL-ZnONC,1,-11.05
NLL-ZnONC,1,-10.08
NLL-ZnONC,2,-11.45
NLL-ZnONC,3,-13.78
PRL-ZnONC,1,-12.69
PRL-ZnONC,2,-14.11
PRL-ZnONC,3,-13.96
PRL-ZnONC,4,-10.83
PRL-ZnONC,5,-12.41
PRL-ZnONC,6,-9.21
CNL-ZnONS,1,-12.79
CNL-ZnONS,2,-12.48
CNL-ZnONS,3,-10.10
CNL-ZnONS,4,-9.86
CNL-ZnONS,5,-11.46
CNL-ZnONS,6,-10.15
CCL-ZnONS,1,-14.08
CCL-ZnONS,2,-13.93
CCL-ZnONS,3,-10.33
CCL-ZnONS,4,-10.41
CCL-ZnONS,5,-10.68
CCL-ZnONS,6,-10.96
CCL-ZnONS,7,-12.51
CCL-ZnONS,8,-10.86
CCL-ZnONS,9,-10.31
CCL-ZnONS,10,-9.43
CCL-ZnONS,11,-9.05
CSVEOF

# === solve block: nh3_adsorption_energies.csv ===
cat > "$OUTDIR/nh3_adsorption_energies.csv" << 'CSVEOF'
model,site_label,delta_E_ads_kcal_mol
AL-ZnONC,1,-10.84
NLL-ZnONC,1,-9.26
NLL-ZnONC,2,-10.92
NLL-ZnONC,3,-13.65
PRL-ZnONC,1,-12.23
PRL-ZnONC,2,-12.19
PRL-ZnONC,3,-14.11
PRL-ZnONC,4,-9.08
PRL-ZnONC,5,-10.52
PRL-ZnONC,6,-8.39
CNL-ZnONS,1,-13.21
CNL-ZnONS,2,-9.14
CNL-ZnONS,3,-10.43
CCL-ZnONS,1,-14.08
CCL-ZnONS,2,-11.01
CCL-ZnONS,3,-9.37
CCL-ZnONS,4,-9.15
CCL-ZnONS,5,-9.22
CCL-ZnONS,6,-7.60
CSVEOF
