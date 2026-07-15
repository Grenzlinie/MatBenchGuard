#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs && OUTDIR=/app/outputs

# === solve block: transition_energies.json ===
cat > "$OUTDIR/transition_energies.json" <<'EOF'
{
  "COF1_primary": 8.61,
  "COF102_site1": 8.93,
  "COF102_site2": 12.78
}
EOF

# === solve block: rotational_barriers.json ===
cat > "$OUTDIR/rotational_barriers.json" <<'EOF'
{
  "COF1_barrier": 41.25,
  "COF102_barrier": 35.18
}
EOF
