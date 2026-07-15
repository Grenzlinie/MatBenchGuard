#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'EOF'
{
  "FM": {"C11": 252, "C12": 87, "C13": 152, "C33": 224, "C44": 99, "C66": 69},
  "AFM1": {"C11": 306, "C12": 72, "C13": 141, "C33": 284, "C44": 123, "C66": 69},
  "AFM2": {"C11": 238, "C12": 82, "C13": 155, "C33": 220, "C44": 87, "C66": 48}
}
EOF

# === solve block: magnetoelastic_constants.json ===
cat > "$OUTDIR/magnetoelastic_constants.json" <<'EOF'
{
  "FM": {"b21": 135, "b22": -111, "b3": -40, "b4": -34, "b3p": 86},
  "AFM1": {"b21": 12, "b22": -19, "b3": -37, "b4": 1, "b3p": 47},
  "AFM2": {"b21": -62, "b22": 23, "b3": 118, "b4": 26, "b3p": 75}
}
EOF

# === solve block: polycrystalline_parameters.json ===
cat > "$OUTDIR/polycrystalline_parameters.json" <<'EOF'
{
  "FM": {"xi": -68, "eta": 558},
  "AFM1": {"xi": 7, "eta": -7},
  "AFM2": {"xi": 130, "eta": -623}
}
EOF
