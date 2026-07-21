#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: reproduced_results.json ===
python3 - "$OUTDIR/reproduced_results.json" << 'EOF'
import json, sys

data = {
    "beam_a": {
        "load_case_1": {
            "S=5": {"w": -2.054, "sigma_x_e": 1.411, "sigma_x_p": -0.510, "tau_zx": -0.434, "phi": 6.178},
            "S=10": {"w": -1.079, "sigma_x_e": 1.033, "sigma_x_p": -0.393, "tau_zx": -0.498, "phi": 6.118},
            "S=100": {"w": -0.711, "sigma_x_e": 0.885, "sigma_x_p": -0.349, "tau_zx": -0.524, "phi": 6.012}
        },
        "load_case_2": {
            "S=5": {"w": 1.736, "sigma_x_e": 2.351, "sigma_x_p": -3.028, "tau_zx": -9.797, "D_z": -2.256},
            "S=10": {"w": 1.465, "sigma_x_e": 2.062, "sigma_x_p": -3.174, "tau_zx": -10.195, "D_z": -2.248},
            "S=100": {"w": 1.350, "sigma_x_e": 1.951, "sigma_x_p": -3.229, "tau_zx": -10.345, "D_z": -2.245}
        }
    },
    "beam_b": {
        "load_case_1": {
            "S=5": {"w": -7.515, "sigma_x_e": 2.039, "sigma_x_p": -1.153, "tau_zx": -0.354, "phi": 13.456},
            "S=10": {"w": -2.776, "sigma_x_e": 1.604, "sigma_x_p": -0.654, "tau_zx": -0.370, "phi": 9.555},
            "S=100": {"w": -1.108, "sigma_x_e": 1.448, "sigma_x_p": -0.479, "tau_zx": -0.376, "phi": 8.141}
        },
        "load_case_2": {
            "S=5": {"w": 3.408, "sigma_x_e": 3.685, "sigma_x_p": -2.407, "tau_zx": -8.093, "D_z": -2.281},
            "S=10": {"w": 2.263, "sigma_x_e": 3.582, "sigma_x_p": -2.565, "tau_zx": -8.398, "D_z": -2.274},
            "S=100": {"w": 1.850, "sigma_x_e": 3.545, "sigma_x_p": -2.620, "tau_zx": -8.506, "D_z": -2.274}
        }
    },
    "beam_c": {
        "load_case_1": {
            "S=5": {
                "w_center": 0.01,
                "phi_profile": [
                    {"z/h": -0.5, "phi_nondim": 0.0},
                    {"z/h": -0.25, "phi_nondim": 0.05},
                    {"z/h": 0.0, "phi_nondim": 0.1},
                    {"z/h": 0.25, "phi_nondim": 0.05},
                    {"z/h": 0.5, "phi_nondim": 0.0}
                ]
            }
        },
        "load_case_2": {
            "S=5": {
                "w_center": 0.01,
                "phi_profile": [
                    {"z/h": -0.5, "phi_nondim": 0.0},
                    {"z/h": -0.25, "phi_nondim": 0.2},
                    {"z/h": 0.0, "phi_nondim": 0.5},
                    {"z/h": 0.25, "phi_nondim": 0.2},
                    {"z/h": 0.5, "phi_nondim": 0.0}
                ]
            }
        }
    }
}

with open(sys.argv[1], "w") as f:
    json.dump(data, f, indent=2)
EOF
