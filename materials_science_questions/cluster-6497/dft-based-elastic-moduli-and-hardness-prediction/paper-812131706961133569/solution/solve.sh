#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: structural_params.json ===
cat > $OUTDIR/structural_params.json <<'EOF'
{
  "rutile_GGA": {"a": 4.825, "c": 3.245, "u": 0.3065},
  "rutile_LDA": {"a": 4.580, "c": 3.080, "u": 0.3044},
  "CaCl2_GGA": {"a": 4.855, "b": 4.737, "c": 3.258, "u": 0.3273, "v": 0.2853},
  "CaCl2_LDA": {"a": 4.506, "b": 4.371, "c": 3.020, "u": 0.3170, "v": 0.2750},
  "cubic_GGA": {"a": 5.079, "u": 0.3460},
  "cubic_LDA": {"a": 5.872, "u": 0.3420}
}
EOF

# === solve block: transition_pressures.json ===
cat > $OUTDIR/transition_pressures.json <<'EOF'
{
  "GGA": {"rutile_cacl2": 12.4, "cacl2_cubic": 22.1},
  "LDA": {"rutile_cacl2": 10.1, "cacl2_cubic": 18.3}
}
EOF
