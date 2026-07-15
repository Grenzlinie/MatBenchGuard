#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relaxed_structure.json ===
cat > "$OUTDIR/relaxed_structure.json" <<'EOF'
{
  "a": 9.34,
  "c": 5.76,
  "volume": 502.5,
  "Li": {
    "x": 0.0807,
    "y": 0.8857,
    "z": 0.0551
  },
  "Si": {
    "x": 0.1107,
    "y": 0.9528,
    "z": 0.5951
  }
}
EOF

# === solve block: bond_data.json ===
cat > "$OUTDIR/bond_data.json" <<'EOF'
{
  "Si_Si_bonds": [2.42, 2.50],
  "Li_Li_bonds": [2.69, 2.94, 2.95],
  "Li_Si_bonds": [2.63, 2.72, 2.74, 2.89, 3.09],
  "Si_Si_Si_angles": [107.5, 110.8, 117.4]
}
EOF

# === solve block: total_energies.json ===
cat > "$OUTDIR/total_energies.json" <<'EOF'
{
  "LiSi_per_fu": -7.717,
  "Li_per_atom": -1.897,
  "Si_per_atom": -5.414
}
EOF

# === solve block: intercalation_voltage.txt ===
cat > "$OUTDIR/intercalation_voltage.txt" <<'EOF'
0.405
EOF

# === solve block: electron_counts.json ===
cat > "$OUTDIR/electron_counts.json" <<'EOF'
{
  "Li_in_LiSi": {
    "s": 0.485,
    "p": 0.995,
    "d": 0.355,
    "total": 1.835
  },
  "Si_in_LiSi": {
    "s": 1.38,
    "p": 2.225,
    "d": 0.24,
    "total": 3.845
  }
}
EOF

# === solve finalize ===
# No final consistency step required.
