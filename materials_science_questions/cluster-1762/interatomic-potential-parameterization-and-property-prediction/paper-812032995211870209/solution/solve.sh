#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_table1.json ===
python3 -c '
import json
data = {
    "fcc": {"A_l": 0.2115, "2B_l": 0.9479},
    "bcc": {"A_l": 0.1994, "2B_l": 0.7423}
}
with open("/app/outputs/step_01_table1.json", "w") as f:
    json.dump(data, f)
'

# === solve block: step_02_table5.json ===
python3 -c '
import json
data = {
    "Li": {
        "A": {"electrostatic": 0.339, "repulsive": -0.068, "van_der_Waals": 0.008, "total": 0.279},
        "2B": {"electrostatic": 1.263, "repulsive": 0.369, "van_der_Waals": -0.027, "total": 1.605}
    },
    "Na": {
        "A": {"electrostatic": 0.143, "repulsive": -0.042, "van_der_Waals": 0.005, "total": 0.106},
        "2B": {"electrostatic": 0.532, "repulsive": 0.255, "van_der_Waals": -0.017, "total": 0.770}
    },
    "K": {
        "A": {"electrostatic": 0.0644, "repulsive": -0.0202, "van_der_Waals": 0.0099, "total": 0.0541},
        "2B": {"electrostatic": 0.240, "repulsive": 0.127, "van_der_Waals": -0.035, "total": 0.332}
    },
    "Cu": {
        "A": {"electrostatic": 0.573, "repulsive": 4.54, "van_der_Waals": -0.012, "total": 5.1},
        "2B": {"electrostatic": 2.57, "repulsive": 6.35, "van_der_Waals": -0.034, "total": 8.9}
    }
}
with open("/app/outputs/step_02_table5.json", "w") as f:
    json.dump(data, f)
'

# === solve block: step_03_table4.json ===
python3 -c '
import json
data = {
    "Li": {
        "2C": 1.30, "A": 0.279, "2B": 1.605,
        "c11": 1.49, "c12": 1.21, "c44": 1.605
    },
    "Na": {
        "2C": 0.85, "A": 0.106, "2B": 0.770,
        "c11": 0.92, "c12": 0.81, "c44": 0.770
    },
    "K": {
        "2C": 0.40, "A": 0.0541, "2B": 0.332,
        "c11": 0.44, "c12": 0.38, "c44": 0.332
    },
    "Cu": {
        "theoretical": {
            "2C": 14.1, "A": 5.1, "2B": 8.9,
            "c11": 17.5, "c12": 12.4, "c44": 8.9
        },
        "experimental_room": {
            "2C": 12.7, "A": 4.7, "2B": 7.5,
            "c11": 17.0, "c12": 12.3, "c44": 7.5
        },
        "experimental_absolute_zero": {
            "2C": 13.9, "A": 5.1, "2B": 8.2,
            "c11": 18.6, "c12": 13.5, "c44": 8.2
        }
    }
}
with open("/app/outputs/step_03_table4.json", "w") as f:
    json.dump(data, f)
'

# === solve block: step_04_table6.json ===
python3 -c '
import json
data = {
    "Li": {"without_ion_interaction": 354, "with_ion_interaction": 339},
    "Na": {"without_ion_interaction": 131, "with_ion_interaction": 135},
    "K": {"without_ion_interaction": 76, "with_ion_interaction": 90}
}
with open("/app/outputs/step_04_table6.json", "w") as f:
    json.dump(data, f)
'
