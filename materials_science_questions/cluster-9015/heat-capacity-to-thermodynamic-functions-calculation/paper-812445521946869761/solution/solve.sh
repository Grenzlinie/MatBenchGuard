#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_thermodynamic_functions.json ===
python3 << 'PYEOF' > "$OUTDIR/step_01_thermodynamic_functions.json"
import json, math, sys

compounds = [
    {
        "compound": "Bi2Ca2O5",
        "T1": 40.0, "T2": 120.0,
        "A1": 0.5128, "B1": 0.0001985,
        "A2": 7.9552, "B2": 1.0059, "C2": -0.0018068, "D2": -19338.0,
        "A3": -65.770, "B3": 1.4232, "C3": -0.0018545, "D3": 331245.0,
        "A4": 226.096, "B4": 0.033374, "C4": -3.4323e6
    },
    {
        "compound": "Bi2CaO4",
        "T1": 40.0, "T2": 110.0,
        "A1": 0.5688, "B1": 0.0001635,
        "A2": 72.194, "B2": -0.3979, "C2": 0.0037418, "D2": -46474.0,
        "A3": -72.762, "B3": 1.3081, "C3": -0.0018997, "D3": 262860.0,
        "A4": 157.161, "B4": 0.03875, "C4": -1.5461e6
    },
    {
        "compound": "Bi6Ca4O13",
        "T1": 40.0, "T2": 110.0,
        "A1": 1.3319, "B1": 0.0003997,
        "A2": -64.872, "B2": 4.2301, "C2": -0.014084, "D2": 4703.0,
        "A3": -312.901, "B3": 4.6156, "C3": -0.0064634, "D3": 1367590.0,
        "A4": 550.808, "B4": 0.11489, "C4": -7.2005e6
    }
]

results = []
for c in compounds:
    T298 = 298.15
    # Cpm at 298.15 K via high-temperature polynomial Cpm,4
    cpm298 = c["A4"] + c["B4"]*T298 + c["C4"]/(T298**2)

    # Sm(298.15) by piecewise integration of Cpm/T from 0 K to 298.15 K
    T1 = c["T1"]
    T2 = c["T2"]

    # integral 1: ∫0→T1 (A1 + B1*T^2) dT
    int1 = c["A1"]*T1 + c["B1"]*(T1**3)/3.0

    # integral 2: ∫T1→T2 (A2/T + B2 + C2*T + D2/T^3) dT
    int2 = c["A2"] * math.log(T2/T1)
    int2 += c["B2"] * (T2 - T1)
    int2 += c["C2"] * (T2**2 - T1**2) / 2.0
    int2 += c["D2"] * (1.0/(2*T1**2) - 1.0/(2*T2**2))

    # integral 3: ∫T2→298.15 (A3/T + B3 + C3*T + D3/T^3) dT
    int3 = c["A3"] * math.log(T298/T2)
    int3 += c["B3"] * (T298 - T2)
    int3 += c["C3"] * (T298**2 - T2**2) / 2.0
    int3 += c["D3"] * (1.0/(2*T2**2) - 1.0/(2*T298**2))

    sm298 = int1 + int2 + int3

    results.append({
        "compound": c["compound"],
        "Cpm_298": cpm298,
        "Sm_298": sm298
    })

json.dump(results, sys.stdout, indent=2)
PYEOF
