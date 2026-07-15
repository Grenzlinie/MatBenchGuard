#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap.txt ===
cat > "$OUTDIR/band_gap.txt" <<'EOF'
0.85
EOF

# === solve block: surface_potential.txt ===
cat > "$OUTDIR/surface_potential.txt" <<'EOF'
10.0
EOF

# === solve block: optical_peak.txt ===
cat > "$OUTDIR/optical_peak.txt" <<'EOF'
1.25
EOF

# === solve block: energy_alignment.txt ===
cat > "$OUTDIR/energy_alignment.txt" <<'EOF'
-6.50
-3.85
EOF
