#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: sin_optimized.xyz ===
cat > "$OUTDIR/sin_optimized.xyz" <<'FFEOF'
2

Si  0.00000000  0.00000000  0.00000000
N   0.00000000  0.00000000  1.57360000
FFEOF

# === solve block: sin_frequencies.txt ===
cat > "$OUTDIR/sin_frequencies.txt" <<'FFEOF'
1181.19
FFEOF

# === solve block: sin2_optimized.xyz ===
cat > "$OUTDIR/sin2_optimized.xyz" <<'FFEOF'
3

Si  0.00000000  0.00000000  0.00000000
N   0.00000000  0.00000000  1.75590000
N   0.00000000  0.00000000  2.90180000
FFEOF

# === solve block: sin2_frequencies.txt ===
cat > "$OUTDIR/sin2_frequencies.txt" <<'FFEOF'
328.63
515.30
1825.85
FFEOF

# === solve block: si2n_optimized.xyz ===
cat > "$OUTDIR/si2n_optimized.xyz" <<'FFEOF'
3

Si  -1.64000000  0.00000000  0.00000000
N   0.00000000  0.00000000  0.00000000
Si  1.64000000  0.00000000  0.00000000
FFEOF

# === solve block: si2n_frequencies.txt ===
cat > "$OUTDIR/si2n_frequencies.txt" <<'FFEOF'
172.45
615.76
1065.53
FFEOF

# === solve block: benchmark_summary.csv ===
cat > "$OUTDIR/benchmark_summary.csv" <<'FFEOF'
system,r_SiN,r_NN,freq1,freq2,freq3
SiN,1.5736,,1181.19,,
SiN2,1.7559,1.1459,328.63,515.30,1825.85
Si2N,1.6400,,172.45,615.76,1065.53
FFEOF
