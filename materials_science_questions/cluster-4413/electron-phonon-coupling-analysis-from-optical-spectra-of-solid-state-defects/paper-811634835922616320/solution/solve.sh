#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cuB2O4_parameters.json ===
python3 << 'EOF'
import json
data = {
    "4b_Dq": 0.1403,
    "4b_Ds": 0.311,
    "4b_Dt": 0.134,
    "8d_Dq": 0.1577,
    "8d_Ds": 0.345,
    "8d_Dt": 0.147
}
with open("/app/outputs/cuB2O4_parameters.json", "w") as f:
    json.dump(data, f, indent=2)
EOF

# === solve block: estimated_parameters.json ===
python3 << 'EOF'
import json
data = [
    {"compound": "La2CuO4", "Dq": 0.1735, "Ds": 0.255, "Dt": 0.125},
    {"compound": "Nd2CuO4", "Dq": 0.1505, "Ds": 0.324, "Dt": 0.144},
    {"compound": "CuGeO3", "Dq": 0.1581, "Ds": 0.303, "Dt": 0.137},
    {"compound": "Sr2CuO2Cl2", "Dq": 0.1391, "Ds": 0.355, "Dt": 0.129},
    {"compound": "Cu3B7O13Cl", "Dq": 0.1258, "Ds": 0.345, "Dt": 0.125}
]
with open("/app/outputs/estimated_parameters.json", "w") as f:
    json.dump(data, f, indent=2)
EOF
