#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 << 'PYEOF'
import json, math

mu_B_eV = 5.7883818060e-05
k_B_eV = 8.617333262e-05
g = 6.1
S = 0.5
Bc1 = 3.27
Bc2 = 5.35
Bc3 = 13.44
TN = 31.9
Q = 11.0/14.0

factor = g * mu_B_eV / S

J1 = (1.0/168.0) * (-31*Bc1 + 22*Bc2 - 33*Bc3) * factor
J2 = (1.0/336.0) * (67*Bc1 - 34*Bc2 - 33*Bc3) * factor
J3 = (1.0/6.0) * (Bc1 - Bc2) * factor

J1_kB = J1 / k_B_eV
J2_kB = J2 / k_B_eV
J3_kB = J3 / k_B_eV

JQ_kB = 2.0 * TN
J0_kB = JQ_kB - (2*J1_kB*math.cos(math.pi*Q) + 2*J2_kB*math.cos(2*math.pi*Q) + 2*J3_kB*math.cos(3*math.pi*Q))

dBC1 = 0.935
dBC2 = 1.027
dBC3 = 0.60
dTN = 0.94

dJ1_dP = (1.0/168.0) * (-31*dBC1 + 22*dBC2 - 33*dBC3) * factor
dJ2_dP = (1.0/336.0) * (67*dBC1 - 34*dBC2 - 33*dBC3) * factor
dJ3_dP = (1.0/6.0) * (dBC1 - dBC2) * factor

dJ1_kB_dP = dJ1_dP / k_B_eV
dJ2_kB_dP = dJ2_dP / k_B_eV
dJ3_kB_dP = dJ3_dP / k_B_eV

dJQ_kB_dP = 2.0 * dTN

dJ0_kB_dP = dJQ_kB_dP - (2*math.cos(math.pi*Q)*dJ1_kB_dP + 2*math.cos(2*math.pi*Q)*dJ2_kB_dP + 2*math.cos(3*math.pi*Q)*dJ3_kB_dP)

dlnJ0 = (dJ0_kB_dP / J0_kB) * 100.0
dlnJ1 = (dJ1_kB_dP / J1_kB) * 100.0
dlnJ2 = (dJ2_kB_dP / J2_kB) * 100.0
dlnJ3 = (dJ3_kB_dP / J3_kB) * 100.0

ambient = {
    "J0_kB": J0_kB,
    "J1_kB": J1_kB,
    "J2_kB": J2_kB,
    "J3_kB": J3_kB
}
pressure = {
    "dlnJ0_dP": dlnJ0,
    "dlnJ1_dP": dlnJ1,
    "dlnJ2_dP": dlnJ2,
    "dlnJ3_dP": dlnJ3
}

with open("/tmp/ambient.json", "w") as f:
    json.dump(ambient, f)
with open("/tmp/pressure.json", "w") as f:
    json.dump(pressure, f)
PYEOF

# === solve block: ambient_J_values.json ===
cat /tmp/ambient.json > /app/outputs/ambient_J_values.json

# === solve block: pressure_derivatives.json ===
cat /tmp/pressure.json > /app/outputs/pressure_derivatives.json
