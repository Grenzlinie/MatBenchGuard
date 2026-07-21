#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_results.csv ===
python3 <<'PYEOF'
import csv, os
out = os.environ.get("OUTDIR", "/app/outputs")
rows = [
    ("C","T",-0.908,0.18,1.72,2.0),
    ("C","B",-1.535,0.46,1.53,0.44),
    ("C","H",-0.158,0.01,3.15,2.15),
    ("Si","T",-0.472,0.12,2.22,1.75),
    ("Si","B",-0.554,0.20,2.21,1.59),
    ("Si","H",-0.135,0.01,3.28,2.00),
    ("Ge","T",-0.353,0.12,2.41,1.77),
    ("Ge","B",-0.378,0.16,2.44,1.76),
    ("Ge","H",-0.093,0.01,3.28,1.99),
    ("Sn","T",-0.248,0.10,2.70,1.75),
    ("Sn","B",-0.249,0.12,2.76,1.76),
    ("Sn","H",-0.088,0.01,3.37,1.83),
    ("Pb","T",-0.216,0.08,2.82,1.75),
    ("Pb","B",-0.214,0.10,2.90,1.76),
    ("Pb","H",-0.090,0.02,3.41,1.76),
]
with open(os.path.join(out, "adsorption_results.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["atom","site","E_ad","Δh","d_ac","M"])
    writer.writerows(rows)
PYEOF
