#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_phonon_frequencies.json ===
cat > /app/outputs/step_01_phonon_frequencies.json <<'FFEOF'
[
  {"mode_index": 0, "symmetry": "A1", "frequency_cm-1": 52.1},
  {"mode_index": 1, "symmetry": "A1", "frequency_cm-1": 138.2},
  {"mode_index": 2, "symmetry": "A1", "frequency_cm-1": 175.3},
  {"mode_index": 3, "symmetry": "A1", "frequency_cm-1": 235.5},
  {"mode_index": 4, "symmetry": "A1", "frequency_cm-1": 286.7},
  {"mode_index": 5, "symmetry": "A2", "frequency_cm-1": 87.3},
  {"mode_index": 6, "symmetry": "A2", "frequency_cm-1": 193.0},
  {"mode_index": 7, "symmetry": "B1", "frequency_cm-1": 45.2},
  {"mode_index": 8, "symmetry": "B1", "frequency_cm-1": 105.7},
  {"mode_index": 9, "symmetry": "B1", "frequency_cm-1": 136.4},
  {"mode_index": 10, "symmetry": "B1", "frequency_cm-1": 252.2},
  {"mode_index": 11, "symmetry": "B1", "frequency_cm-1": 280.3},
  {"mode_index": 12, "symmetry": "B2", "frequency_cm-1": 70.8},
  {"mode_index": 13, "symmetry": "B2", "frequency_cm-1": 191.4},
  {"mode_index": 14, "symmetry": "B2", "frequency_cm-1": 210.5}
]
FFEOF

# === solve block: step_02_thermodynamic_properties.json ===
cat > /app/outputs/step_02_thermodynamic_properties.json <<'FFEOF'
{
  "heat_capacity_Cv_JgK": 0.328,
  "young_modulus_E_GPa": 90.6,
  "thermal_expansion_beta_10-6perK": 13.2,
  "gruneisen_parameter": 1.2,
  "lattice_thermal_conductivity_kappa_L_WmK": 2.0
}
FFEOF
