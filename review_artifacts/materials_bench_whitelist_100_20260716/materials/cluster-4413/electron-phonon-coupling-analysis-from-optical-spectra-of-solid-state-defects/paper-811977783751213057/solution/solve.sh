#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: vibronic_fine_structure.json ===
python3 << 'PYEOF'
import json

nts = [
    {
        "l": 1,
        "ed": [
            {"energy": -73.0, "intensity": 0.296},
            {"energy": -69.0, "intensity": 0.038}
        ],
        "ep": [
            {"energy": -24.0, "intensity": 3.0},
            {"energy": -23.0, "intensity": 1.526},
            {"energy": -21.0, "intensity": 1.582},
            {"energy": -18.0, "intensity": 2.21}
        ]
    },
    {
        "l": 2,
        "ed": [
            {"energy": -51.0, "intensity": 0.698},
            {"energy": -45.0, "intensity": 0.144},
            {"energy": -44.0, "intensity": 0.084},
            {"energy": -43.0, "intensity": 0.032}
        ],
        "ep": [
            {"energy": -23.0, "intensity": 2.17},
            {"energy": -21.0, "intensity": 3.0},
            {"energy": -17.0, "intensity": 1.942}
        ]
    },
    {
        "l": 3,
        "ed": [
            {"energy": -18.0, "intensity": 0.885},
            {"energy": -17.0, "intensity": 0.544},
            {"energy": -14.0, "intensity": 1.088}
        ],
        "ep": [
            {"energy": -35.0, "intensity": 1.552},
            {"energy": -28.0, "intensity": 1.074},
            {"energy": -26.0, "intensity": 1.809},
            {"energy": -23.0, "intensity": 1.13}
        ]
    },
    {
        "l": 4,
        "ed": [
            {"energy": -9.0, "intensity": 0.131},
            {"energy": -8.0, "intensity": 0.190},
            {"energy": -6.0, "intensity": 0.379}
        ],
        "ep": [
            {"energy": -28.0, "intensity": 1.99},
            {"energy": -22.0, "intensity": 1.51}
        ]
    }
]

ts = {
    "edp_bands": [
        {"l": 1, "M_imp": 60.0, "E": -123.0, "I_a": 6.1, "I_b": 18.3, "p_ab": 0.33},
        {"l": 2, "M_imp": 50.0, "E": -93.0, "I_a": 5.6, "I_b": 15.6, "p_ab": 0.353},
        {"l": 3, "M_imp": 49.0, "E": -63.0, "I_a": 6.73, "I_b": 24.3, "p_ab": 0.277},
        {"l": 4, "M_imp": 50.0, "E": -39.0, "I_a": 8.85, "I_b": 38.4, "p_ab": 0.23}
    ],
    "ed_ep_fine": [
        {"l": 1, "type": "ED", "E_j": -69.0, "I_a": 0.032, "I_b": 0.74, "p_ab": 0.043},
        {"l": 1, "type": "EP", "E_j": -12.0, "I_a": 3.83, "I_b": 1.38, "p_ab": 2.77},
        {"l": 1, "type": "EP", "E_j": -9.0, "I_a": 0.508, "I_b": 0.023, "p_ab": 21.0},
        {"l": 1, "type": "EP", "E_j": -5.0, "I_a": 0.69, "I_b": 5.35, "p_ab": 0.13},
        {"l": 2, "type": "ED", "E_j": -44.0, "I_a": 0.081, "I_b": 1.66, "p_ab": 0.048},
        {"l": 2, "type": "EP", "E_j": -12.0, "I_a": 3.76, "I_b": 1.46, "p_ab": 2.6},
        {"l": 2, "type": "EP", "E_j": -9.0, "I_a": 0.499, "I_b": 0.025, "p_ab": 20.0},
        {"l": 2, "type": "EP", "E_j": -5.0, "I_a": 0.677, "I_b": 5.46, "p_ab": 0.12},
        {"l": 3, "type": "ED", "E_j": -20.0, "I_a": 0.282, "I_b": 0.074, "p_ab": 3.8},
        {"l": 3, "type": "ED", "E_j": -17.0, "I_a": 0.094, "I_b": 5.9, "p_ab": 0.016},
        {"l": 3, "type": "EP", "E_j": -11.0, "I_a": 3.24, "I_b": 1.6, "p_ab": 2.0},
        {"l": 3, "type": "EP", "E_j": -9.0, "I_a": 0.5, "I_b": 0.0063, "p_ab": 79.0},
        {"l": 3, "type": "EP", "E_j": -4.0, "I_a": 0.62, "I_b": 5.6, "p_ab": 0.1},
        {"l": 4, "type": "ED", "E_j": -9.0, "I_a": 1.04, "I_b": 0.064, "p_ab": 15.6},
        {"l": 4, "type": "ED", "E_j": -4.0, "I_a": 0.499, "I_b": 3.0, "p_ab": 0.17},
        {"l": 4, "type": "EP", "E_j": -14.0, "I_a": 1.0, "I_b": 3.51, "p_ab": 0.28},
        {"l": 4, "type": "EP", "E_j": -12.0, "I_a": 0.342, "I_b": 0.177, "p_ab": 1.9}
    ]
}

out = {"nts": nts, "ts": ts}
with open("/app/outputs/vibronic_fine_structure.json", "w") as f:
    json.dump(out, f, indent=2)
print("Reference file written.")
PYEOF
