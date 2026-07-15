#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dielectric_constants.json ===
cat > "$OUTDIR/dielectric_constants.json" <<'FFEOF'
{
  "100": {
    "tensor": [14.227, -0.053, 0.387, -0.053, 17.722, 0.111, 0.391, 0.111, 17.850],
    "avg_diagonal": 16.600
  },
  "110": {
    "tensor": [25.016, 4.551, -0.140, 4.552, 24.265, -0.629, -0.140, -0.629, 20.936],
    "avg_diagonal": 23.406
  },
  "111": {
    "tensor": [25.700, 2.151, -2.451, 2.152, 25.477, 2.237, -2.449, 2.235, 25.800],
    "avg_diagonal": 25.659
  }
}
FFEOF

# === solve block: polaron_trapping_energies.json ===
cat > "$OUTDIR/polaron_trapping_energies.json" <<'FFEOF'
{
  "100": {"electron": 117, "hole": 7},
  "110": {"electron": 225, "hole": 71},
  "111": {"electron": 151, "hole": 20}
}
FFEOF

# === solve block: rotational_frequencies.json ===
cat > "$OUTDIR/rotational_frequencies.json" <<'FFEOF'
{
  "CH3NH3": 1.0,
  "CH3ND3": 0.85,
  "CD3NH3": 0.85,
  "CD3ND3": 0.76
}
FFEOF

# === solve finalize ===
echo 'All artifacts written.'
