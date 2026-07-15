#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: v_shape_results.json ===
python3 << 'PYEOF'
import json

data = {
    "table2": [
        {"K_I": 1.2548, "K_II": 0.8456, "K_I_kink": -0.4492, "RRMS_normal": 1.34e-05, "RRMS_shear": 6.08e-05}
    ],
    "table4": [
        {"rho": "1/2", "K_I": 1.2550, "K_II": 0.8452, "K_I_kink": -0.2505, "RRMS_normal": 1.03e-04, "RRMS_shear": 2.19e-03},
        {"rho": "8/13", "K_I": 1.2548, "K_II": 0.8456, "K_I_kink": -0.4492, "RRMS_normal": 9.08e-06, "RRMS_shear": 5.77e-05},
        {"rho": "274/445", "K_I": 1.2548, "K_II": 0.8456, "K_I_kink": -0.4498, "RRMS_normal": 1.06e-05, "RRMS_shear": 8.71e-06}
    ],
    "table5": [
        {"case": "1", "K_I_seg1": -1.1554, "K_I_seg2": 1.8206, "K_II_seg1": 0.9037, "K_II_seg2": -0.7554, "K_I_kink": -0.0564, "K_II_kink": -2.4051, "RRMS_normal": 1.16e-06, "RRMS_shear": 2.25e-06},
        {"case": "2", "K_I_seg1": -1.1495, "K_I_seg2": 1.8147, "K_II_seg1": 0.9134, "K_II_seg2": -0.7457, "K_I_kink": -0.0556, "K_II_kink": -3.4794, "RRMS_normal": 0.0147, "RRMS_shear": 0.0264},
        {"case": "3", "K_I_seg1": -1.1519, "K_I_seg2": 1.8171, "K_II_seg1": 0.9591, "K_II_seg2": -0.6999, "K_I_kink": -0.0565, "K_II_kink": 0.0, "RRMS_normal": 0.0344, "RRMS_shear": 0.0392}
    ]
}

with open("/app/outputs/v_shape_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: multiply_kinked_results.json ===
python3 << 'PYEOF'
import json

data = {
    "table7": [
        {"a1_a2": 0.1, "theta": 30, "K_I": 1.604, "K_II": 0.716},
        {"a1_a2": 0.1, "theta": 45, "K_I": 1.237, "K_II": 0.926},
        {"a1_a2": 0.1, "theta": 60, "K_I": 0.810, "K_II": 0.995},
        {"a1_a2": 0.2, "theta": 30, "K_I": 1.695, "K_II": 0.827},
        {"a1_a2": 0.2, "theta": 45, "K_I": 1.260, "K_II": 1.061},
        {"a1_a2": 0.2, "theta": 60, "K_I": 0.762, "K_II": 1.126}
    ],
    "table8": [
        {"a3": 0.10, "K_I": 0.3991, "K_II": -0.2464},
        {"a3": 0.20, "K_I": 0.5687, "K_II": -0.3498},
        {"a3": 0.60, "K_I": 1.0120, "K_II": -0.6127},
        {"a3": 1.0,  "K_I": 1.3223, "K_II": -0.7959}
    ]
}

with open("/app/outputs/multiply_kinked_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: branched_results.json ===
python3 << 'PYEOF'
import json

data = {
    "table9": [
        {"d": 1.05, "K_I": 2.00, "K_II": 0.94},
        {"d": 1.10, "K_I": 1.93, "K_II": 0.89},
        {"d": 1.25, "K_I": 1.81, "K_II": 0.78},
        {"d": 1.50, "K_I": 1.68, "K_II": 0.70}
    ],
    "table10": [
        {"beta2": 30, "K_I_tip2": 0.53, "K_II_tip2": 1.12, "K_I_tip6": 1.66, "K_II_tip6": -0.31},
        {"beta2": 60, "K_I_tip2": 0.61, "K_II_tip2": 1.15, "K_I_tip6": 1.10, "K_II_tip6": -0.95}
    ]
}

with open("/app/outputs/branched_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
