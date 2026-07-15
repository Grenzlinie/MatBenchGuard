#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: beta_phonon_frequencies.csv ===
cat > /app/outputs/beta_phonon_frequencies.csv <<'FFEOF'
mode_id,computed_frequency,symmetry
1,106,E2g
2,108,Ag
3,129,E1g
4,275,E2g
5,309,Ag
6,373,E2g
7,443,Ag
8,721,E1g
9,781,Ag
10,791,E2g
11,878,E2g
FFEOF

# === solve block: gamma_phonon_frequencies.csv ===
cat > /app/outputs/gamma_phonon_frequencies.csv <<'FFEOF'
mode_id,computed_frequency,symmetry
1,245,T2g
2,467,Eg
3,576,T2g
4,710,T2g
5,830,A1g
FFEOF
