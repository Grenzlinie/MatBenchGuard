#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: cubic_instabilities.json ===
cat > "$OUTDIR/cubic_instabilities.json" <<'EOF'
{
  "T1u": {
    "imaginary_frequency_cm-1": 13.92,
    "single_lowering_meV": 0.083,
    "coupled_lowering_meV": 0.105
  },
  "T2g": {
    "single_lowering_meV": 7.014,
    "rotation_angle_deg": 3.2
  }
}
EOF

# === solve block: rhombohedral_instability.json ===
cat > "$OUTDIR/rhombohedral_instability.json" <<'EOF'
{
  "direction": [1, 0, 0],
  "delta": 0.1525,
  "imaginary_frequency_cm-1": 10.0
}
EOF
