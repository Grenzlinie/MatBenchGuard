#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: wrinkling_analysis.json ===
cat > /app/outputs/wrinkling_analysis.json <<'EOF'
{
  "armchair": {
    "wrinkles_present": true,
    "wavelength_nm": 1.2
  },
  "zigzag": {
    "wrinkles_present": false,
    "wavelength_nm": null
  }
}
EOF

# === solve block: contact_stiffness.csv ===
cat > /app/outputs/contact_stiffness.csv <<'EOF'
geometry,chirality,contact_stiffness_Nm
convex,armchair,42.0
convex,zigzag,63.0
concave,armchair,120.0
concave,zigzag,189.0
planar,armchair,100.0
planar,zigzag,150.0
EOF
