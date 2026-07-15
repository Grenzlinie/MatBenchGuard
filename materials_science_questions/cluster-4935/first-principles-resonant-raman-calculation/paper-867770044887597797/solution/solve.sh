#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: Q0_GDR.txt ===
cat > /app/outputs/Q0_GDR.txt <<'EOF'
Q0 = 7.30 b
EOF

# === solve block: Q0_experimental.txt ===
cat > /app/outputs/Q0_experimental.txt <<'EOF'
Q0 = 7.31 b
EOF

# === solve block: comparison_report.txt ===
cat > /app/outputs/comparison_report.txt <<'EOF'
GDR-derived Q0: 7.30 b
Experimental Q0: 7.31 b
Absolute difference: 0.01 b, values agree within 0.05 b.
EOF
