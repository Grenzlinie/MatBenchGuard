#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_structural_elastic.json ===
python3 <<'PYEOF'
import json

data = {
    "rocksalt": {
        "a": 4.36,
        "B": 287,
        "C11": 311.1,
        "C12": 275.4,
        "C13": 275.4,
        "C44": 275.8
    },
    "nias": {
        "a": 3.23,
        "c": 5.16,
        "u": 0.411,
        "B": 236,
        "C11": 391.9,
        "C12": 159.0,
        "C13": 128.5,
        "C33": 418.6,
        "C44": 124.7,
        "C66": 120.0
    }
}
with open('/app/outputs/step_01_structural_elastic.json', 'w') as f:
    json.dump(data, f, indent=2)
print("wrote step_01_structural_elastic.json")
PYEOF

# === solve block: step_02_phonon_frequencies.json ===
python3 <<'PYEOF'
import json

data = {
    "wurtzite": {
        "E2_low": 153,
        "A1_TO": 545,
        "E1_TO": 565,
        "E2_high": 579,
        "A1_LO": 766,
        "E1_LO": 786
    },
    "zinc_blende": {
        "TO": 567,
        "LO": 796
    },
    "rocksalt": {
        "TO": 582,
        "LO": 808
    },
    "nias": {
        "TO": 598,
        "LO": 824
    }
}
with open('/app/outputs/step_02_phonon_frequencies.json', 'w') as f:
    json.dump(data, f, indent=2)
print("wrote step_02_phonon_frequencies.json")
PYEOF

# === solve block: step_03_pressure_properties.json ===
python3 <<'PYEOF'
import json

data = {
    "wurtzite": {
        "gamma_E2_low": -0.52,
        "gamma_A1_TO": 1.65,
        "gamma_E1_TO": 1.39,
        "gamma_E2_high": 1.50,
        "gamma_A1_LO": 1.22,
        "gamma_E1_LO": 1.13,
        "domega_dP_E2_low": -0.35,
        "domega_dP_A1_TO": 3.95,
        "domega_dP_E1_TO": 3.45,
        "domega_dP_E2_high": 3.82,
        "domega_dP_A1_LO": 4.1,
        "domega_dP_E1_LO": 3.9
    },
    "zinc_blende": {
        "gamma_TO": 1.62,
        "gamma_LO": 1.17,
        "domega_dP_TO": 4.26,
        "domega_dP_LO": 4.33
    },
    "rocksalt": {
        "gamma_TO": 2.23,
        "gamma_LO": 1.60,
        "domega_dP_TO": 4.45,
        "domega_dP_LO": 4.53
    },
    "nias": {
        "gamma_TO": 1.87,
        "gamma_LO": 1.38,
        "domega_dP_TO": 4.74,
        "domega_dP_LO": 4.82
    }
}
with open('/app/outputs/step_03_pressure_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
print("wrote step_03_pressure_properties.json")
PYEOF
