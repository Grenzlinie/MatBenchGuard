#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_heptamer.json ===
cat > "$OUTDIR/step_02_heptamer.json" <<'EOF'
{
  "isolated_site": "V1",
  "heptamer_center": "V2",
  "heptamer_vertices": ["V3", "V3", "V3", "V3", "V3", "V3"]
}
EOF

# === solve block: step_03_integrated_intensities.csv ===
cat > /app/outputs/step_03_integrated_intensities.csv <<'EOF'
V_site,PART_I,PART_II
V1,1.17,2.26
V2,1.30,2.19
V3,1.28,2.19
EOF

# === solve block: step_04_valence_ordering.json ===
cat > /app/outputs/step_04_valence_ordering.json <<'EOF'
{
  "ordering": {
    "V1": "lowest",
    "V2": "highest",
    "V3": "intermediate"
  },
  "c_axis_sequence": ["V1", "V3", "V2", "V3", "V1"]
}
EOF
