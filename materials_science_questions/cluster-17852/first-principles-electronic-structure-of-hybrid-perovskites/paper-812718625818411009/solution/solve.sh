#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: builtin_potentials.json ===
cat > "$OUTDIR/builtin_potentials.json" <<'FFEOF'
[
  {
    "interface": "PbI/titania",
    "builtin_potential_eV": 0.29
  },
  {
    "interface": "MAI/titania",
    "builtin_potential_eV": -0.50
  },
  {
    "interface": "MAIdep/titania",
    "builtin_potential_eV": -0.28
  }
]
FFEOF

# === solve block: interface_band_gaps.json ===
cat > "$OUTDIR/interface_band_gaps.json" <<'FFEOF'
[
  {
    "interface": "PbI/titania",
    "band_gap_eV": 1.5
  },
  {
    "interface": "MAI/titania",
    "band_gap_eV": 1.9
  },
  {
    "interface": "MAIdep/titania",
    "band_gap_eV": 1.7
  }
]
FFEOF

# === solve block: driving_force_ranking.json ===
cat > "$OUTDIR/driving_force_ranking.json" <<'FFEOF'
{
  "ranking": [
    "PbI/titania",
    "MAIdep/titania",
    "MAI/titania"
  ]
}
FFEOF
