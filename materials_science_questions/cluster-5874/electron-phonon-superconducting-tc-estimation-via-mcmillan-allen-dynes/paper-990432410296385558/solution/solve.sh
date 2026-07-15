#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'FFEOF'
{
  "C11": 570.0,
  "C22": 322.0,
  "C12": 22.0,
  "C44": 146.0,
  "Ya": 569.4,
  "Yb": 321.4
}
FFEOF

# === solve block: tc_zero_strain.json ===
cat > "$OUTDIR/tc_zero_strain.json" <<'FFEOF'
{
  "Tc_anisotropic_ME": 20.0
}
FFEOF

# === solve block: tc_thirteen_strain.json ===
cat > "$OUTDIR/tc_thirteen_strain.json" <<'FFEOF'
{
  "Tc_anisotropic_ME": 46.0
}
FFEOF
