#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.csv ===
cat > /app/outputs/computed_properties.csv <<'FFEOF'
compound,source,chi1_el,chi1,epsilon_inf,epsilon_0,theta,chi14_el,chi14,r41_el,r41,p11,p12,p44,B,d_epsilon_inf_dP,d_epsilon_0_dP,prod_d_epsilon_inf_dP_B,prod_d_epsilon_0_dP_B
SiC,Mann,0.43,0.48,6.46,7.00,0.11,1.86,0.14,-0.55,-0.04,-0.25,-0.08,-0.13,166,-1.74,-2.43,-2.89,-4.03
SiC,Herman-Skillman,0.46,0.49,6.81,7.13,0.06,1.60,0.07,-0.40,-0.02,-0.26,-0.08,-0.13,177,-1.93,-2.49,-3.41,-4.41
GeC,Mann,0.44,0.51,6.57,7.39,0.15,2.54,0.25,-0.74,-0.07,-0.22,-0.07,-0.11,124,-2.19,-3.46,-2.71,-4.29
GeC,Herman-Skillman,0.49,0.53,7.11,7.63,0.08,2.12,0.10,-0.53,-0.02,-0.24,-0.08,-0.12,137,-2.55,-3.19,-3.48,-4.37
SnC,Mann,0.42,0.58,6.28,8.29,0.39,4.59,1.10,-1.46,-0.35,-0.14,-0.04,-0.07,64,-2.13,-7.13,-1.36,-4.56
SnC,Herman-Skillman,0.48,0.57,7.00,8.18,0.19,4.08,0.50,-1.05,-0.13,-0.19,-0.06,-0.10,72,-3.75,-6.71,-2.70,-4.83
FFEOF
