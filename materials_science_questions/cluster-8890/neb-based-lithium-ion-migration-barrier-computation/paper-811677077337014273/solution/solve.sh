#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_parameters.json ===
cat > /app/outputs/lattice_parameters.json <<'EOF'
{
  "li2co3": {
    "a": 8.370,
    "b": 4.929,
    "c": 5.870,
    "beta_deg": 117.10
  },
  "li2o": {
    "a": 4.503
  },
  "lif": {
    "a": 3.910
  }
}
EOF

# === solve block: electronic_properties.json ===
cat > /app/outputs/electronic_properties.json <<'EOF'
{
  "li2co3": {
    "vb_width_eV": 2.6,
    "band_gap_eV": 4.7
  },
  "li2o": {
    "vb_width_eV": 3.0,
    "band_gap_eV": 4.7
  },
  "lif": {
    "vb_width_eV": 3.6,
    "band_gap_eV": 8.9
  }
}
EOF

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'EOF'
{
  "li2co3": {
    "min_barrier_eV": 0.227,
    "max_barrier_eV": 0.491
  },
  "li2o": {
    "path3_barrier_eV": 0.152
  },
  "lif": {
    "barrier_eV": 0.729
  }
}
EOF
