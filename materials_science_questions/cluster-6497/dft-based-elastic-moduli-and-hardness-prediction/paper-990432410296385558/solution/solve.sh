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
  "C11": 570.0,
  "C22": 322.0,
  "C12": 22.0,
  "C44": 146.0
}
EOF

# === solve block: young_moduli.json ===
cat > "$OUTDIR/young_moduli.json" <<'EOF'
{
  "Ya": 569.4,
  "Yb": 321.4
}
EOF

# === solve block: superconducting_tc.json ===
cat > "$OUTDIR/superconducting_tc.json" <<'EOF'
{
  "Tc_unstrained": 20.0,
  "Tc_strained_13_percent": 46.0
}
EOF
