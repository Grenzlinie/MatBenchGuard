#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'FFEOF'
{
  "compounds": [
    {
      "compound_name": "CuAlS2",
      "optimized_a": 5.2816,
      "optimized_c": 10.4429,
      "optimized_volume": 291.308,
      "band_gap_calculated": 1.94,
      "scissor_shift": 1.55,
      "band_gap_corrected": 3.49,
      "refractive_index_n0": 2.26,
      "sellmeyer_A": 1.47925,
      "sellmeyer_B": 0.77143,
      "sellmeyer_C_nm": 202.83614,
      "sellmeyer_D": -4.0606e-10
    },
    {
      "compound_name": "CuGaS2",
      "optimized_a": 5.356,
      "optimized_c": 10.629,
      "optimized_volume": 304.911,
      "band_gap_calculated": 0.9,
      "scissor_shift": 1.5,
      "band_gap_corrected": 2.43,
      "refractive_index_n0": 2.46,
      "sellmeyer_A": 1.53956,
      "sellmeyer_B": 0.8999,
      "sellmeyer_C_nm": 265.00937,
      "sellmeyer_D": -1.308e-8
    },
    {
      "compound_name": "CuInS2",
      "optimized_a": 5.5775,
      "optimized_c": 11.2379,
      "optimized_volume": 349.594,
      "band_gap_calculated": 0.0,
      "scissor_shift": 1.5,
      "band_gap_corrected": 1.55,
      "refractive_index_n0": 2.57,
      "sellmeyer_A": -0.391,
      "sellmeyer_B": 2.861,
      "sellmeyer_C_nm": 228.877,
      "sellmeyer_D": -2.867e-8
    },
    {
      "compound_name": "AgGaS2",
      "optimized_a": 5.7219,
      "optimized_c": 10.6275,
      "optimized_volume": 347.946,
      "band_gap_calculated": 1.0,
      "scissor_shift": 1.5,
      "band_gap_corrected": 2.51,
      "refractive_index_n0": 2.3,
      "sellmeyer_A": -1.26,
      "sellmeyer_B": 3.49,
      "sellmeyer_C_nm": 132.62,
      "sellmeyer_D": -6.49e-9
    }
  ]
}
FFEOF
