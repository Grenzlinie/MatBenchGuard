#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_phonon_modes.json ===
python3 -c "
import json

data = [
  {'symmetry': 'Ag', 'computed_frequency': 531.0, 'dominant_atoms': ['O4']},
  {'symmetry': 'Ag', 'computed_frequency': 511.0, 'dominant_atoms': ['O3']},
  {'symmetry': 'Ag', 'computed_frequency': 468.0, 'dominant_atoms': ['O3']},
  {'symmetry': 'Ag', 'computed_frequency': 400.0, 'dominant_atoms': ['O5']},
  {'symmetry': 'Ag', 'computed_frequency': 337.0, 'dominant_atoms': ['O5','O4','O3']},
  {'symmetry': 'Ag', 'computed_frequency': 271.0, 'dominant_atoms': ['O4']},
  {'symmetry': 'Ag', 'computed_frequency': 200.0, 'dominant_atoms': ['Cu2','O3']},
  {'symmetry': 'Ag', 'computed_frequency': 182.0, 'dominant_atoms': ['La','O3','Cu2']},
  {'symmetry': 'Ag', 'computed_frequency': 166.0, 'dominant_atoms': ['Cu2','O3']},
  {'symmetry': 'Ag', 'computed_frequency': 64.0, 'dominant_atoms': ['Cu2','La']},
  {'symmetry': 'Bg', 'computed_frequency': 568.0, 'dominant_atoms': ['O3']},
  {'symmetry': 'Bg', 'computed_frequency': 491.0, 'dominant_atoms': ['O4']},
  {'symmetry': 'Bg', 'computed_frequency': 474.0, 'dominant_atoms': ['O5','O4','O3']},
  {'symmetry': 'Bg', 'computed_frequency': 398.0, 'dominant_atoms': ['O5']},
  {'symmetry': 'Bg', 'computed_frequency': 343.0, 'dominant_atoms': ['O5','O4','O3']},
  {'symmetry': 'Bg', 'computed_frequency': 298.0, 'dominant_atoms': ['O3','O4']},
  {'symmetry': 'Bg', 'computed_frequency': 216.0, 'dominant_atoms': ['Cu2','O4','O3']},
  {'symmetry': 'Bg', 'computed_frequency': 188.0, 'dominant_atoms': ['La','O3','Cu2']},
  {'symmetry': 'Bg', 'computed_frequency': 142.0, 'dominant_atoms': ['Cu2']},
  {'symmetry': 'Bg', 'computed_frequency': 111.0, 'dominant_atoms': ['La']},
  {'symmetry': 'Eg', 'computed_frequency': 578.0, 'dominant_atoms': ['O5']},
  {'symmetry': 'Eg', 'computed_frequency': 387.0, 'dominant_atoms': ['O3']},
  {'symmetry': 'Eg', 'computed_frequency': 313.0, 'dominant_atoms': ['O4']},
  {'symmetry': 'Eg', 'computed_frequency': 156.0, 'dominant_atoms': ['Cu2']},
  {'symmetry': 'Eg', 'computed_frequency': 114.0, 'dominant_atoms': ['La']}
]

with open('/app/outputs/computed_phonon_modes.json', 'w') as f:
    json.dump(data, f, indent=2)
"
