#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_band_gap_and_dielectric.json ===
python3 -c "
import json
data = {
    'band_gap_eV': 1.76,
    'epsilon_inf_perp': 6.96,
    'epsilon_inf_par': 7.51,
    'epsilon0_perp': 19.31,
    'epsilon0_par': 9.59
}
with open('/app/outputs/step_01_band_gap_and_dielectric.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_02_phonon_frequencies.json ===
python3 -c "
import json

modes = []

# Eg Raman
for freq in [163, 280, 516, 571, 619, 737, 778, 813, 849, 1064, 1077]:
    modes.append({'symmetry': 'Eg', 'frequency_cm-1': freq, 'character': 'Raman', 'irreducible_rep': 'Eg'})

# Eu TO
for freq in [127, 406, 547, 634, 657, 777, 785, 852, 1052, 1094]:
    modes.append({'symmetry': 'Eu', 'frequency_cm-1': freq, 'character': 'TO', 'irreducible_rep': 'Eu'})

# Eu LO
for freq in [232, 413, 549, 634, 658, 779, 786, 852, 1079, 1097]:
    modes.append({'symmetry': 'Eu', 'frequency_cm-1': freq, 'character': 'LO', 'irreducible_rep': 'Eu'})

# A1g Raman
for freq in [200, 530, 677, 758, 789, 890, 1023, 1167]:
    modes.append({'symmetry': 'A1g', 'frequency_cm-1': freq, 'character': 'Raman', 'irreducible_rep': 'A1g'})

# A2u TO
for freq in [281, 486, 661, 794, 911, 1008, 1113]:
    modes.append({'symmetry': 'A2u', 'frequency_cm-1': freq, 'character': 'TO', 'irreducible_rep': 'A2u'})

# A2u LO
for freq in [310, 492, 664, 798, 911, 1008, 1114]:
    modes.append({'symmetry': 'A2u', 'frequency_cm-1': freq, 'character': 'LO', 'irreducible_rep': 'A2u'})

# A1u silent
for freq in [427, 638, 775]:
    modes.append({'symmetry': 'A1u', 'frequency_cm-1': freq, 'character': 'silent', 'irreducible_rep': 'A1u'})

# A2g silent
for freq in [307, 530, 751]:
    modes.append({'symmetry': 'A2g', 'frequency_cm-1': freq, 'character': 'silent', 'irreducible_rep': 'A2g'})

with open('/app/outputs/step_02_phonon_frequencies.json', 'w') as f:
    json.dump({'modes': modes}, f, indent=2)
"

# === solve block: step_03_elastic_constants.json ===
python3 -c "
import json
data = {
    'C11_GPa': 470.37,
    'C12_GPa': 89.80,
    'C13_GPa': 98.06,
    'C14_GPa': -31.02,
    'C33_GPa': 380.45,
    'C44_GPa': 173.62
}
with open('/app/outputs/step_03_elastic_constants.json', 'w') as f:
    json.dump(data, f, indent=2)
"
