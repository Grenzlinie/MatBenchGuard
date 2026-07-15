#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: geometries.csv ===
python3 << 'PYEOF'
import csv
import os

outpath = os.path.join(os.environ.get("OUTDIR", "/app/outputs"), "geometries.csv")
rows = []

# Si2
params = [("OLYP", "r(Si-Si)", 2.298, "Å"),
          ("OPW91", "r(Si-Si)", 2.165, "Å"),
          ("OB95", "r(Si-Si)", 2.162, "Å"),
          ("VSXC", "r(Si-Si)", 2.156, "Å"),
          ("PBE0", "r(Si-Si)", 2.265, "Å"),
          ("B3LYP", "r(Si-Si)", 2.280, "Å")]
for func, param, val, unit in params:
    rows.append({"cluster": "Si2", "functional": func, "parameter": param, "unit": unit, "value": val})

# CuSi
params = [("OLYP", "r(Si-Cu)", 2.246, "Å"),
          ("OPW91", "r(Si-Cu)", 2.232, "Å"),
          ("OB95", "r(Si-Cu)", 2.221, "Å"),
          ("VSXC", "r(Si-Cu)", 2.235, "Å"),
          ("PBE0", "r(Si-Cu)", 2.243, "Å"),
          ("B3LYP", "r(Si-Cu)", 2.251, "Å")]
for func, param, val, unit in params:
    rows.append({"cluster": "CuSi", "functional": func, "parameter": param, "unit": unit, "value": val})

# Si3
params_r13 = [("OLYP", 2.194), ("OPW91", 2.185), ("OB95", 2.180), ("VSXC", 2.174), ("PBE0", 2.183), ("B3LYP", 2.185)]
for func, val in params_r13:
    rows.append({"cluster": "Si3", "functional": func, "parameter": "r(Si1-Si3)", "unit": "Å", "value": val})
params_r12 = [("OLYP", 2.892), ("OPW91", 2.811), ("OB95", 2.784), ("VSXC", 2.889), ("PBE0", 2.846), ("B3LYP", 2.877)]
for func, val in params_r12:
    rows.append({"cluster": "Si3", "functional": func, "parameter": "r(Si1-Si2)", "unit": "Å", "value": val})
params_a = [("OLYP", 82.455), ("OPW91", 80.083), ("OB95", 79.357), ("VSXC", 83.263), ("PBE0", 81.372), ("B3LYP", 82.348)]
for func, val in params_a:
    rows.append({"cluster": "Si3", "functional": func, "parameter": "α(Si1-Si3-Si2)", "unit": "°", "value": val})

# CuSi2
params_rSiCu = [("OLYP", 2.324), ("OPW91", 2.303), ("OB95", 2.290), ("VSXC", 2.311), ("PBE0", 2.322), ("B3LYP", 2.337)]
for func, val in params_rSiCu:
    rows.append({"cluster": "CuSi2", "functional": func, "parameter": "r(Si1-Cu)", "unit": "Å", "value": val})
params_rSiSi = [("OLYP", 2.179), ("OPW91", 2.166), ("OB95", 2.164), ("VSXC", 2.161), ("PBE0", 2.151), ("B3LYP", 2.170)]
for func, val in params_rSiSi:
    rows.append({"cluster": "CuSi2", "functional": func, "parameter": "r(Si1-Si2)", "unit": "Å", "value": val})
params_a_SiCuSi = [("OLYP", 55.923), ("OPW91", 56.081), ("OB95", 56.400), ("VSXC", 55.763), ("PBE0", 55.191), ("B3LYP", 55.320)]
for func, val in params_a_SiCuSi:
    rows.append({"cluster": "CuSi2", "functional": func, "parameter": "α(Si1-Cu-Si2)", "unit": "°", "value": val})

# Si4
params_r14 = [("OLYP", 2.335), ("OPW91", 2.322), ("OB95", 2.315), ("VSXC", 2.309), ("PBE0", 2.313), ("B3LYP", 2.329)]
for func, val in params_r14:
    rows.append({"cluster": "Si4", "functional": func, "parameter": "r(Si1-Si4)", "unit": "Å", "value": val})
params_r12_si4 = [("OLYP", 2.421), ("OPW91", 2.398), ("OB95", 2.385), ("VSXC", 2.394), ("PBE0", 2.401), ("B3LYP", 2.430)]
for func, val in params_r12_si4:
    rows.append({"cluster": "Si4", "functional": func, "parameter": "r(Si1-Si2)", "unit": "Å", "value": val})
params_a_Si4 = [("OLYP", 62.462), ("OPW91", 62.169), ("OB95", 62.002), ("VSXC", 62.437), ("PBE0", 62.521), ("B3LYP", 62.893)]
for func, val in params_a_Si4:
    rows.append({"cluster": "Si4", "functional": func, "parameter": "α(Si1-Si3-Si2)", "unit": "°", "value": val})

