#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: step_01_superspace_group.txt ===
cat > "$OUTDIR/step_01_superspace_group.txt" <<'EOF'
A P2_1/m 1 \overline{1}
EOF

# === solve block: step_02_extinction_rules.csv ===
cat > "$OUTDIR/step_02_extinction_rules.csv" <<'EOF'
reflection,condition,description
main,h even,Main reflections (hkl) vanish unless h is even
satellite,h odd,First-order satellite reflections (hkl±q) vanish unless h is odd
EOF

# === solve block: step_03_modulation_cell.txt ===
cat > "$OUTDIR/step_03_modulation_cell.txt" <<'EOF'
basic modulation cell: a=9.1, b=19.9, c=3.4, gamma=97 degrees
incommensurate modulation cell: a=18.2, b=19.9, c=9.66, gamma=97 degrees, B-centered
EOF
