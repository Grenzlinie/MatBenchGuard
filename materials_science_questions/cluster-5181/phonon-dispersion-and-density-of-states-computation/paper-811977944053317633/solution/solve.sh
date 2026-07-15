#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: model4_parameters.json ===
cat > "$OUTDIR/model4_parameters.json" <<'EOF'
{
  "A12": 11.56,
  "B12": -1.16,
  "A11": 0.78,
  "B11": -0.29,
  "A22": -0.38,
  "B22": 0.16,
  "Z": 0.946,
  "alpha1": 2.48,
  "alpha2": 0.46,
  "d1": -0.052,
  "d2": 0.054,
  "chi_squared": 5.42
}
EOF

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'EOF'
{
  "C11": 5.24,
  "C12": 1.37,
  "C44": 0.82
}
EOF

# === solve block: dos_histogram.csv ===
python3 /solution/generate_dos.py "$OUTDIR/dos_histogram.csv"
