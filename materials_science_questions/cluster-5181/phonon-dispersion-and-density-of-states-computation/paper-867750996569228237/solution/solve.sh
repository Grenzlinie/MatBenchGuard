#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gap_pristine_RbH.txt ===
cat > "$OUTDIR/band_gap_pristine_RbH.txt" <<'EOF'
2.62
EOF

# === solve block: N0_vs_x.csv ===
cat > "$OUTDIR/N0_vs_x.csv" <<'EOF'
x,N0
0.05,0.06
0.20,0.10
0.45,0.18
EOF

# === solve block: lambda_vs_x.csv ===
cat > "$OUTDIR/lambda_vs_x.csv" <<'EOF'
x,lambda
0.05,0.3
0.20,0.8
0.45,1.92
EOF

# === solve block: Tc_at_x045.txt ===
cat > "$OUTDIR/Tc_at_x045.txt" <<'EOF'
51.3 66.1
EOF

# === solve finalize ===
# No post-processing needed
