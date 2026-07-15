#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: poisson_ratio.json ===
cat > "$OUTDIR/poisson_ratio.json" <<'FFEOF'
{
  "nu": 0.2704,
  "B_H": 323.3,
  "G_H": 175.3
}
FFEOF

# === solve block: alpha_V_avg.txt ===
cat > "$OUTDIR/alpha_V_avg.txt" <<'FFEOF'
24.86
FFEOF

# === solve block: thermal_properties.csv ===
cat > "$OUTDIR/thermal_properties.csv" <<'FFEOF'
T(K),alpha(10⁻⁶ K⁻¹),C_V(J/mol-K)
300,18.5,45.0
500,32.0,68.0
1000,42.0,74.5
1500,46.0,74.8
2000,48.5,74.9
FFEOF
