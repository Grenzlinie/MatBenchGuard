#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: group_theory_summary.txt ===
cat << 'EOF' > "$OUTDIR/group_theory_summary.txt"
Group theory analysis of LiNH2 (space group I-4) zone-centre phonon modes.

Raman-active modes (excluding acoustic A+E):
  Phonon region (0-700 cm^{-1}): 7 A, 8 B, 9 E  (total 24)
  Molecular vibration region (NH2 bending & stretching): 3 A, 3 B, 3 E  (total 9)

Total Raman-active modes: 10 A + 11 B + 12 E = 33 modes.

Selection rules: A appears in (aa),(bb),(cc); B in (ab),(a+b a-b); E in (ac),(bc).
EOF

# === solve block: computed_phonon_frequencies.csv ===
cat << 'EOF' > "$OUTDIR/computed_phonon_frequencies.csv"
mode_number,symmetry,frequency_rt,region
1,E,109,I
2,B,184,I
3,E,195,I
4,A,210,I
5,E,239,I
6,B,257,I
7,A,275,I
8,E,279,I
9,A,305,I
10,B,312,I
11,E,317,I
12,B,338,I
13,A,348,I
14,E,385,I
15,A,404,I
16,B,419,I
17,B,457,I
18,E,500,I
19,A,515,I
20,E,569,I
21,B,600,I
22,A,669,I
23,E,679,I
24,B,719,I
25,E,1435,II
26,B,1485,II
27,A,1502,II
28,A,3257,III
29,E,3263,III
30,B,3265,III
31,E,3345,III
32,B,3346,III
33,A,3348,III
EOF
