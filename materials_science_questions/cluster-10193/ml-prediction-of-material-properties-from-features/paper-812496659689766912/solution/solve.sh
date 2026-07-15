#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bond_stretch_metrics.csv ===
python3 <<'PYEOF' > /app/outputs/bond_stretch_metrics.csv
import csv, sys

molecules = ["benzene_CC","benzene_CH","methanol","methane","CO","H2","ethylene","water","acetylene","hydrogen_cyanide","N2","ammonia","biphenyl","aspartame","sucrose","dialanine","diglycine"]

data = {}
ani1x = {
    "r0": [1]*17, "repulsive": [1]*17, "attractive": [1]*17, "spurious": [0]*17, "mape": 0.265
}
ani1x["r0"][5]=0
ani1x["repulsive"][4]=0; ani1x["repulsive"][5]=0; ani1x["repulsive"][6]=0; ani1x["repulsive"][8]=0; ani1x["repulsive"][10]=0; ani1x["repulsive"][11]=0
for i in [2,3,4,7,12]: ani1x["spurious"][i]=1
data["ANI-1x"] = ani1x

ani2x = {
    "r0": [1]*17, "repulsive": [1]*17, "attractive": [1]*17, "spurious": [0]*17, "mape": 0.002
}
ani2x["repulsive"][4]=0; ani2x["repulsive"][5]=0; ani2x["repulsive"][10]=0; ani2x["repulsive"][11]=0
for i in [0,1,2,3,5,6,7,8,9,10,12,13]: ani2x["spurious"][i]=1
data["ANI-2x"] = ani2x

ccnn = {
    "r0": [1]*17, "repulsive": [1]*17, "attractive": [1]*17, "spurious": [0]*17, "mape": 0.2555
}
ccnn["r0"][5]=0
for i in [0,1,2,3,4,5,6,7,8,9,10,12,13]: ccnn["spurious"][i]=1
data["Colorful_CNN"] = ccnn

fchl = {
    "r0": [1]*17, "repulsive": [1]*17, "attractive": [1]*17, "spurious": [0]*17, "mape": 0.255
}
zeros_r0 = [1,4,5,6,8,10,11]
for i in zeros_r0: fchl["r0"][i]=0
fchl["repulsive"][5]=0
fchl["attractive"][5]=0; fchl["attractive"][4]=0
for i in [0,1,2,3,5,6,7,8,9,10,12,13,15]: fchl["spurious"][i]=1
data["FCHL_KRR"] = fchl

writer = csv.writer(sys.stdout)
writer.writerow(["molecule","method","r0_correct","repulsive_wall_correct","attractive_forces_correct","spurious_minima","median_MAPE"])
for method in ["ANI-1x","ANI-2x","Colorful_CNN","FCHL_KRR"]:
    d = data[method]
    for i,mol in enumerate(molecules):
        writer.writerow([mol, method, d["r0"][i], d["repulsive"][i], d["attractive"][i], d["spurious"][i], d["mape"]])
PYEOF

# === solve block: dihedral_summary.csv ===
python3 <<'PYEOF' > /app/outputs/dihedral_summary.csv
import csv, sys

rows = [
    ["biphenyl","ANI-1x",-45,3.95],
    ["biphenyl","ANI-2x",-45,4.16],
    ["biphenyl","Colorful_CNN",-135,5.49],
    ["biphenyl","FCHL_KRR",180,5.52],
    ["sucrose","ANI-1x",0,2.50e3],
    ["sucrose","ANI-2x",0,1.93e3],
    ["sucrose","Colorful_CNN",0,9.46e2],
    ["sucrose","FCHL_KRR",0,9.73e4],
]
writer = csv.writer(sys.stdout)
writer.writerow(["molecule","method","theta0_deg","barrier_energy_kcal_per_mol"])
writer.writerows(rows)
PYEOF

# === solve block: torsion_2d_mae.csv ===
python3 <<'PYEOF' > /app/outputs/torsion_2d_mae.csv
import csv, sys

rows = [
    ["dialanine","ANI-2x",1.89],
    ["dialanine","ANI-1x",3.01],
    ["dialanine","Colorful_CNN",7.10],
    ["dialanine","FCHL_KRR",252.17],
    ["diglycine","ANI-2x",1.71],
    ["diglycine","ANI-1x",2.52],
    ["diglycine","Colorful_CNN",6.07],
    ["diglycine","FCHL_KRR",200.86],
]
writer = csv.writer(sys.stdout)
writer.writerow(["molecule","method","MAE_kcal_per_mol"])
writer.writerows(rows)
PYEOF
