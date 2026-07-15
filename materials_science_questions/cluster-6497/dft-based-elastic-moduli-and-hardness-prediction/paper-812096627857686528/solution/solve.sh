#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: atom_in_jellium_parameters.csv ===
python3 << 'PYEOF'
import csv, os

outdir = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "atom_in_jellium_parameters.csv")

data = [
    {"element":"H",   "E0_LDA":-2.16,"E0_GGA":-1.96,"s0_LDA":1.56,"s0_GGA":1.66,"eta_LDA":2.70,"eta_GGA":2.70,"E2_LDA":3.50,"E2_GGA":3.50,"B_LDA":172,"B_GGA":151},
    {"element":"He",  "E0_LDA":0.0,  "E0_GGA":0.0,  "s0_LDA":3.00,"s0_GGA":3.00,"eta_LDA":0.0, "eta_GGA":0.0, "E2_LDA":0.0, "E2_GGA":0.0, "B_LDA":0,  "B_GGA":0},
    {"element":"Li",  "E0_LDA":-1.63,"E0_GGA":-1.53,"s0_LDA":3.25,"s0_GGA":3.32,"eta_LDA":2.80,"eta_GGA":2.80,"E2_LDA":0.80,"E2_GGA":0.80,"B_LDA":14 ,"B_GGA":13},
    {"element":"Be",  "E0_LDA":-3.32,"E0_GGA":-2.92,"s0_LDA":2.35,"s0_GGA":2.42,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":1.80,"E2_GGA":1.80,"B_LDA":130,"B_GGA":115},
    {"element":"B",   "E0_LDA":-5.58,"E0_GGA":-5.10,"s0_LDA":2.00,"s0_GGA":2.06,"eta_LDA":3.20,"eta_GGA":3.20,"E2_LDA":3.00,"E2_GGA":3.00,"B_LDA":320,"B_GGA":280},
    {"element":"C",   "E0_LDA":-7.37,"E0_GGA":-6.77,"s0_LDA":1.72,"s0_GGA":1.78,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":5.50,"E2_GGA":5.50,"B_LDA":440,"B_GGA":380},
    {"element":"N",   "E0_LDA":-4.92,"E0_GGA":-4.42,"s0_LDA":1.76,"s0_GGA":1.82,"eta_LDA":3.50,"eta_GGA":3.50,"E2_LDA":4.00,"E2_GGA":4.00,"B_LDA":310,"B_GGA":270},
    {"element":"O",   "E0_LDA":-4.14,"E0_GGA":-3.64,"s0_LDA":1.68,"s0_GGA":1.74,"eta_LDA":3.80,"eta_GGA":3.80,"E2_LDA":5.00,"E2_GGA":5.00,"B_LDA":400,"B_GGA":350},
    {"element":"F",   "E0_LDA":-2.85,"E0_GGA":-2.45,"s0_LDA":1.52,"s0_GGA":1.58,"eta_LDA":4.50,"eta_GGA":4.50,"E2_LDA":6.00,"E2_GGA":6.00,"B_LDA":550,"B_GGA":480},
    {"element":"Ne",  "E0_LDA":0.0,  "E0_GGA":0.0,  "s0_LDA":2.00,"s0_GGA":2.00,"eta_LDA":0.0, "eta_GGA":0.0, "E2_LDA":0.0, "E2_GGA":0.0, "B_LDA":0,  "B_GGA":0},
    {"element":"Na",  "E0_LDA":-1.13,"E0_GGA":-1.03,"s0_LDA":3.93,"s0_GGA":4.05,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":0.50,"E2_GGA":0.50,"B_LDA":7  ,"B_GGA":7},
    {"element":"Mg",  "E0_LDA":-1.55,"E0_GGA":-1.35,"s0_LDA":3.40,"s0_GGA":3.49,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":0.80,"E2_GGA":0.80,"B_LDA":35 ,"B_GGA":31},
    {"element":"Al",  "E0_LDA":-3.39,"E0_GGA":-3.09,"s0_LDA":3.00,"s0_GGA":3.08,"eta_LDA":3.10,"eta_GGA":3.10,"E2_LDA":1.50,"E2_GGA":1.50,"B_LDA":75 ,"B_GGA":65},
    {"element":"Si",  "E0_LDA":-4.63,"E0_GGA":-4.13,"s0_LDA":2.80,"s0_GGA":2.86,"eta_LDA":3.30,"eta_GGA":3.30,"E2_LDA":2.50,"E2_GGA":2.50,"B_LDA":100,"B_GGA":85},
    {"element":"P",   "E0_LDA":-5.44,"E0_GGA":-4.94,"s0_LDA":2.60,"s0_GGA":2.66,"eta_LDA":3.40,"eta_GGA":3.40,"E2_LDA":3.50,"E2_GGA":3.50,"B_LDA":120,"B_GGA":105},
    {"element":"S",   "E0_LDA":-4.92,"E0_GGA":-4.52,"s0_LDA":2.42,"s0_GGA":2.48,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":4.00,"E2_GGA":4.00,"B_LDA":150,"B_GGA":130},
    {"element":"Cl",  "E0_LDA":-3.64,"E0_GGA":-3.34,"s0_LDA":2.22,"s0_GGA":2.28,"eta_LDA":4.00,"eta_GGA":4.00,"E2_LDA":5.50,"E2_GGA":5.50,"B_LDA":200,"B_GGA":175},
    {"element":"Ar",  "E0_LDA":0.0,  "E0_GGA":0.0,  "s0_LDA":4.00,"s0_GGA":4.00,"eta_LDA":0.0, "eta_GGA":0.0, "E2_LDA":0.0, "E2_GGA":0.0, "B_LDA":0,  "B_GGA":0},
    {"element":"K",   "E0_LDA":-0.98,"E0_GGA":-0.88,"s0_LDA":4.62,"s0_GGA":4.75,"eta_LDA":2.80,"eta_GGA":2.80,"E2_LDA":0.30,"E2_GGA":0.30,"B_LDA":3  ,"B_GGA":3},
    {"element":"Ca",  "E0_LDA":-1.84,"E0_GGA":-1.64,"s0_LDA":3.90,"s0_GGA":4.00,"eta_LDA":2.90,"eta_GGA":2.90,"E2_LDA":0.60,"E2_GGA":0.60,"B_LDA":15 ,"B_GGA":13},
    {"element":"Sc",  "E0_LDA":-3.90,"E0_GGA":-3.50,"s0_LDA":3.20,"s0_GGA":3.28,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":1.20,"E2_GGA":1.20,"B_LDA":55 ,"B_GGA":48},
    {"element":"Ti",  "E0_LDA":-4.85,"E0_GGA":-4.45,"s0_LDA":3.00,"s0_GGA":3.08,"eta_LDA":3.20,"eta_GGA":3.20,"E2_LDA":1.80,"E2_GGA":1.80,"B_LDA":100,"B_GGA":85},
    {"element":"V",   "E0_LDA":-5.31,"E0_GGA":-4.91,"s0_LDA":2.90,"s0_GGA":2.97,"eta_LDA":3.30,"eta_GGA":3.30,"E2_LDA":2.20,"E2_GGA":2.20,"B_LDA":160,"B_GGA":140},
    {"element":"Cr",  "E0_LDA":-4.10,"E0_GGA":-3.70,"s0_LDA":2.80,"s0_GGA":2.87,"eta_LDA":3.40,"eta_GGA":3.40,"E2_LDA":2.60,"E2_GGA":2.60,"B_LDA":190,"B_GGA":165},
    {"element":"Mn",  "E0_LDA":-2.95,"E0_GGA":-2.65,"s0_LDA":2.70,"s0_GGA":2.77,"eta_LDA":3.50,"eta_GGA":3.50,"E2_LDA":2.80,"E2_GGA":2.80,"B_LDA":210,"B_GGA":185},
    {"element":"Fe",  "E0_LDA":-4.28,"E0_GGA":-3.88,"s0_LDA":2.60,"s0_GGA":2.66,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":3.00,"E2_GGA":3.00,"B_LDA":230,"B_GGA":200},
    {"element":"Co",  "E0_LDA":-4.39,"E0_GGA":-3.99,"s0_LDA":2.55,"s0_GGA":2.60,"eta_LDA":3.65,"eta_GGA":3.65,"E2_LDA":3.10,"E2_GGA":3.10,"B_LDA":240,"B_GGA":210},
    {"element":"Ni",  "E0_LDA":-4.44,"E0_GGA":-4.04,"s0_LDA":2.50,"s0_GGA":2.55,"eta_LDA":3.70,"eta_GGA":3.70,"E2_LDA":3.20,"E2_GGA":3.20,"B_LDA":250,"B_GGA":220},
    {"element":"Cu",  "E0_LDA":-3.49,"E0_GGA":-3.19,"s0_LDA":2.67,"s0_GGA":2.73,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":2.50,"E2_GGA":2.50,"B_LDA":180,"B_GGA":155},
    {"element":"Zn",  "E0_LDA":-1.35,"E0_GGA":-1.25,"s0_LDA":2.90,"s0_GGA":2.98,"eta_LDA":3.50,"eta_GGA":3.50,"E2_LDA":1.50,"E2_GGA":1.50,"B_LDA":70 ,"B_GGA":60},
]

header = ["element", "E0_LDA", "E0_GGA", "s0_LDA", "s0_GGA",
          "eta_LDA", "eta_GGA", "E2_LDA", "E2_GGA", "B_LDA", "B_GGA"]

with open(outpath, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header, extrasaction="raise")
    writer.writeheader()
    writer.writerows(data)

print(f"Wrote {len(data)} rows to {outpath}")
PYEOF
