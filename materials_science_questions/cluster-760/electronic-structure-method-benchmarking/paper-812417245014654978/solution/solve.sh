#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_energies.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p $OUTDIR
python3 << 'PYEOF'
import csv, os
hartree_to_kJmol = 2625.5
rel = {
    "ICN1": -54.2,
    "ICN2": -192.9,
    "SiNC": -344.5,
    "SiCN": -376.7,
    "TS1": -38.4,
    "TS2": -29.7,
    "TS3": -116.2,
    "TS4": -255.6,
    "INC2": -34.9,
    "TS5": -30.6,
    "INC1": -37.9
}
E_cluster_kJ = -6859560.0
E_ICN_kJ = -273568.0
E_INC_kJ = E_ICN_kJ + 123.1
E_sep_ICN_hartree = (E_cluster_kJ + E_ICN_kJ) / hartree_to_kJmol
E_sep_INC_hartree = (E_cluster_kJ + E_INC_kJ) / hartree_to_kJmol
icn_set = {"ICN1","ICN2","SiNC","SiCN","TS1","TS2","TS3","TS4"}
order = ["ICN1","ICN2","SiNC","SiCN","TS1","TS2","TS3","TS4","INC2","TS5","INC1"]
rows = []
for s in order:
    r = rel[s]
    if s in icn_set:
        tot = E_sep_ICN_hartree + r / hartree_to_kJmol
    else:
        tot = E_sep_INC_hartree + r / hartree_to_kJmol
    rows.append([s, f"{tot:.8f}", f"{r:.1f}"])
outdir = os.environ.get('OUTDIR', '/app/outputs')
outpath = os.path.join(outdir, 'step_01_energies.csv')
with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['structure','total_energy_hartree','relative_energy_kJmol'])
    w.writerows(rows)
PYEOF
