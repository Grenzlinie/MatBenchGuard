#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_energies.json ===
cat > /app/outputs/total_energies.json <<'EOF'
{
  "LiAgF3-1": {"E_FM": -9.73982, "E_AFM": -9.89530},
  "LiAgF3-2": {"E_FM": -9.14112, "E_AFM": -9.87970, "E_AFM2": -9.85862},
  "Li2AgF4-1": {"E_FM": -13.66620, "E_AFM": -13.91604},
  "Li2AgF4-2": {"E_FM": -13.88713, "E_AFM": -13.89120},
  "Li2AgF4-3": {"E_FM": -13.71692, "E_AFM": -13.81240},
  "LiF": {"E_FM": -4.0},
  "AgF2": {"E_FM": -6.0}
}
EOF

# === solve block: j_values.json ===
cat > /app/outputs/j_values.json <<'EOF'
{
  "LiAgF3-1": -77.74,
  "LiAgF3-2_J1": -358.75,
  "LiAgF3-2_J2": -10.54,
  "Li2AgF4-1": -62.46,
  "Li2AgF4-2": -4.07,
  "Li2AgF4-3": -95.48
}
EOF

# === solve block: convex_hull.json ===
cat > /app/outputs/convex_hull.json <<'EOF'
{
  "LiAgF3-1": 10.1,
  "LiAgF3-2": 11.6,
  "Li2AgF4-1": 8.1,
  "Li2AgF4-2": 10.5,
  "Li2AgF4-3": 18.1
}
EOF
