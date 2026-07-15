#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: zt_elec_results.json ===
cat > "$OUTDIR/zt_elec_results.json" <<'EOF'
{
  "SnSe_hBN": {
    "100": 0.985,
    "200": 0.966,
    "300": 0.950,
    "400": 0.933,
    "500": 0.912,
    "600": 0.888,
    "700": 0.861,
    "800": 0.832,
    "900": 0.802,
    "1000": 0.773
  },
  "SnSe_CsPbI3": {
    "100": 0.991,
    "200": 0.980,
    "300": 0.961,
    "400": 0.944,
    "500": 0.930,
    "600": 0.913,
    "700": 0.889,
    "800": 0.876,
    "900": 0.865,
    "1000": 0.854
  },
  "layered_CsPbI3": {
    "3-layer": {
      "150": 2.5
    },
    "4-layer": {
      "150": 2.49
    }
  }
}
EOF
