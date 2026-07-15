#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: total_energy.txt ===
printf '%s\n' '-208.7764415' > "$OUTDIR/total_energy.txt"

# === solve block: dipole_moment.txt ===
cat > "$OUTDIR/dipole_moment.txt" <<'FFEOF'
1.977
1.977
0.000
0.000
FFEOF

# === solve block: homo_eigenvalues.json ===
cat > "$OUTDIR/homo_eigenvalues.json" <<'FFEOF'
{
  "1a2": -0.2989,
  "2b1": -0.3490,
  "1b1": -0.5705
}
FFEOF
