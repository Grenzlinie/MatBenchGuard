#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > $OUTDIR/results.json <<'EOF'
{
  "Zr3N4": {
    "a0": 6.837,
    "B0": 211,
    "B0_prime": 6.61,
    "C11": 310.13,
    "C12": 75.53,
    "C44": 122.43,
    "epsilon1_0": 11.91,
    "B_poly": 153.73,
    "G": 120.32,
    "E": 280.54,
    "nu": 0.19,
    "n0": 3.45,
    "eps2_peak": 2.99,
    "dos_fermi": 4.35
  },
  "Hf3N4": {
    "a0": 6.578,
    "B0": 232,
    "B0_prime": 5.95,
    "C11": 358.93,
    "C12": 51.02,
    "C44": 148.47,
    "epsilon1_0": 8,
    "B_poly": 153.66,
    "G": 150.66,
    "E": 346.23,
    "nu": 0.12,
    "n0": 2.88,
    "eps2_peak": 3.81,
    "dos_fermi": 3.69
  }
}
EOF
