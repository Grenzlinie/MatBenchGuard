#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_energy_ranking.json ===
cat > "$OUTDIR/step_01_energy_ranking.json" <<'EOF'
[
  {"polymorph": "rock_salt", "total_lattice_energy_eV": -39.92},
  {"polymorph": "zinc_blende", "total_lattice_energy_eV": -39.53},
  {"polymorph": "wurtzite", "total_lattice_energy_eV": -39.65}
]
EOF

# === solve block: step_02_lattice_parameters.json ===
cat > "$OUTDIR/step_02_lattice_parameters.json" <<'EOF'
[
  {"polymorph": "rock_salt", "a_nm": 0.4274, "c_nm": null},
  {"polymorph": "zinc_blende", "a_nm": 0.457, "c_nm": null},
  {"polymorph": "wurtzite", "a_nm": 0.322, "c_nm": 0.509}
]
EOF

# === solve block: step_03_dielectric_constants.json ===
cat > "$OUTDIR/step_03_dielectric_constants.json" <<'EOF'
[
  {"polymorph": "rock_salt", "epsilon_0": 12.21, "epsilon_inf": 5.64, "epsilon_0_11": null, "epsilon_0_33": null, "epsilon_inf_11": null, "epsilon_inf_33": null},
  {"polymorph": "zinc_blende", "epsilon_0": 5.89, "epsilon_inf": 3.79, "epsilon_0_11": null, "epsilon_0_33": null, "epsilon_inf_11": null, "epsilon_inf_33": null},
  {"polymorph": "wurtzite", "epsilon_0": null, "epsilon_inf": null, "epsilon_0_11": 5.38, "epsilon_0_33": 7.36, "epsilon_inf_11": 3.62, "epsilon_inf_33": 4.22}
]
EOF
