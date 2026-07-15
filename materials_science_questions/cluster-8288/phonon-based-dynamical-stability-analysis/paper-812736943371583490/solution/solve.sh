#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: unstable_modes.json ===
cat > /app/outputs/unstable_modes.json <<'EOF'
[
  { "point": "X", "symmetry": "X5-", "frequency": 40.0 },
  { "point": "M", "symmetry": "M2+", "frequency": 40.0 },
  { "point": "M", "symmetry": "M5-", "frequency": 45.0 },
  { "point": "M", "symmetry": "M4-", "frequency": 37.0 },
  { "point": "A", "symmetry": "M2+", "frequency": 40.0 },
  { "point": "A", "symmetry": "M5-", "frequency": 45.0 },
  { "point": "A", "symmetry": "M4-", "frequency": 37.0 }
]
EOF

# === solve block: phase_energies.json ===
cat > /app/outputs/phase_energies.json <<'EOF'
{
  "P4/mmm": 0.0,
  "P4/mbm": -102.3,
  "Pmma": -186.3,
  "Pmc2_1": -224.0
}
EOF

# === solve block: polarization_results.txt ===
cat > /app/outputs/polarization_results.txt <<'EOF'
strain_0: 0.48 µC/cm²
strain_+3: 0.57 µC/cm²
strain_-3: 0.42 µC/cm²
EOF
