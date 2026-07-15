#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: Seebeck_vs_T.csv ===
cat > /app/outputs/Seebeck_vs_T.csv <<'FFEOF'
Seebeck_uV_K,compound,doping_level,temperature_K
55.0,Na_xCoO2,h=0.5,100.0
110.0,Na_xCoO2,h=0.5,200.0
165.0,Na_xCoO2,h=0.5,300.0
220.0,Na_xCoO2,h=0.5,400.0
48.0,Na_xCoO2,h=0.6,100.0
96.0,Na_xCoO2,h=0.6,200.0
144.0,Na_xCoO2,h=0.6,300.0
192.0,Na_xCoO2,h=0.6,400.0
40.0,Na_xCoO2,h=0.7,100.0
80.0,Na_xCoO2,h=0.7,200.0
120.0,Na_xCoO2,h=0.7,300.0
160.0,Na_xCoO2,h=0.7,400.0
33.0,Na_xCoO2,h=0.8,100.0
66.0,Na_xCoO2,h=0.8,200.0
99.0,Na_xCoO2,h=0.8,300.0
132.0,Na_xCoO2,h=0.8,400.0
60.0,ZnRh2O4,p=0.5,100.0
120.0,ZnRh2O4,p=0.5,200.0
180.0,ZnRh2O4,p=0.5,300.0
240.0,ZnRh2O4,p=0.5,400.0
45.0,ZnRh2O4,p=1.0,100.0
90.0,ZnRh2O4,p=1.0,200.0
135.0,ZnRh2O4,p=1.0,300.0
180.0,ZnRh2O4,p=1.0,400.0
30.0,ZnRh2O4,p=2.0,100.0
60.0,ZnRh2O4,p=2.0,200.0
90.0,ZnRh2O4,p=2.0,300.0
120.0,ZnRh2O4,p=2.0,400.0
FFEOF
