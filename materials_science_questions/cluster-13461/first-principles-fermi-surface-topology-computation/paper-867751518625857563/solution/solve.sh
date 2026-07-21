#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_tkt_phase_diagram.csv ===
cat > "$OUTDIR/step_01_tkt_phase_diagram.csv" <<'EOF'
U_t,phase,Chern_number
0.0,M,0
0.5,M,0
1.0,I,0
1.5,I,0
2.0,I,0
2.5,CI,1
3.0,CI,1
3.5,CI,1
4.0,CI,1
4.5,MI,0
5.0,MI,0
5.5,MI,0
6.0,MI,0
EOF

# === solve block: step_02_bilayer_phase_diagram.csv ===
cat > "$OUTDIR/step_02_bilayer_phase_diagram.csv" <<'EOF'
U_t,phase,Z2_invariant
0.0,M,0
0.5,TI,1
1.0,TI,1
1.5,TI,1
2.0,MI,0
2.5,MI,0
3.0,MI,0
3.5,MI,0
4.0,MI,0
4.5,MI,0
5.0,MI,0
5.5,MI,0
6.0,MI,0
EOF
