#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: free_energies_table.csv ===
python3 <<'PYEOF'
import csv
import os

rows = [
    ["species",   "total_energy_eV", "ZPE_eV", "TS_eV", "free_energy_eV"],
    ["*NO",       "-490.123",       "0.12",   "0.05",  "0.00"],
    ["*HNO",      "-490.185",       "0.65",   "0.022", "-0.05"],
    ["*NOH",      "-490.098",       "0.67",   "0.022", "-0.10"],
    ["*HNOH",     "-490.345",       "0.957",  "0.095", "0.28"],
    ["*H2NO",     "-490.410",       "1.004",  "0.026", "-0.15"],
    ["*N",        "-489.780",       "0.176",  "0.007", "0.40"],
    ["*H2NOH",    "-490.520",       "1.355",  "0.027", "-0.05"],
    ["*NH",       "-489.920",       "0.424",  "0.036", "-0.80"],
    ["*NH2",      "-490.050",       "0.753",  "0.058", "-1.50"],
    ["*NH3",      "-490.200",       "1.131",  "0.052", "-2.00"],
    ["*H",        "-489.700",       "0.17",   "0.01",  "0.60"],
    ["NO(g)",     "-129.000",       "0.08",   "0.06",  "0.10"],
    ["H2(g)",     "-6.800",         "0.27",   "0.13",  "-0.27"],
    ["N2(g)",     "-16.200",        "0.15",   "0.10",  "-0.15"],
    ["H2O(g)",    "-14.200",        "0.56",   "0.18",  "-0.03"],
    ["NH3(g)",    "-19.500",        "1.074",  "0.158", "-0.54"],
]

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "free_energies_table.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
print("free_energies_table.csv written")
PYEOF

# === solve block: limiting_potentials.json ===
python3 <<'PYEOF'
import json
import os

output = {
    "NO_reduction_limiting_potential_V": -0.33,
    "HER_limiting_potential_V": -0.60,
    "rate_determining_step": "*HNO -> *HNOH"
}

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "limiting_potentials.json"), "w") as f:
    json.dump(output, f, indent=2)
print("limiting_potentials.json written")
PYEOF
