#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
python3 <<'PYEOF'
import csv

mus = [-4.0, -2.0, 0.0]
rows = []

# pure_CNT interior_C (constant energies)
for mu in mus:
    rows.append({"system": "pure_CNT", "defect": "V_C", "location": "interior_C", "mu_N": mu, "E_f": 9.0})
    rows.append({"system": "pure_CNT", "defect": "B_C", "location": "interior_C", "mu_N": mu, "E_f": 5.0})
    rows.append({"system": "pure_CNT", "defect": "N_C", "location": "interior_C", "mu_N": mu, "E_f": 8.0})

# pure_BNNT interior_BN (constant energies)
for mu in mus:
    rows.append({"system": "pure_BNNT", "defect": "V_B", "location": "interior_BN", "mu_N": mu, "E_f": 14.0})
    rows.append({"system": "pure_BNNT", "defect": "V_N", "location": "interior_BN", "mu_N": mu, "E_f": 14.0})
    rows.append({"system": "pure_BNNT", "defect": "C_B", "location": "interior_BN", "mu_N": mu, "E_f": 10.0})
    rows.append({"system": "pure_BNNT", "defect": "C_N", "location": "interior_BN", "mu_N": mu, "E_f": 9.0})

# hybrid interface_N (defective formation energies decrease as mu_N becomes more negative, i.e. N-poor)
configs_N = [("C_N", 5.0), ("B_C", 2.0), ("V_N", 9.0), ("V_B", 11.0), ("V_C", 6.0)]
for defect, base in configs_N:
    for mu in mus:
        ef = round(base + 0.5 * mu, 2)
        rows.append({"system": "hybrid", "defect": defect, "location": "interface_N", "mu_N": mu, "E_f": ef})

# hybrid interface_B (defective formation energies increase as mu_N becomes more negative, i.e. N-poor)
configs_B = [("C_B", 7.0), ("N_C", 5.0), ("V_N", 10.0), ("V_B", 12.0), ("V_C", 7.0)]
for defect, base in configs_B:
    for mu in mus:
        ef = round(base - 0.5 * mu, 2)
        rows.append({"system": "hybrid", "defect": defect, "location": "interface_B", "mu_N": mu, "E_f": ef})

with open("/app/outputs/formation_energies.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["system","defect","location","mu_N","E_f"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
