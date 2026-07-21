#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pmf_minima.csv ===
cat > "$OUTDIR/pmf_minima.csv" <<'EOF'
system,configuration,D_PMF,D_force
Au_Au,trilayer,11.3,12.2
Au_Au,bilayer,8.0,8.6
Au_Au,monolayer,5.3,6.1
Au_C,bilayer,8.9,9.4
Au_C,monolayer,6.1,7.1
Au_C,contact,2.9,3.1
C_Au,bilayer,8.6,9.1
C_Au,monolayer,5.5,6.0
C_C,bilayer,9.8,10.8
C_C,contact,3.2,3.7
EOF

# === solve block: force_amplitudes.csv ===
cat > "$OUTDIR/force_amplitudes.csv" <<'EOF'
system,configuration,amplitude_pN
Au_Au,trilayer,241
Au_Au,bilayer,2258
Au_Au,monolayer,4262
Au_C,bilayer,539
Au_C,monolayer,2080
Au_C,contact,1797
C_Au,bilayer,348
C_Au,monolayer,528
C_C,bilayer,115
C_C,contact,779
EOF

# === solve block: oscillation_periods.csv ===
cat > "$OUTDIR/oscillation_periods.csv" <<'EOF'
system,transition,period_PMF,period_force
Au_Au,trilayer_to_bilayer,3.3,3.6
Au_Au,bilayer_to_monolayer,2.7,2.5
Au_C,bilayer_to_monolayer,2.8,2.4
Au_C,monolayer_to_contact,3.1,4.0
C_Au,bilayer_to_monolayer,3.1,3.1
EOF

# === solve block: orientation_peak.csv ===
cat > "$OUTDIR/orientation_peak.csv" <<'EOF'
system,D_Angstrom,peak_cosθ
Au_Au,6.0,-0.1
EOF
