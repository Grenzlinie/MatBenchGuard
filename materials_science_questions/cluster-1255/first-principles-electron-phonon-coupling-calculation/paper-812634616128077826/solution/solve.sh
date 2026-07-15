#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_thermodynamic_curves.csv ===
python3 <<'PYEOF'
import csv, math

Tmin, Tmax, dT = 0.0, 50.0, 0.5
Tm = 21.0
eps0 = 0.0029
chi_bkg = 1.8e-4
# jump at Tm (tetragonal -> cubic): 0.4e-4 emu/g
chi_tet = chi_bkg - 0.4e-4
# slope just above Tm: -0.032e-6 emu/g·K
slope = -0.032e-6
# cubic branch: linear continuation from chi_tet + jump at Tm with given slope
chi_cub_Tm = chi_tet + 0.4e-4
# specific heat: linear in T with jump
C_jump = 0.4
C_slope = 0.01

def epsilon(T):
    if T < Tm:
        return eps0 * math.sqrt(max(0.0, 1.0 - T/Tm))
    else:
        return 0.0

def chi(T):
    if T < Tm:
        return chi_tet
    else:
        return chi_cub_Tm + slope * (T - Tm)

def C(T):
    if T < Tm:
        return C_slope * T
    else:
        return (C_slope * Tm + C_jump) + C_slope * (T - Tm)

rows = []
T = Tmin
while T <= Tmax + 1e-9:
    rows.append([T, epsilon(T), chi(T), C(T)])
    T += dT

with open("/app/outputs/step_01_thermodynamic_curves.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T", "epsilon", "chi", "C"])
    w.writerows(rows)
PYEOF

# === solve block: step_02_derived_values.json ===
python3 <<'PYEOF'
import json

data = {
    "Tm": 21.0,
    "epsilon_0": 0.0029,
    "dchi_dT_at_Tm": 0.032,
    "Delta_Cv": 0.4
}
with open("/app/outputs/step_02_derived_values.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