# CuSi3
params_rSiCu_csi3 = [("OLYP", 2.271), ("OPW91", 2.249), ("OB95", 2.233), ("VSXC", 2.263), ("PBE0", 2.263), ("B3LYP", 2.279)]
for func, val in params_rSiCu_csi3:
    rows.append({"cluster": "CuSi3", "functional": func, "parameter": "r(Si1-Cu)", "unit": "Å", "value": val})
params_rSi3 = [("OLYP", 2.265), ("OPW91", 2.258), ("OB95", 2.243), ("VSXC", 2.247), ("PBE0", 2.237), ("B3LYP", 2.265)]
for func, val in params_rSi3:
    rows.append({"cluster": "CuSi3", "functional": func, "parameter": "r(Si1-Si3)", "unit": "Å", "value": val})
params_a_Si3Si2 = [("OLYP", 93.437), ("OPW91", 91.682), ("OB95", 93.044), ("VSXC", 95.592), ("PBE0", 90.349), ("B3LYP", 93.437)]
for func, val in params_a_Si3Si2:
    rows.append({"cluster": "CuSi3", "functional": func, "parameter": "α(Si1-Si3-Si2)", "unit": "°", "value": val})
params_a_CuSi2 = [("OLYP", 93.141), ("OPW91", 91.643), ("OB95", 93.606), ("VSXC", 94.679), ("PBE0", 88.974), ("B3LYP", 93.141)]
for func, val in params_a_CuSi2:
    rows.append({"cluster": "CuSi3", "functional": func, "parameter": "α(Si1-Cu-Si2)", "unit": "°", "value": val})

# Si5
params_r12_si5 = [("OLYP", 2.965), ("OPW91", 2.964), ("OB95", 2.976), ("VSXC", 2.922), ("PBE0", 2.951), ("B3LYP", 2.947)]
for func, val in params_r12_si5:
    rows.append({"cluster": "Si5", "functional": func, "parameter": "r(Si1-Si2)", "unit": "Å", "value": val})
params_r13_si5 = [("OLYP", 2.321), ("OPW91", 2.300), ("OB95", 2.288), ("VSXC", 2.301), ("PBE0", 2.306), ("B3LYP", 2.329)]
for func, val in params_r13_si5:
    rows.append({"cluster": "Si5", "functional": func, "parameter": "r(Si1-Si3)", "unit": "Å", "value": val})
params_r34_si5 = [("OLYP", 3.094), ("OPW91", 3.047), ("OB95", 3.006), ("VSXC", 3.081), ("PBE0", 3.068), ("B3LYP", 3.124)]
for func, val in params_r34_si5:
    rows.append({"cluster": "Si5", "functional": func, "parameter": "r(Si3-Si4)", "unit": "Å", "value": val})

# CuSi4
params_rSi1Cu_csi4 = [("OLYP", 2.498), ("OPW91", 2.573), ("OB95", 2.534), ("VSXC", 2.616), ("PBE0", 2.623), ("B3LYP", 2.563)]
for func, val in params_rSi1Cu_csi4:
    rows.append({"cluster": "CuSi4", "functional": func, "parameter": "r(Si1-Cu)", "unit": "Å", "value": val})
params_rSi4Cu = [("OLYP", 2.366), ("OPW91", 2.406), ("OB95", 2.387), ("VSXC", 2.431), ("PBE0", 2.401), ("B3LYP", 2.360)]
for func, val in params_rSi4Cu:
    rows.append({"cluster": "CuSi4", "functional": func, "parameter": "r(Si4-Cu)", "unit": "Å", "value": val})
params_rSi1Si2_csi4 = [("OLYP", 2.431), ("OPW91", 2.438), ("OB95", 2.428), ("VSXC", 2.432), ("PBE0", 2.398), ("B3LYP", 2.438)]
for func, val in params_rSi1Si2_csi4:
    rows.append({"cluster": "CuSi4", "functional": func, "parameter": "r(Si1-Si2)", "unit": "Å", "value": val})
params_rSi1Si3_csi4 = [("OLYP", 2.359), ("OPW91", 2.358), ("OB95", 2.350), ("VSXC", 2.353), ("PBE0", 2.353), ("B3LYP", 2.354)]
for func, val in params_rSi1Si3_csi4:
    rows.append({"cluster": "CuSi4", "functional": func, "parameter": "r(Si1-Si3)", "unit": "Å", "value": val})
params_rSi1Si4_csi4 = [("OLYP", 2.413), ("OPW91", 2.421), ("OB95", 2.415), ("VSXC", 2.429), ("PBE0", 2.395), ("B3LYP", 2.405)]
for func, val in params_rSi1Si4_csi4:
    rows.append({"cluster": "CuSi4", "functional": func, "parameter": "r(Si1-Si4)", "unit": "Å", "value": val})
params_dihedral = [("OLYP", 177.237), ("OPW91", 177.347), ("OB95", 177.278), ("VSXC", 177.157), ("PBE0", 178.415), ("B3LYP", 179.608)]
for func, val in params_dihedral:
    rows.append({"cluster": "CuSi4", "functional": func, "parameter": "α(Si3-Si1-Si2-Si4)", "unit": "°", "value": val})

with open(outpath, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["cluster", "functional", "parameter", "unit", "value"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
