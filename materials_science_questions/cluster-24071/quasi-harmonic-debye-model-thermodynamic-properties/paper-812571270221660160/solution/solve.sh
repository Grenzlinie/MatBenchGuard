#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_pressures_volume_drops.csv ===
cat > "/app/outputs/transition_pressures_volume_drops.csv" <<'FFEOF'
compound,temperature_K,transition_pressure_GPa,volume_drop_percent
LaS,0,28.05,9.28
LaS,300,27.25,9.55
PrS,0,22.90,9.08
PrS,300,22.00,9.33
FFEOF

# === solve block: elastic_properties.csv ===
cat > "/app/outputs/elastic_properties.csv" <<'FFEOF'
compound,property,temperature_K,value
LaS,C11,0,218
LaS,C12,0,24
LaS,C44,0,50
LaS,Y,0,214
LaS,BT,0,89
LaS,G,0,66
LaS,CS,0,97
LaS,CL,0,172
LaS,A,0,0.52
LaS,zeta,0,0.26
LaS,sigma,0,0.09
LaS,nu_l,0,5366
LaS,nu_t,0,3277
LaS,nu_m,0,3619
LaS,dBT_dP,0,5.08
LaS,dCS_dP,0,6.34
LaS,dC44_dP,0,0.29
LaS,C12_minus_C44,0,-26
LaS,BT_over_G,0,1.35
LaS,s1,0,320
LaS,s2,0,0.52
LaS,s3,0,0.29
LaS,F12,0,0.11
LaS,F44,0,0.23
LaS,C11,300,215
LaS,C12,300,23
LaS,C44,300,49
LaS,Y,300,210
LaS,BT,300,87
LaS,G,300,65
LaS,CS,300,95
LaS,CL,300,169
LaS,A,300,0.51
LaS,zeta,300,0.26
LaS,sigma,300,0.09
LaS,nu_l,300,5314
LaS,nu_t,300,3240
LaS,nu_m,300,3587
LaS,dBT_dP,300,5.21
LaS,dCS_dP,300,6.53
LaS,dC44_dP,300,0.28
LaS,C12_minus_C44,300,-26
LaS,BT_over_G,300,1.33
LaS,s1,300,315
LaS,s2,300,0.52
LaS,s3,300,0.29
LaS,F12,300,0.10
LaS,F44,300,0.23
PrS,C11,0,238
PrS,C12,0,41
PrS,C44,0,49
PrS,Y,0,226
PrS,BT,0,107
PrS,G,0,65
PrS,CS,0,98
PrS,CL,0,188
PrS,A,0,0.50
PrS,zeta,0,0.32
PrS,sigma,0,0.14
PrS,nu_l,0,6196
PrS,nu_t,0,3592
PrS,nu_m,0,3986
PrS,dBT_dP,0,6.74
PrS,dCS_dP,0,8.62
PrS,dC44_dP,0,0.11
PrS,C12_minus_C44,0,-8
PrS,BT_over_G,0,1.64
PrS,s1,0,335
PrS,s2,0,0.56
PrS,s3,0,0.29
PrS,F12,0,0.17
PrS,F44,0,0.20
PrS,C11,300,233
PrS,C12,300,39
PrS,C44,300,48
PrS,Y,300,222
PrS,BT,300,105
PrS,G,300,64
PrS,CS,300,97
PrS,CL,300,184
PrS,A,300,0.50
PrS,zeta,300,0.32
PrS,sigma,300,0.14
PrS,nu_l,300,6129
PrS,nu_t,300,3567
PrS,nu_m,300,3958
PrS,dBT_dP,300,6.95
PrS,dCS_dP,300,8.94
PrS,dC44_dP,300,0.12
PrS,C12_minus_C44,300,-9
PrS,BT_over_G,300,1.62
PrS,s1,300,329
PrS,s2,300,0.56
PrS,s3,300,0.30
PrS,F12,300,0.17
PrS,F44,300,0.20
FFEOF
