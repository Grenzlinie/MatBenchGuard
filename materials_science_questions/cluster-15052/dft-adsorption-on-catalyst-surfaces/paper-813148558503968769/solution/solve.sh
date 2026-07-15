#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.csv ===
cat > /app/outputs/adsorption_energies.csv <<'CSVEOF'
defect_label,E_ads_BnSH_kJmol,Bader_charge_e,E_ads_Pd13_kJmol
1,-332.55,-0.415,-119.26
2,-62.37,0.001,-181.13
3,-78.38,0.027,-279.97
4,-87.98,0.048,-322.24
5,-64.81,0.021,-149.21
6,-95.54,-0.023,-294.05
7,-64.81,-0.021,-171.41
8,-105.36,-0.141,-150.28
9,-78.59,-0.017,-224.83
10,-77.21,-0.023,-172.50
11,-45.47,0.030,-161.03
CSVEOF
