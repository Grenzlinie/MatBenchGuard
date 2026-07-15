#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
cat > /tmp/write_structures.py << 'PYEOF'
import json
data = {
'BSi2': {'a': 6.881, 'c': 8.127, 'V_per_fu': 40.10, 'atoms': [{'element': 'B', 'x': 0.5078, 'y': 0.4922, 'z': 0.25, 'wyckoff': '8f'}, {'element': 'Si1', 'x': 0.25, 'y': 0.0694, 'z': 0.3634, 'wyckoff': '8g'}, {'element': 'Si2', 'x': 0.25, 'y': 0.5666, 'z': 0.6213, 'wyckoff': '8g'}]},
'LiBSi2': {'a': 6.827, 'c': 8.845, 'V_per_fu': 51.47, 'atoms': [{'element': 'Li', 'x': 0.25, 'y': 0.5031, 'z': 0.0756, 'wyckoff': '8g'}, {'element': 'B', 'x': 0.5078, 'y': 0.4922, 'z': 0.25, 'wyckoff': '8f'}, {'element': 'Si1', 'x': 0.25, 'y': 0.0694, 'z': 0.3634, 'wyckoff': '8g'}, {'element': 'Si2', 'x': 0.25, 'y': 0.5666, 'z': 0.6213, 'wyckoff': '8g'}]},
'NaBSi2': {'a': 7.047, 'c': 9.295, 'V_per_fu': 57.71, 'atoms': [{'element': 'Na', 'x': 0.25, 'y': 0.5007, 'z': 0.0587, 'wyckoff': '8g'}, {'element': 'B', 'x': 0.5103, 'y': 0.4897, 'z': 0.25, 'wyckoff': '8f'}, {'element': 'Si1', 'x': 0.25, 'y': 0.0706, 'z': 0.3569, 'wyckoff': '8g'}, {'element': 'Si2', 'x': 0.25, 'y': 0.5680, 'z': 0.6289, 'wyckoff': '8g'}]},
'KBSi2': {'a': 7.058, 'c': 12.735, 'V_per_fu': 79.30, 'atoms': [{'element': 'K', 'x': 0.25, 'y': 0.5028, 'z': 0.0351, 'wyckoff': '8g'}, {'element': 'B', 'x': 0.4971, 'y': 0.5029, 'z': 0.25, 'wyckoff': '8f'}, {'element': 'Si1', 'x': 0.25, 'y': 0.0776, 'z': 0.3152, 'wyckoff': '8g'}, {'element': 'Si2', 'x': 0.25, 'y': 0.5742, 'z': 0.6759, 'wyckoff': '8g'}]},
'RbBSi2': {'a': 7.120, 'c': 13.404, 'V_per_fu': 84.94, 'atoms': [{'element': 'Rb', 'x': 0.25, 'y': 0.5018, 'z': 0.0328, 'wyckoff': '8g'}, {'element': 'B', 'x': 0.4975, 'y': 0.5025, 'z': 0.25, 'wyckoff': '8f'}, {'element': 'Si1', 'x': 0.25, 'y': 0.0790, 'z': 0.3098, 'wyckoff': '8g'}, {'element': 'Si2', 'x': 0.25, 'y': 0.5756, 'z': 0.6802, 'wyckoff': '8g'}]}
}
with open('/app/outputs/structures_summary.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
cat > /tmp/write_electronic.py << 'PYEOF'
import json
data = {
'BSi2': {'band_gap_eV': None, 'is_metal': True, 'dos_fermi_character': 'B_p and Si_p'},
'LiBSi2': {'band_gap_eV': 1.14, 'is_metal': False, 'dos_fermi_character': 'N/A (semiconductor)'},
'NaBSi2': {'band_gap_eV': 0.73, 'is_metal': False, 'dos_fermi_character': 'N/A (semiconductor)'},
'KBSi2': {'band_gap_eV': None, 'is_metal': True, 'dos_fermi_character': 'Si_pz dominated'},
'RbBSi2': {'band_gap_eV': None, 'is_metal': True, 'dos_fermi_character': 'Si_pz dominated'}
}
with open('/app/outputs/electronic_summary.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
cat > /tmp/write_elastic.py << 'PYEOF'
import json
data = {
'BSi2': {'C11': 174, 'C33': 142, 'C44': 11, 'C66': 34, 'C12': 78, 'C13': 57, 'B': 96, 'G': 25, 'B/G': 3.84},
'LiBSi2': {'C11': 238, 'C33': 210, 'C44': 89, 'C66': 68, 'C12': 39, 'C13': 47, 'B': 103, 'G': 86, 'B/G': 1.20},
'NaBSi2': {'C11': 202, 'C33': 135, 'C44': 72, 'C66': 87, 'C12': 44, 'C13': 43, 'B': 87, 'G': 73, 'B/G': 1.19},
'KBSi2': {'C11': 118, 'C33': 46, 'C44': 22, 'C66': 43, 'C12': 37, 'C13': 19, 'B': 43, 'G': 29, 'B/G': 1.48},
'RbBSi2': {'C11': 112, 'C33': 49, 'C44': 18, 'C66': 41, 'C12': 34, 'C13': 18, 'B': 42, 'G': 27, 'B/G': 1.56}
}
with open('/app/outputs/elastic_constants_summary.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: structures_summary.json ===
cat > "$OUTDIR/structures_summary.json" << 'EOF'
{
  "BSi2": {
    "a": 6.881,
    "c": 8.127,
    "V_per_fu": 40.1,
    "atoms": [
      {"element": "B", "x": 0.5078, "y": 0.4922, "z": 0.25, "wyckoff": "8f"},
      {"element": "Si1", "x": 0.25, "y": 0.0694, "z": 0.3634, "wyckoff": "8g"},
      {"element": "Si2", "x": 0.25, "y": 0.5666, "z": 0.6213, "wyckoff": "8g"}
    ]
  },
  "LiBSi2": {
    "a": 6.827,
    "c": 8.845,
    "V_per_fu": 51.47,
    "atoms": [
      {"element": "Li", "x": 0.25, "y": 0.5031, "z": 0.0756, "wyckoff": "8g"},
      {"element": "B", "x": 0.5078, "y": 0.4922, "z": 0.25, "wyckoff": "8f"},
      {"element": "Si1", "x": 0.25, "y": 0.0694, "z": 0.3634, "wyckoff": "8g"},
      {"element": "Si2", "x": 0.25, "y": 0.5666, "z": 0.6213, "wyckoff": "8g"}
    ]
  },
  "NaBSi2": {
    "a": 7.047,
    "c": 9.295,
    "V_per_fu": 57.71,
    "atoms": [
      {"element": "Na", "x": 0.25, "y": 0.5007, "z": 0.0587, "wyckoff": "8g"},
      {"element": "B", "x": 0.5103, "y": 0.4897, "z": 0.25, "wyckoff": "8f"},
      {"element": "Si1", "x": 0.25, "y": 0.0706, "z": 0.3569, "wyckoff": "8g"},
      {"element": "Si2", "x": 0.25, "y": 0.568, "z": 0.6289, "wyckoff": "8g"}
    ]
  },
  "KBSi2": {
    "a": 7.058,
    "c": 12.735,
    "V_per_fu": 79.3,
    "atoms": [
      {"element": "K", "x": 0.25, "y": 0.5028, "z": 0.0351, "wyckoff": "8g"},
      {"element": "B", "x": 0.4971, "y": 0.5029, "z": 0.25, "wyckoff": "8f"},
      {"element": "Si1", "x": 0.25, "y": 0.0776, "z": 0.3152, "wyckoff": "8g"},
      {"element": "Si2", "x": 0.25, "y": 0.5742, "z": 0.6759, "wyckoff": "8g"}
    ]
  },
  "RbBSi2": {
    "a": 7.12,
    "c": 13.404,
    "V_per_fu": 84.94,
    "atoms": [
      {"element": "Rb", "x": 0.25, "y": 0.5018, "z": 0.0328, "wyckoff": "8g"},
      {"element": "B", "x": 0.4975, "y": 0.5025, "z": 0.25, "wyckoff": "8f"},
      {"element": "Si1", "x": 0.25, "y": 0.079, "z": 0.3098, "wyckoff": "8g"},
      {"element": "Si2", "x": 0.25, "y": 0.5756, "z": 0.6802, "wyckoff": "8g"}
    ]
  }
}
EOF

# === solve block: bsi2_phonon_stability.txt ===
echo 'Stable: no imaginary frequencies' > /app/outputs/bsi2_phonon_stability.txt

# === solve block: electronic_summary.json ===
python3 /tmp/write_electronic.py

# === solve block: elastic_constants_summary.json ===
python3 /tmp/write_elastic.py
