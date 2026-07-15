#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: structural_properties.json ===
cat > "$OUTDIR/structural_properties.json" <<'EOF'
{
  "KCl": {
    "a0": 6.379,
    "B": 17.104,
    "Bprime": 4.304
  },
  "K0.5Rb0.5Cl": {
    "a0": 6.557,
    "B": 14.1417,
    "Bprime": 5.1972
  }
}
EOF

# === solve block: band_gap.json ===
cat > "$OUTDIR/band_gap.json" <<'EOF'
{
  "KCl": 5.071,
  "K0.5Rb0.5Cl": 4.928,
  "nature": "direct"
}
EOF

# === solve block: optical_properties.json ===
cat > "$OUTDIR/optical_properties.json" <<'EOF'
{
  "KCl": {
    "epsilon1_0": 2.1,
    "n_0": 1.5,
    "epsilon1_peak": {"energy": 7.2, "value": 3.9},
    "epsilon2_peaks": [
      {"energy": 8.0, "value": 2.6},
      {"energy": 10.3, "value": 4.2}
    ],
    "k_peak": {"energy": 10.5, "value": 1.45}
  },
  "K0.5Rb0.5Cl": {
    "epsilon1_0": 2.0,
    "n_0": 1.49,
    "epsilon1_peak": {"energy": 6.5, "value": 3.5},
    "epsilon2_peaks": [
      {"energy": 7.9, "value": 2.3},
      {"energy": 10.1, "value": 3.6}
    ],
    "k_peak": {"energy": 10.2, "value": 1.35}
  }
}
EOF

# === solve block: thermoelectric_properties.json ===
cat > "$OUTDIR/thermoelectric_properties.json" <<'EOF'
{
  "KCl": {
    "Seebeck_50K": 254,
    "Seebeck_800K": 205,
    "conductivity_50K": 1.47e17,
    "conductivity_800K": 1.4e19
  },
  "K0.5Rb0.5Cl": {
    "Seebeck_50K": 700,
    "Seebeck_800K": 192,
    "conductivity_50K": 5.16e14,
    "conductivity_800K": 5.11e18
  }
}
EOF
