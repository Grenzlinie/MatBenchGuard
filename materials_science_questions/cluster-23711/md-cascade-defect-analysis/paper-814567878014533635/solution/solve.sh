#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: primary_defects_table.json ===
cat > "$OUTDIR/primary_defects_table.json" <<'EOF'
{
  "V": 2.26,
  "I": 2.26,
  "V2": 1.62,
  "I2": 1.62
}
EOF

# === solve block: defect_saturation.json ===
cat > "$OUTDIR/defect_saturation.json" <<'EOF'
{
  "VO_saturation_fluence": "4e11",
  "V2O_saturation_fluence": "6e12",
  "V3O_saturation_fluence": "6e12",
  "V2O_max": 1e15,
  "V3O_max": 3.75e14
}
EOF

# === solve block: leakage_current.json ===
cat > "$OUTDIR/leakage_current.json" <<'EOF'
{
  "0": 0.010,
  "1e12": 10.3,
  "1e14": 22.2
}
EOF
