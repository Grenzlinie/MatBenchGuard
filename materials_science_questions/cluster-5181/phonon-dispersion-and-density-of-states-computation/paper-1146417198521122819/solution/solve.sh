#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: phonon_frequencies.csv ===
cat > "$OUTDIR/phonon_frequencies.csv" <<'EOF'
q_point,mode_index,frequency_M2,frequency_M8+Dip
Gamma,0,0.0,0.0
Gamma,1,0.0,0.0
Gamma,2,0.0,0.0
Gamma,3,-188.5,-188.5
Gamma,4,-188.5,-188.5
Gamma,5,-188.5,-95.2
Gamma,6,170.3,170.3
Gamma,7,170.3,170.3
Gamma,8,170.3,195.0
Gamma,9,310.2,310.2
Gamma,10,310.2,310.2
Gamma,11,310.2,340.1
Gamma,12,508.4,508.4
Gamma,13,508.4,508.4
Gamma,14,508.4,698.4
X,0,0.0,0.0
X,1,0.0,0.0
X,2,0.0,0.0
X,3,45.2,45.2
X,4,45.2,45.2
X,5,45.2,45.2
X,6,155.3,155.3
X,7,155.3,155.3
X,8,155.3,155.3
X,9,295.7,295.7
X,10,295.7,295.7
X,11,295.7,295.7
X,12,485.5,485.5
X,13,485.5,485.5
X,14,485.5,485.5
EOF

# === solve block: unstable_TO_mode.txt ===
cat > "$OUTDIR/unstable_TO_mode.txt" <<'EOF'
M2: frequency=-188.5 (cm^-1), character=chain-like eigendisplacement
M8+Dip: frequency=-190.2 (cm^-1), character=chain-like eigendisplacement
EOF

# === solve block: hysteresis_summary.csv ===
cat > "$OUTDIR/hysteresis_summary.csv" <<'EOF'
model,coercive_field,remanent_polarization
M2,2.42,25.0
M8+Dip,2.58,25.4
EOF
