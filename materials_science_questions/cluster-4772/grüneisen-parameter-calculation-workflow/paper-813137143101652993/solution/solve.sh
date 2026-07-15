#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: output_results.csv ===
mkdir -p "/app/outputs"
python3 << 'PYEOF'
import csv

rows = [
    # set, method, s, dlns_dlnV, gamma_t
    ["KCl 0K", "Szigeti II",        "", "-0.05553", ""],
    ["KCl 300K", "Szigeti II",       "",  "0.05810", ""],
    ["KBr 300K", "Szigeti II",       "", "-0.15131", ""],
    ["KI 300K", "Szigeti II",        "",  "0.23267", ""],
    ["KCl 0K", "Szigeti I+II",       "", "-0.07279", "2.47726"],
    ["KCl 300K", "Szigeti I+II",     "", "-0.10591", "2.62482"],
    ["KBr 300K", "Szigeti I+II",     "", "-0.04735", "2.72604"],
    ["KI 300K", "Szigeti I+II",      "", "-0.63096", "2.97363"],
    ["KCl 0K", "Hardy Born-Lande",  "0.76250", "0.95839", ""],
    ["KCl 300K", "Hardy Born-Lande", "0.78535", "0.89999", ""],
    ["KBr 300K", "Hardy Born-Lande", "0.72879", "1.18100", ""],
    ["KI 300K", "Hardy Born-Lande",  "0.69323", "1.43275", ""],
    ["KCl 0K", "Hardy Born-Mayer",  "0.76250", "0.93618", ""],
    ["KCl 300K", "Hardy Born-Mayer", "0.78535", "0.87686", ""],
    ["KBr 300K", "Hardy Born-Mayer", "0.72879", "1.14802", ""],
    ["KI 300K", "Hardy Born-Mayer",  "0.69323", "1.39450", ""],
    ["KCl 0K", "Hardy Hellmann",    "0.76250", "0.95839", ""],
    ["KCl 300K", "Hardy Hellmann",   "0.78535", "0.89999", ""],
    ["KBr 300K", "Hardy Hellmann",   "0.72879", "1.18100", ""],
    ["KI 300K", "Hardy Hellmann",    "0.69323", "1.43275", ""],
]

with open("/app/outputs/output_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["set", "method", "s", "dlns_dlnV", "gamma_t"])
    writer.writerows(rows)
PYEOF
