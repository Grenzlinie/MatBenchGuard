#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap.txt ===
cat > "$OUTDIR/band_gap.txt" <<'EOF'
0.80
EOF

# === solve block: cbm_character.txt ===
cat > "$OUTDIR/cbm_character.txt" <<'EOF'
Hf 5d_xy
EOF

# === solve block: bec.txt ===
cat > "$OUTDIR/bec.txt" <<'EOF'
atom,Zxx,Zyy,Zzz
Hf,4.52,4.52,3.09
N1,-4.66,-4.66,-1.65
N2,-2.59,-2.59,-4.58
Ba,2.73,2.73,3.14
EOF

# === solve block: dielectric.txt ===
cat > "$OUTDIR/dielectric.txt" <<'EOF'
7.47
7.55
33.8
21.4
EOF

# === solve block: phonon_undoped.txt ===
cat > "$OUTDIR/phonon_undoped.txt" <<'EOF'
mode_label,symmetry,frequency_TO,frequency_LO
1-2,E_u,72,93
3-4,E_g,82,
5,A_2u,105,144
6,A_1g,120,
7-8,E_g,152,
9,A_1g,172,
10-11,E_u,210,240
12-13,E_g,232,
14,B_1g,341,
15-16,E_u,424,614
17,A_2u,468,492
18-19,E_g,623,
20,A_2u,641,751
21,A_1g,717,
EOF

# === solve block: phonon_doped.txt ===
cat > "$OUTDIR/phonon_doped.txt" <<'EOF'
mode_label,frequency
1-2,76
3-4,94
5,144
6,136
7-8,148
9,175
10-11,210
12-13,283
14,328
15-16,475
17,457
18-19,651
20,596
21,646
EOF
