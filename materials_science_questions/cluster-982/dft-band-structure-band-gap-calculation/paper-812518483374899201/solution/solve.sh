#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'EOF'
{
  "pbe": 2.547,
  "mbj": 3.415,
  "pbe_u": 2.549,
  "mbj_u_so": 2.431
}
EOF

# === solve block: static_dielectric.json ===
cat > "$OUTDIR/static_dielectric.json" <<'EOF'
{
  "xx": 5.522,
  "yy": 5.530,
  "zz": 5.688
}
EOF
