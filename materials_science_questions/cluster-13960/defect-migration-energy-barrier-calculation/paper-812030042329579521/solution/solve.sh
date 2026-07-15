#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: stability_table.csv ===
python3 - "$OUTDIR" << 'PYEOF'
import csv, sys
outdir = sys.argv[1]

# Separation distances for the nine configurations (angstroms)
seps = {
    1: 3.45,
    2: 3.92,
    3: 4.38,
    4: 4.96,
    5: 5.43,
    6: 6.01,
    7: 6.68,
    8: 7.35,
    9: 8.10,
}

# Stability: config_id -> (stable at +2?, 0?, -2?)
stable_map = {
    1: (True, False, False),
    2: (True, False, False),
    3: (True, False, False),
    4: (True, False, False),
    5: (True, False, False),
    6: (True, False, False),
    7: (True, True, False),
    8: (True, True, False),
    9: (True, True, True),
}

rows = []
for cid, (s2, s0, sm2) in stable_map.items():
    rows.append([cid, 2, seps[cid], s2])
    rows.append([cid, 0, seps[cid], s0])
    rows.append([cid, -2, seps[cid], sm2])

with open(f"{outdir}/stability_table.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["config_id", "charge_state", "separation_A", "stable"])
    w.writerows(rows)
PYEOF

# === solve block: energies_summary.csv ===
python3 - "$OUTDIR" << 'PYEOF'
import csv, sys
outdir = sys.argv[1]

# Isolated defect energies (E_bulk set to 0 for convenience)
E_vac = 3.52
E_int = 3.44
E_sum = E_vac + E_int   # 6.96 eV

# Formation energies for each config (eV), increasing with separation
form_energy = {
    1: 5.95,
    2: 5.98,
    3: 6.10,
    4: 6.15,
    5: 6.25,
    6: 6.40,
    7: 6.55,
    8: 6.65,
    9: 6.70,
}

# Stability map (structurally same as stability_table)
stable_map = {
    1: [2],
    2: [2],
    3: [2],
    4: [2],
    5: [2],
    6: [2],
    7: [2, 0],
    8: [2, 0],
    9: [2, 0, -2],
}

rows = []
for cid, charges in stable_map.items():
    for cs in charges:
        fe = form_energy[cid]
        be = E_sum - fe
        # total_energy_eV = formation energy (since E_bulk=0)
        rows.append(["FP", cid, cs, fe, fe, be])

# Isolated defects
rows.append(["vacancy", "", "", E_vac, "", ""])
rows.append(["interstitial", "", "", E_int, "", ""])

with open(f"{outdir}/energies_summary.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["type", "config_id", "charge_state", "total_energy_eV",
                "formation_energy_eV", "binding_energy_eV"])
    w.writerows(rows)
PYEOF

# === solve finalize ===
echo "Oracle artifacts written."
