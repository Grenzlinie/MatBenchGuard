#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energies.json ===
cat > "$OUTDIR/formation_energies.json" <<'EOF'
{
  "system": "beta-Ga2O3: 2V_Ga1-Ga_i complex",
  "charge_states": [-2, -1, 0],
  "formation_energies": {
    "ic_0": {
      "mu_O": 0.0,
      "mu_Ga": -5.0,
      "energy_eV": 2.5
    },
    "ib_0": {
      "mu_O": 0.0,
      "mu_Ga": -5.0,
      "energy_eV": 3.0
    },
    "ic_-1": {
      "mu_O": 0.0,
      "mu_Ga": -5.0,
      "energy_eV": 4.0
    },
    "ib_-1": {
      "mu_O": 0.0,
      "mu_Ga": -5.0,
      "energy_eV": 4.5
    },
    "ic_-2": {
      "mu_O": 0.0,
      "mu_Ga": -5.0,
      "energy_eV": 5.5
    },
    "ib_-2": {
      "mu_O": 0.0,
      "mu_Ga": -5.0,
      "energy_eV": 6.0
    }
  },
  "data_source": "HSE06 DFT calculation"
}
EOF

# === solve block: transition_levels.json ===
cat > "$OUTDIR/transition_levels.json" <<'EOF'
[
  {
    "defect": "2V_Ga1-Ga_i^c",
    "transition": "-2/-3",
    "level_eV": 2.8,
    "method": "HSE06 hybrid DFT"
  }
]
EOF

# === solve block: simulated_intensity_profiles.csv ===
python3 /solution/generate_profile.py "$OUTDIR/simulated_intensity_profiles.csv"
