#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: eu_assignment.csv ===
cat > "$OUTDIR/eu_assignment.csv" <<'FFEOF'
label,wavenumber,assignment
1,19597,T2g(5D2)->A2g(7F3)
2,19429,T2g(5D2)->T2g(7F3)
3,19365,T2g(5D2)->T1g(7F3)
4,18997,T1g(5D1)->A1g(7F0)
5,18191,T1g(5D1)->Eg(7F2)
6,17926,T1g(5D1)->T2g(7F2)
7,16917,A1g(5D0)->T1g(7F1)
8,15233,A1g(5D0)->T1g(7F3)
9,14109,A1g(5D0)->T1g(7F4)
FFEOF

# === solve block: b4_value.txt ===
cat > "$OUTDIR/b4_value.txt" <<'FFEOF'
209
FFEOF

# === solve block: phonon_energies.csv ===
cat > "$OUTDIR/phonon_energies.csv" <<'FFEOF'
mode,energy_cm1
S6(t1u),372
S7(t1u),174
S8(t1u),139
S10(t2u),99
FFEOF

# === solve block: tb_assignment.csv ===
cat > "$OUTDIR/tb_assignment.csv" <<'FFEOF'
label,wavenumber,assignment
3,18060.0,Eg->T1gb
4,18091.0,T1g->Eg
5,18119.5,T2g->T1gb
6,18173.0,T2g->Eg
7,18173.0,T1g->T2g
8,18200.0,Eg->T2g
10,18471.5,A1g->T1ga
11,18514.5,T1g->T1ga
12,18540.5,Eg->T1ga
A,15594,s. Text
B,15857,s. Text
4,15962,A1g->T1g
5,16003,T1g->T1g
6,16035,Eg->T1g
C,16137,s. Text
D,16256,s. Text
FFEOF
