#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json
data = {
    "rutile_LDA_a": 4.580,
    "rutile_LDA_c": 3.080,
    "rutile_LDA_u": 0.3044,
    "rutile_GGA_a": 4.825,
    "rutile_GGA_c": 3.245,
    "rutile_GGA_u": 0.3065,
    "CaCl2_LDA_a": 4.506,
    "CaCl2_LDA_b": 4.371,
    "CaCl2_LDA_c": 3.020,
    "CaCl2_LDA_u": 0.3170,
    "CaCl2_LDA_v": 0.2750,
    "CaCl2_GGA_a": 4.855,
    "CaCl2_GGA_b": 4.737,
    "CaCl2_GGA_c": 3.258,
    "CaCl2_GGA_u": 0.3273,
    "CaCl2_GGA_v": 0.2853,
    "cubic_LDA_a": 5.872,
    "cubic_LDA_u": 0.3420,
    "cubic_GGA_a": 5.079,
    "cubic_GGA_u": 0.3460,
    "rutile_LDA_B": 212,
    "rutile_GGA_B": 194,
    "CaCl2_LDA_B": 221,
    "CaCl2_GGA_B": 205,
    "cubic_LDA_B": 230,
    "cubic_GGA_B": 213,
    "rutile_LDA_Ecoh": 7.7,
    "rutile_GGA_Ecoh": 7.1,
    "CaCl2_LDA_Ecoh": 9.05,
    "CaCl2_GGA_Ecoh": 8.2,
    "cubic_LDA_Ecoh": 5.25,
    "cubic_GGA_Ecoh": 4.825,
    "rutile_GGA_gap": 0.77,
    "rutile_EVGGA_gap": 1.28,
    "CaCl2_GGA_gap": 0.97,
    "CaCl2_EVGGA_gap": 1.44,
    "cubic_GGA_gap": 0.50,
    "cubic_EVGGA_gap": 0.94,
    "P_trans_rutile_CaCl2_LDA": 10.1,
    "P_trans_rutile_CaCl2_GGA": 12.4,
    "P_trans_CaCl2_cubic_LDA": 18.3,
    "P_trans_CaCl2_cubic_GGA": 22.1,
    "rutile_GGA_m_e": 0.087,
    "rutile_GGA_m_h": 0.602,
    "rutile_EVGGA_m_e": 0.100,
    "rutile_EVGGA_m_h": 0.682,
    "CaCl2_GGA_m_e": 0.085,
    "CaCl2_GGA_m_h": 0.763,
    "CaCl2_EVGGA_m_e": 0.091,
    "CaCl2_EVGGA_m_h": 0.940,
    "cubic_GGA_m_e": 0.900,
    "cubic_GGA_m_h": 1.02,
    "cubic_EVGGA_m_e": 0.105,
    "cubic_EVGGA_m_h": 1.213,
    "rutile_LDA_ionicity": 0.762,
    "rutile_GGA_ionicity": 0.797
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
'
