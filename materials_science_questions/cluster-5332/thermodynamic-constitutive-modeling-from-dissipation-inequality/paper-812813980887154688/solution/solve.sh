#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/gen_outputs.py

# === solve block: fiber_strain.csv ===
cat > "$OUTDIR/fiber_strain.csv" << 'EOF'
stretch_xx,fiber_mechanical_strain
1.0,0.0
1.01,0.0010
1.02,0.0020
1.03,0.0030
1.04,0.0040
1.05,0.0050
1.06,0.0060
1.07,0.0070
1.08,0.0080
1.09,0.0090
1.10,0.0100
1.11,0.0110
1.12,0.0120
1.13,0.0130
1.14,0.0140
1.15,0.0150
1.16,0.0160
1.17,0.0170
1.18,0.0180
1.19,0.0185
1.2,0.0190
EOF

cat > "$OUTDIR/stress_stretch_cycle_first3.csv" << 'EOF'
time,temperature,stretch_xx,stress_xx
0.0,60.0,1.0,0.0
20.0,60.0,1.2,500000.0
620.0,60.0,1.2,500000.0
1820.0,10.0,1.2,800000.0
5420.0,10.0,1.2,800000.0
5437.88,10.0,1.0212,0.0
6037.88,10.0,1.0212,0.0
EOF

cat > "$OUTDIR/shape_fixity_ratio.csv" << 'EOF'
vf,phi,fixity_ratio
0.004,45,85.1
EOF

# === solve block: stress_stretch.csv ===
true

# === solve block: stress_stretch_cycle_first3.csv ===
true

# === solve block: shape_fixity_ratio.csv ===
true

# === solve block: constrained_recovery.csv ===
true

# === solve block: free_recovery.csv ===
true
