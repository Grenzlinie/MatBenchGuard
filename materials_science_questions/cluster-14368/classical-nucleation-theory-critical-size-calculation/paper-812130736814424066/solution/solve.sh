#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: supersaturation.json ===
cat > "$OUTDIR/supersaturation.json" <<'EOF'
{
  "delta0": 0.1
}
EOF

# === solve block: max_radius.json ===
cat > "$OUTDIR/max_radius.json" <<'EOF'
{
  "a0_microns": 0.38
}
EOF

# === solve block: growth_time.json ===
cat > "$OUTDIR/growth_time.json" <<'EOF'
{
  "t_90_microsec": 123.0
}
EOF
