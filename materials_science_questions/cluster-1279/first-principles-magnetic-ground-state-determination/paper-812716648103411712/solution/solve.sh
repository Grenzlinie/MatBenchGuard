#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: calculated_properties.json ===
python3 << 'PYEOF'
import json

data = {
  "BeF3": {
    "a": 5.173,
    "E_f": -5.592,
    "E_c": 13.602,
    "T_C": 466.182,
    "M_t": 1.0,
    "E_g_up": 4.488,
    "E_g_HM": 0.599,
    "VBM": -0.599,
    "CBM": 3.889,
    "M_F_A": 0.191,
    "M_F_B": 0.572,
    "M_F_C": 0.191,
    "M_X": -0.014,
    "M_int": 0.060,
    "C11": 289.095,
    "C12": 157.452,
    "C44": 5.165,
    "B": 201.333,
    "G": 18.804,
    "E": 54.709,
    "nu": 0.455,
    "K": 10.707,
    "A": 0.078,
    "hydrostatic_HM_range": {"min_strain": -25.440, "max_strain": 15.0},
    "tetragonal_HM_range": {"min_c_over_a": 0.69795, "max_c_over_a": 1.74747}
  },
  "MgF3": {
    "a": 5.404,
    "E_f": -10.007,
    "E_c": 13.762,
    "T_C": 411.246,
    "M_t": 1.0,
    "E_g_up": 6.352,
    "E_g_HM": 0.568,
    "VBM": -0.568,
    "CBM": 5.784,
    "M_F_A": 0.198,
    "M_F_B": 0.536,
    "M_F_C": 0.198,
    "M_X": -0.004,
    "M_int": 0.072,
    "C11": 228.859,
    "C12": 126.844,
    "C44": 25.493,
    "B": 160.849,
    "G": 33.784,
    "E": 94.721,
    "nu": 0.402,
    "K": 4.761,
    "A": 0.500,
    "hydrostatic_HM_range": {"min_strain": -30.511, "max_strain": 15.0},
    "tetragonal_HM_range": {"min_c_over_a": 0.68331, "max_c_over_a": 1.83274}
  },
  "CaF3": {
    "a": 5.724,
    "E_f": -12.638,
    "E_c": 16.778,
    "T_C": 376.048,
    "M_t": 1.0,
    "E_g_up": 8.795,
    "E_g_HM": 0.566,
    "VBM": -0.566,
    "CBM": 8.229,
    "M_F_A": 0.206,
    "M_F_B": 0.506,
    "M_F_C": 0.206,
    "M_X": -0.009,
    "M_int": 0.091,
    "C11": 179.169,
    "C12": 107.823,
    "C44": 46.084,
    "B": 131.605,
    "G": 41.593,
    "E": 112.887,
    "nu": 0.357,
    "K": 3.164,
    "A": 1.292,
    "hydrostatic_HM_range": {"min_strain": -21.963, "max_strain": 15.0},
    "tetragonal_HM_range": {"min_c_over_a": 0.66749, "max_c_over_a": 2.10223}
  },
  "SrF3": {
    "a": 6.019,
    "E_f": -12.999,
    "E_c": 16.834,
    "T_C": 382.118,
    "M_t": 1.0,
    "E_g_up": 8.715,
    "E_g_HM": 0.495,
    "VBM": -0.495,
    "CBM": 8.220,
    "M_F_A": 0.214,
    "M_F_B": 0.481,
    "M_F_C": 0.214,
    "M_X": -0.002,
    "M_int": 0.093,
    "C11": 155.671,
    "C12": 81.837,
    "C44": 47.202,
    "B": 106.448,
    "G": 42.233,
    "E": 111.901,
    "nu": 0.325,
    "K": 2.520,
    "A": 1.252,
    "hydrostatic_HM_range": {"min_strain": -13.452, "max_strain": 15.0},
    "tetragonal_HM_range": {"min_c_over_a": 0.65609, "max_c_over_a": 2.47141}
  },
  "BaF3": {
    "a": 6.371,
    "E_f": -13.029,
    "E_c": 17.133,
    "T_C": 379.921,
    "M_t": 1.0,
    "E_g_up": 8.711,
    "E_g_HM": 0.411,
    "VBM": -0.411,
    "CBM": 8.300,
    "M_F_A": 0.220,
    "M_F_B": 0.453,
    "M_F_C": 0.222,
    "M_X": -0.001,
    "M_int": 0.106,
    "C11": 125.580,
    "C12": 68.767,
    "C44": 45.783,
    "B": 87.705,
    "G": 37.808,
    "E": 99.172,
    "nu": 0.312,
    "K": 2.320,
    "A": 1.612,
    "hydrostatic_HM_range": {"min_strain": -13.324, "max_strain": 15.0},
    "tetragonal_HM_range": {"min_c_over_a": 0.68928, "max_c_over_a": 2.71072}
  }
}

with open('/app/outputs/calculated_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
