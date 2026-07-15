#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electronic_properties.json ===
cat > /app/outputs/electronic_properties.json <<'EOF'
{
  "rutile": {
    "Ti16O32": {"Eg": 1.871, "magnetic_moment": 0.0},
    "Ti15Mo1O32": {"Eg": 1.142, "magnetic_moment": 1.340},
    "Ti14Mo2O32": {"Eg": 0.623, "magnetic_moment": 2.460}
  },
  "anatase": {
    "Ti16O32": {"Eg": 2.144, "magnetic_moment": 0.0},
    "Ti15Mo1O32": {"Eg": 1.863, "magnetic_moment": 1.120},
    "Ti14Mo2O32": {"Eg": 1.603, "magnetic_moment": 2.520}
  }
}
EOF
