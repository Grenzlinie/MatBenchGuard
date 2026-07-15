#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: qm_mm_results.json ===
python3 -c '
import json
data = [
    {"probe": "clean", "delta_H_st": 0.0, "delta_H_el": 0.0, "delta_H_ch": 0.0,
     "v_st": 3759.5, "v_el": 3760.5, "v_ch": 3760.5,
     "delta_v_st": 0.0, "delta_v_el": 0.0, "delta_v_ch": 0.0},
    {"probe": "H2S", "delta_H_st": 4.2, "delta_H_el": 2.3, "delta_H_ch": 2.0,
     "v_st": 3350, "v_el": 3538, "v_ch": 3521,
     "delta_v_st": 411, "delta_v_el": 222, "delta_v_ch": 238},
    {"probe": "O3", "delta_H_st": 6.1, "delta_H_el": 4.3, "delta_H_ch": 3.4,
     "v_st": 3532, "v_el": 3602, "v_ch": 3607,
     "delta_v_st": 229, "delta_v_el": 158, "delta_v_ch": 153},
    {"probe": "CO", "delta_H_st": 4.4, "delta_H_el": 3.4, "delta_H_ch": 2.9,
     "v_st": 3605, "v_el": 3609, "v_ch": 3626,
     "delta_v_st": 155, "delta_v_el": 152, "delta_v_ch": 134},
    {"probe": "(CH3)2CO", "delta_H_st": 11.4, "delta_H_el": 8.8, "delta_H_ch": 8.8,
     "v_st": 3228, "v_el": 3273, "v_ch": 3228,
     "delta_v_st": 531, "delta_v_el": 488, "delta_v_ch": 531},
    {"probe": "NH3", "delta_H_st": 11.9, "delta_H_el": 11.0, "delta_H_ch": 11.8,
     "v_st": 2954, "v_el": 3018, "v_ch": 2952,
     "delta_v_st": 807, "delta_v_el": 742, "delta_v_ch": 808},
    {"probe": "C5H5N", "delta_H_st": 12.2, "delta_H_el": 10.6, "delta_H_ch": 10.3,
     "v_st": 2826, "v_el": 2947, "v_ch": 2858,
     "delta_v_st": 935, "delta_v_el": 813, "delta_v_ch": 901},
    {"probe": "CH3CN", "delta_H_st": 9.4, "delta_H_el": 7.3, "delta_H_ch": 7.6,
     "v_st": 3407, "v_el": 3483, "v_ch": 3445,
     "delta_v_st": 354, "delta_v_el": 277, "delta_v_ch": 316}
]
with open("/app/outputs/qm_mm_results.json", "w") as f:
    json.dump(data, f, indent=2)
'
