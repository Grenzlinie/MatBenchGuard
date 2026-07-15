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
  "monoclinic": {
    "a": 6.4211,
    "b": 10.9941,
    "c": 5.047,
    "beta": 90.982
  },
  "orthorhombic": {
    "a": 6.4237,
    "b": 5.3474,
    "c": 4.9369
  }
}
EOF

# === solve block: intrinsic_defect_energies.json ===
cat > /app/outputs/intrinsic_defect_energies.json <<'EOF'
{
  "monoclinic": {
    "Li_Frenkel": 2.55,
    "Mn_Frenkel": 6.41,
    "O_Frenkel": 8.11,
    "Schottky": 34.84,
    "LiMn_antisite": 1.38,
    "Li_deficiency_oxidation": 14.36,
    "oxygen_excess_oxidation": 12.43
  },
  "orthorhombic": {
    "Li_Frenkel": 3.90,
    "Mn_Frenkel": 7.79,
    "O_Frenkel": 11.78,
    "Schottky": 43.73,
    "LiMn_antisite": 1.65,
    "Li_deficiency_oxidation": 16.12,
    "oxygen_excess_oxidation": 14.75
  }
}
EOF

# === solve block: li_migration_energies.json ===
cat > /app/outputs/li_migration_energies.json <<'EOF'
{
  "monoclinic": {
    "path_A": 0.60,
    "path_B": 0.54,
    "path_C": 1.58,
    "path_D": 0.94
  },
  "orthorhombic": {
    "path_X": 0.95,
    "path_Y": 1.29
  }
}
EOF

# === solve block: dopant_incorporation_energies.json ===
cat > /app/outputs/dopant_incorporation_energies.json <<'EOF'
{
  "monoclinic": {
    "Al": {
      "Li_site": 9.60,
      "Mn_site": 4.95,
      "Si_site": 2.70
    },
    "Ga": {
      "Li_site": 11.79,
      "Mn_site": 5.09,
      "Si_site": 3.90
    }
  },
  "orthorhombic": {
    "Al": {
      "Li_site": 9.13,
      "Mn_site": 5.15,
      "Si_site": 3.51
    },
    "Ga": {
      "Li_site": 9.16,
      "Mn_site": 5.10,
      "Si_site": 4.74
    }
  }
}
EOF
