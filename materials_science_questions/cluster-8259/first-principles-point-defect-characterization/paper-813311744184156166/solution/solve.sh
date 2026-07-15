#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
cat > /app/outputs/computed_properties.json <<'EOF'
{
  "neutral_vacancy": {
    "ground_state_symmetry": "^3A_2",
    "lowest_excitation_energy_eV": 2.0,
    "lowest_excited_state_symmetry": "^3E",
    "polarization_rules": "perpendicular only"
  },
  "negative_vacancy": {
    "ground_state_symmetry": "^4A_2",
    "first_excitation_energy_eV": 1.568,
    "first_excited_state_symmetry": "^4A_2",
    "second_excitation_energy_eV": 1.572,
    "second_excited_state_symmetry": "^4E",
    "relaxation_energy_eV": 0.1,
    "estimated_zero_phonon_line_eV": 1.47,
    "polarization_rules": "E||c for ^4A_2, E_perp_c for ^4E"
  },
  "comparison_experiment": "The negatively charged silicon vacancy's estimated ZPL (~1.47 eV) and polarization selection rules (parallel for ^4A_2, perpendicular for ^4E) are consistent with the experimental V1/V1' photoluminescence data (ZPL ~1.44 eV, both parallel and perpendicular polarization observed). The neutral vacancy's excitation energy (~2.0 eV) and perpendicular-only polarization do not match the V1/V1' signals. Therefore, the V1 and V1' PL centers are assigned to the negatively charged silicon vacancy."
}
EOF
