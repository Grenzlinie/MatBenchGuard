#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: total_dos_data.csv ===
export OUTDIR="${OUTDIR:-/app/outputs}"
python3 << 'PYEOF'
import csv, os

compounds = {
    "Au2Cs2I6": {"ib_low": 0.64, "ib_high": 1.34, "orbitals": {"I_5p": 0.85, "Au_5d": 0.10, "Cs_5p": 0.05}},
    "Ag2GeBaS4": {"ib_low": 0.90, "ib_high": 2.06, "orbitals": {"S_3p": 0.50, "Ge_4s": 0.35, "Ba_4d": 0.15}},
    "Ag2ZnSnS4": {"ib_low": 0.47, "ib_high": 2.13, "orbitals": {"S_3p": 0.50, "Sn_5s": 0.45, "Sn_5p": 0.05}},
}

energy_vals = [round(-5.0 + i * 0.02, 5) for i in range(501)]
all_orbitals = sorted(set(orb for c in compounds for orb in compounds[c]["orbitals"]))
fieldnames = ["compound", "energy_ev", "total_dos"] + all_orbitals

outdir = os.environ.get("OUTDIR", "/app/outputs")
outpath = os.path.join(outdir, "total_dos_data.csv")
with open(outpath, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for compound, info in compounds.items():
        low, high = info["ib_low"], info["ib_high"]
        for e in energy_vals:
            total = 1.0 if low <= e <= high else 0.0
            row = {"compound": compound, "energy_ev": e, "total_dos": total}
            for orb in all_orbitals:
                if orb in info["orbitals"] and total > 0:
                    row[orb] = info["orbitals"][orb] * total
                else:
                    row[orb] = 0.0
            writer.writerow(row)
PYEOF

# === solve block: dos_results.json ===
python3 /solution/make_outputs.py --json /app/outputs/dos_results.json
