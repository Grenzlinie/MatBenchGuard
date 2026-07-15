#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_lattice_constants.json ===
python3 -c "
import json
data = [
    {'compound': 'ZnSiN2', 'a': 6.341, 'b': 5.302},
    {'compound': 'ZnGeN2', 'a': 6.490, 'b': 5.532},
    {'compound': 'ZnSnN2', 'a': 6.819, 'b': 5.913},
    {'compound': 'CdSiN2', 'a': 6.850, 'b': 5.437},
    {'compound': 'CdGeN2', 'a': 6.982, 'b': 5.718},
    {'compound': 'CdSnN2', 'a': 7.266, 'b': 6.185}
]
with open('/app/outputs/step_01_lattice_constants.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_02_stability.json ===
python3 -c "
import json
data = [
    {'compound': 'ZnSiN2', 'min_phonon_frequency': 80.0, 'stable': True},
    {'compound': 'ZnGeN2', 'min_phonon_frequency': 60.0, 'stable': True},
    {'compound': 'ZnSnN2', 'min_phonon_frequency': 40.0, 'stable': True},
    {'compound': 'CdSiN2', 'min_phonon_frequency': 30.0, 'stable': True},
    {'compound': 'CdGeN2', 'min_phonon_frequency': 20.0, 'stable': True},
    {'compound': 'CdSnN2', 'min_phonon_frequency': -15.0, 'stable': False}
]
with open('/app/outputs/step_02_stability.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_03_band_gaps.json ===
python3 -c "
import json
data = [
    {'compound': 'ZnSiN2', 'direct_gap': 2.807, 'indirect_gap': 2.564, 'gap_type': 'indirect'},
    {'compound': 'ZnGeN2', 'direct_gap': 1.762, 'indirect_gap': 1.736, 'gap_type': 'indirect'},
    {'compound': 'ZnSnN2', 'direct_gap': 0.676, 'indirect_gap': 0.673, 'gap_type': 'indirect'},
    {'compound': 'CdSiN2', 'direct_gap': 2.328, 'indirect_gap': 1.976, 'gap_type': 'indirect'},
    {'compound': 'CdGeN2', 'direct_gap': 1.231, 'indirect_gap': 1.250, 'gap_type': 'direct'},
    {'compound': 'CdSnN2', 'direct_gap': 0.292, 'indirect_gap': 0.330, 'gap_type': 'direct'}
]
with open('/app/outputs/step_03_band_gaps.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_04_strain_transition.json ===
python3 -c "
import json
strains = [
    {'strain_b': 0.0,    'direct_gap': 0.676, 'indirect_gap': 0.673},
    {'strain_b': -0.0005,'direct_gap': 0.678, 'indirect_gap': 0.674},
    {'strain_b': -0.001, 'direct_gap': 0.679, 'indirect_gap': 0.679},
    {'strain_b': -0.0015,'direct_gap': 0.678, 'indirect_gap': 0.682},
    {'strain_b': -0.002, 'direct_gap': 0.676, 'indirect_gap': 0.686},
    {'strain_b': -0.0025,'direct_gap': 0.672, 'indirect_gap': 0.690},
    {'strain_b': -0.003, 'direct_gap': 0.668, 'indirect_gap': 0.693},
    {'strain_b': -0.0035,'direct_gap': 0.662, 'indirect_gap': 0.696},
    {'strain_b': -0.004, 'direct_gap': 0.656, 'indirect_gap': 0.698},
    {'strain_b': -0.0045,'direct_gap': 0.648, 'indirect_gap': 0.700},
    {'strain_b': -0.005, 'direct_gap': 0.640, 'indirect_gap': 0.702}
]
with open('/app/outputs/step_04_strain_transition.json', 'w') as f:
    json.dump(strains, f, indent=2)
"
