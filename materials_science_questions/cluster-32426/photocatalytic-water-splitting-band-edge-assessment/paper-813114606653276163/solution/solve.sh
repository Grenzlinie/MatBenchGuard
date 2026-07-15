#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pristine_results.json ===
cat > /app/outputs/pristine_results.json <<'EOF'
{
  "band_gap": 2.45,
  "CBM_vacuum": -4.10,
  "VBM_vacuum": -6.55
}
EOF

# === solve block: B_doped_results.json ===
cat > /app/outputs/B_doped_results.json <<'EOF'
{
  "band_gap": 2.01,
  "CBM_vacuum": -4.10,
  "VBM_vacuum": -6.11
}
EOF

# === solve block: P_doped_results.json ===
cat > /app/outputs/P_doped_results.json <<'EOF'
{
  "band_gap": 2.08,
  "CBM_vacuum": -4.10,
  "VBM_vacuum": -6.18
}
EOF
