#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: eos_parameters.json ===
cat > "$OUTDIR/eos_parameters.json" <<'FFEOF'
{
  "KZnF3": {
    "a0": 4.0589,
    "B0": 77.214,
    "Bprime": 4.371
  },
  "AgZnF3": {
    "a0": 3.9937,
    "B0": 92.412,
    "Bprime": 4.956
  }
}
FFEOF

# === solve block: cv_300K.json ===
cat > "$OUTDIR/cv_300K.json" <<'FFEOF'
{
  "KZnF3": {
    "Cv_300": 111.843
  },
  "AgZnF3": {
    "Cv_300": 114.0335
  }
}
FFEOF
