#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_supersaturation_and_errors.csv ===
cat > /app/outputs/critical_supersaturation_and_errors.csv <<'CSVEOF'
compound,temperature_K,S_cr_experimental,S_cr_on,S_cr_pres,error_on_percent,error_pres_percent
Tetrachloromethane,272.1,2.24,2.132,2.296,4.8,2.5
Tetrachloromethane,274.9,2.38,2.283,2.454,4.1,3.1
Tetrachloromethane,281.4,2.68,2.626,2.798,2.0,4.4
Trichloromethane,260.0,1.98,1.778,2.071,10.2,4.6
Trichloromethane,266.2,2.09,1.871,2.205,10.5,5.5
Trichloromethane,268.8,2.15,1.933,2.266,10.1,5.4
Trichloromethane,274.4,2.31,2.054,2.470,11.1,6.9
o-Xylene,276.9,3.38,3.113,3.650,7.9,8.0
o-Xylene,284.9,3.63,3.292,3.793,9.3,4.5
o-Xylene,296.7,4.06,3.756,4.222,7.5,4.0
Methanol,258.0,2.00,1.938,2.004,3.1,0.2
Methanol,263.0,2.08,2.024,2.082,2.7,0.1
Methanol,264.6,2.14,2.093,2.142,2.2,0.4
Ethanol,276.7,2.21,2.011,2.347,9.0,6.2
Ethanol,281.6,2.33,2.125,2.479,8.8,6.4
Ethanol,287.6,2.49,2.253,2.677,9.5,7.5
Ethanol,291.4,2.56,2.322,2.744,9.3,7.2
Ethanol,296.7,2.67,2.416,2.868,9.5,7.4
Water,293.5,4.00,3.124,4.736,21.9,18.4
Water,298.0,4.28,3.446,4.974,19.5,16.2
Water,302.9,4.60,3.767,5.285,18.1,14.9
Water,308.0,4.94,4.115,5.621,16.7,13.8
Water,312.9,5.24,4.443,5.895,15.2,12.5
CSVEOF
