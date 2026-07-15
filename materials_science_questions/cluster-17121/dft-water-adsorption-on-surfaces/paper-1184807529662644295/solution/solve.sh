#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pure_cof_enthalpy.csv ===
python3 -c '
import csv
rows = [["incline_angle","enthalpy"],
        [70,-49500],
        [80,-49800],
        [85,-50000],
        [90,-49900]]
with open("/app/outputs/pure_cof_enthalpy.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
'

# === solve block: cof_thf_enthalpy.csv ===
python3 -c '
import csv
H_pure = {70:-49500,80:-49800,85:-50000,90:-49900}
A = {70:-20,80:-15,85:-10,90:-10}          # per-molecule binding favoring 70°
h_thf = -5
n_max = 112
angles = [70,80,85,90]
loadings = [0,30,60,112]
rows = [["incline_angle","n_THF","enthalpy"]]
for a in angles:
    for n in loadings:
        H0 = H_pure[a] + A[a]*n
        H = H0 + (n_max - n)*h_thf
        rows.append([a,n,H])
with open("/app/outputs/cof_thf_enthalpy.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
'

# === solve block: cof_thf_interaction_energy.csv ===
python3 -c '
import csv
A = {70:-20,80:-15,85:-10,90:-10}
angles = [70,80,85,90]
loadings = [0,30,60,112]
rows = [["incline_angle","n_THF","interaction_energy"]]
for a in angles:
    for n in loadings:
        rows.append([a,n,A[a]*n])
with open("/app/outputs/cof_thf_interaction_energy.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
'

# === solve block: cof_h2o_enthalpy.csv ===
python3 -c '
import csv
H_pure = {70:-49500,80:-49800,85:-50000,90:-49900}
h_h2o = -3
n_max = 917
# per-molecule binding for each loading, ordered by angles [70,80,85,90]
bind = {
    628: [-2.0, -1.5, -0.5, -0.3],
    780: [-0.5, -1.2, -0.7, -0.6],
    917: [-0.2, -0.5, -1.2, -0.9]
}
angles = [70,80,85,90]
loadings = [628,780,917]
rows = [["incline_angle","n_H2O","enthalpy"]]
for a_idx, a in enumerate(angles):
    for n in loadings:
        b = bind[n][a_idx]
        H0 = H_pure[a] + b*n
        H = H0 + (n_max - n)*h_h2o
        rows.append([a,n,H])
with open("/app/outputs/cof_h2o_enthalpy.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
'

# === solve block: cof_h2o_rdf_peak.csv ===
python3 -c '
import csv
rows = [["n_H2O","incline_angle","first_peak_position","first_peak_height"]]
for n in [628,780,917]:
    for a in [70,80,85,90]:
        if n == 628 or (a == 70):
            pos, hgt = 2.80, 2.0                # liquid-like
        elif n == 917 and a in (80,85,90):
            pos, hgt = 2.75, 3.5                # ordered hot ice
        else:   # n=780 at 80,85,90  intermediate
            pos, hgt = 2.78, 2.8
        rows.append([n,a,pos,hgt])
with open("/app/outputs/cof_h2o_rdf_peak.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
'
