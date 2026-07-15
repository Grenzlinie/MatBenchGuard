#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_vibrational_frequencies.json ===
cat > /app/outputs/step_01_vibrational_frequencies.json << 'EOF'
[
  {"mode": "v(O-H)", "frequency": 3767.6, "intensity": 87, "symmetry": "a'"},
  {"mode": "v_as(CH2)", "frequency": 3174.4, "intensity": 0.6, "symmetry": "a''"},
  {"mode": "v_s(CH2)", "frequency": 3074.3, "intensity": 5, "symmetry": "a'"},
  {"mode": "δ(CH2)", "frequency": 1329.6, "intensity": 5, "symmetry": "a'"},
  {"mode": "v_s(ReO2)", "frequency": 1014.8, "intensity": 30, "symmetry": "a'"},
  {"mode": "v_as(ReO2)", "frequency": 993.0, "intensity": 81, "symmetry": "a''"},
  {"mode": "δ(Re-O-H) + ρ(CH2) + v(Re=C)", "frequency": 837.2, "intensity": 8, "symmetry": "a'"},
  {"mode": "δ(Re-O-H) + ρ(CH2) + v(Re=C)", "frequency": 813.1, "intensity": 10, "symmetry": "a'"},
  {"mode": "δ(Re-O-H) + ρ(CH2) + v(Re=C)", "frequency": 761.7, "intensity": 73, "symmetry": "a'"},
  {"mode": "v(Re-OH)", "frequency": 681.9, "intensity": 100, "symmetry": "a'"},
  {"mode": "CH2 scissor", "frequency": 661.4, "intensity": 1, "symmetry": "a''"},
  {"mode": "CH2 wag", "frequency": 540.5, "intensity": 0.2, "symmetry": "a''"},
  {"mode": "δ(Re-O-H)", "frequency": 324.3, "intensity": 42, "symmetry": "a''"}
]
EOF
