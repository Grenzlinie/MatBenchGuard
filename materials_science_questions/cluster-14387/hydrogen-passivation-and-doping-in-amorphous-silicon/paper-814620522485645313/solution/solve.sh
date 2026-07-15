#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_si_gap.txt ===
echo '0.55' > "$OUTDIR/bulk_si_gap.txt"

# === solve block: qd_gaps.csv ===
cat > "$OUTDIR/qd_gaps.csv" <<'EOF'
qd_name,diameter_nm,raw_gap_eV,corrected_gap_eV
QD_0.6nm,0.6,1.72,2.3
QD_1.0nm,1.0,1.22,1.8
QD_1.9nm,1.9,0.72,1.3
EOF
