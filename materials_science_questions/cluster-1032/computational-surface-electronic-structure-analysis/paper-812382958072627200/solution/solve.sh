#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: work_function.txt ===
cat > "$OUTDIR/work_function.txt" <<'WORKEOF'
3.38
WORKEOF

# === solve block: dos_shifts.csv ===
cat > "$OUTDIR/dos_shifts.csv" <<'SHIFTEOF'
maxima,shift_eV
I,0.1
II,0.15
III,0.98
SHIFTEOF

# === solve block: occupied_surface_states.csv ===
cat > "$OUTDIR/occupied_surface_states.csv" <<'OCCEOF'
feature,q,energy
a1,0.01,0.0
a1,0.03,0.0
a2,0.01,-0.48
a2,0.03,-0.46
a3,0.01,-0.89
a3,0.03,-0.81
a4,0.01,-1.29
a4,0.03,-1.31
a5,0.01,-2.46
a5,0.03,-2.44
OCCEOF

# === solve block: unoccupied_surface_states.csv ===
cat > "$OUTDIR/unoccupied_surface_states.csv" <<'UNOCCEOF'
feature,q,energy
b1,0.01,0.43
b1,0.03,0.51
b2,0.01,0.92
b2,0.03,0.91
b3,0.01,1.88
b3,0.03,1.87
b4,0.01,2.16
b4,0.03,2.14
UNOCCEOF
