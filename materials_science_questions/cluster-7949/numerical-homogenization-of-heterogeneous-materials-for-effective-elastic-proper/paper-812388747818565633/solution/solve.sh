#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: effective_modulus.csv ===
cat > "$OUTDIR/effective_modulus.csv" <<'EOF'
concentration,shear_modulus_GPa
0.15,2.03
0.30,2.83
0.45,3.78
0.60,4.82
EOF

# === solve block: stress_concentration_f2.csv ===
python3 /solution/gen_stress.py "$OUTDIR"
