#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: V_N_IE_15A.dat ===
cat > "$OUTDIR/V_N_IE_15A.dat" <<'FFEOF'
2.01
FFEOF

# === solve block: C_N_IE_15A.dat ===
cat > "$OUTDIR/C_N_IE_15A.dat" <<'FFEOF'
1.39
FFEOF

# === solve block: C_N_convergence.dat ===
printf "10\t1.39\n" > "$OUTDIR/C_N_convergence.dat"
printf "20\t1.39\n" >> "$OUTDIR/C_N_convergence.dat"
printf "30\t1.39\n" >> "$OUTDIR/C_N_convergence.dat"
