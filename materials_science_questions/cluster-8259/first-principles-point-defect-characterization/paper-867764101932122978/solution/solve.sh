#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: formation_energies.json ===
cat > "$OUTDIR/formation_energies.json" <<'EOF'
{
  "(001)-site1-q0": 5.1378,
  "(001)-site1-q1+": 5.3593,
  "(001)-site1-q2+": 5.9628,
  "(001)-site2-q0": 5.2306,
  "(001)-site2-q1+": 5.3537,
  "(001)-site2-q2+": 5.9717,
  "(001)-subsurface-q0": 5.5779,
  "(001)-subsurface-q1+": 5.5137,
  "(001)-subsurface-q2+": 2.7874,
  "(100)-bridge-q0": 5.2099,
  "(100)-bridge-q1+": 3.6295,
  "(100)-bridge-q2+": 3.6239,
  "(100)-metastable-ring-q0": 5.3224,
  "(100)-metastable-ring-q1+": 3.1666,
  "(100)-metastable-ring-q2+": 1.2963,
  "(100)-ring-2III-O-q0": 3.4193,
  "(100)-ring-2III-O-q1+": 0.6417,
  "(100)-ring-2III-O-q2+": -1.1842
}
EOF

# === solve block: magnetic_states.json ===
cat > "$OUTDIR/magnetic_states.json" <<'EOF'
{
  "(001)-site1-q0": false,
  "(001)-site1-q1+": true,
  "(001)-site1-q2+": true,
  "(001)-site2-q0": false,
  "(001)-site2-q1+": true,
  "(001)-site2-q2+": true,
  "(001)-subsurface-q0": false,
  "(001)-subsurface-q1+": true,
  "(001)-subsurface-q2+": false,
  "(100)-bridge-q0": false,
  "(100)-bridge-q1+": true,
  "(100)-bridge-q2+": true,
  "(100)-metastable-ring-q0": false,
  "(100)-metastable-ring-q1+": true,
  "(100)-metastable-ring-q2+": false,
  "(100)-ring-2III-O-q0": false,
  "(100)-ring-2III-O-q1+": true,
  "(100)-ring-2III-O-q2+": false
}
EOF
