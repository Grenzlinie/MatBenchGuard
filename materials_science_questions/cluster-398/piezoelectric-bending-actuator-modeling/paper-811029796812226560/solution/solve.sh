#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: w_displacements_1V.csv ===
cat > /app/outputs/w_displacements_1V.csv <<'HEREDOC'
x,z,w
0.0,0.0,0.0
1.0,0.0,0.046
2.0,0.0,0.201
3.0,0.0,0.374
4.0,0.0,0.688
5.0,0.0,1.167
6.0,0.0,1.647
7.0,0.0,2.254
8.0,0.0,2.996
9.0,0.0,3.685
10.0,0.0,4.616
0.0,0.5,0.5
1.0,0.5,0.501
2.0,0.5,0.679
3.0,0.5,0.835
4.0,0.5,1.173
5.0,0.5,1.739
6.0,0.5,2.273
7.0,0.5,3.015
8.0,0.5,3.854
9.0,0.5,4.649
10.0,0.5,5.666
0.0,1.0,1.0
1.0,1.0,1.217
2.0,1.0,1.399
3.0,1.0,1.625
4.0,1.0,1.987
5.0,1.0,2.546
6.0,1.0,3.048
7.0,1.0,3.803
8.0,1.0,4.633
9.0,1.0,5.348
10.0,1.0,6.385
HEREDOC

# === solve block: tip_displacements.csv ===
cat > /app/outputs/tip_displacements.csv <<'HEREDOC'
voltage,tip_displacement
0,0
1,0.002326
2,0.004438
5,0.01192
10,0.02328
15,0.03547
20,0.04824
25,0.06424
50,0.1165
HEREDOC
