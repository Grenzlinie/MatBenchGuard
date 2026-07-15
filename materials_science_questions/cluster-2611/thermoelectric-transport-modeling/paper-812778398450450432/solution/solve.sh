#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimum_transport.csv ===
python3 -c '
import csv, sys
rows = [
    {"compound": "Be2C",  "T": 300, "PF": 6.78e-3,  "S": 8.84e-6,  "n": 1.5e21},
    {"compound": "Be2C",  "T": 500, "PF": 13.93e-3, "S": 12.0e-6,  "n": 1.8e21},
    {"compound": "Be2C",  "T": 800, "PF": 26.33e-3, "S": 15.0e-6,  "n": 2.0e21},
    {"compound": "BeMgC", "T": 300, "PF": 9.88e-3,  "S": 14.5e-6,  "n": 1.6e21},
    {"compound": "BeMgC", "T": 500, "PF": 19.40e-3, "S": 20.0e-6,  "n": 2.0e21},
    {"compound": "BeMgC", "T": 800, "PF": 35.94e-3, "S": 25.0e-6,  "n": 2.5e21},
    {"compound": "Mg2C",  "T": 300, "PF": 17.10e-3, "S": 22.76e-6, "n": 2.0e21},
    {"compound": "Mg2C",  "T": 500, "PF": 31.00e-3, "S": 30.0e-6,  "n": 2.5e21},
    {"compound": "Mg2C",  "T": 800, "PF": 58.20e-3, "S": 40.0e-6,  "n": 3.0e21},
]
out = "%s/optimum_transport.csv" % sys.argv[1]
with open(out, "w") as f:
    w = csv.writer(f)
    w.writerow(["compound", "temperature", "PF_max", "S_max", "sigma_at_max", "carrier_concentration"])
    for r in rows:
        sigma = r["PF"] / (r["S"]**2)
        w.writerow([r["compound"], r["T"], r["PF"], r["S"], sigma, r["n"]])
' "$OUTDIR"

# === solve block: mg2c_phonon.json ===
python3 -c '
import json, sys
data = {"TO": [421.78], "Raman": 389.18, "LO": 635.99, "LO-TO_split": 214.21}
out = f"{sys.argv[1]}/mg2c_phonon.json"
with open(out, "w") as f:
    json.dump(data, f, indent=2)
' "$OUTDIR"

# === solve finalize ===
echo "Oracle solve complete"
