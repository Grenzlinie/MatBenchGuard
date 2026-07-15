#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table5_barriers.csv ===
cat > "$OUTDIR/table5_barriers.csv" << 'EOF'
silicate,barrier_with_DMF,barrier_without_DMF,reaction_free_energy_with_DMF,reaction_free_energy_without_DMF
primary_alkyl,17.45,28.88,1.86,13.78
I·Cy,13.23,,7.77,
I·Cy·CN,10.51,,2.03,
I·Cy·OMe,37.73,,17.45,
I·Ph,27.46,36.49,22.61,25.98
I·Ph·CN,18.99,34.89,19.05,25.57
I·Ph·OMe,32.53,43.00,29.16,28.03
EOF

# === solve block: cis_trans_gaps.json ===
cat > "$OUTDIR/cis_trans_gaps.json" << 'EOF'
{
  "1b": {
    "gap": 3.3,
    "cis_energy": 0.0,
    "trans_energy": 3.3
  },
  "1h": {
    "gap": -0.6,
    "cis_energy": 0.6,
    "trans_energy": 0.0
  }
}
EOF

# === solve block: somo_homo.json ===
cat > "$OUTDIR/somo_homo.json" << 'EOF'
{
  "II_Ph": {
    "HOMO_energy": -7.72,
    "SOMO_energy": -8.63
  },
  "II_Ph_CN": {
    "HOMO_energy": -7.74,
    "SOMO_energy": -9.10
  }
}
EOF
