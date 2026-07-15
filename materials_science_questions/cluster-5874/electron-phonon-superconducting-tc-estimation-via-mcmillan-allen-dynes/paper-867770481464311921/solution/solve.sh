#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_formation_energies.txt ===
cat > "$OUTDIR/step_01_formation_energies.txt" <<'EOF'
0.35 -2.99 1.52
EOF

# === solve block: step_02_lattice_constants.txt ===
cat > "$OUTDIR/step_02_lattice_constants.txt" <<'EOF'
8.605 10.705 6.415
EOF

# === solve block: step_03_volume_expansion.txt ===
cat > "$OUTDIR/step_03_volume_expansion.txt" <<'EOF'
26.9
EOF

# === solve block: step_04_tc.txt ===
cat > "$OUTDIR/step_04_tc.txt" <<'EOF'
6.2
EOF
