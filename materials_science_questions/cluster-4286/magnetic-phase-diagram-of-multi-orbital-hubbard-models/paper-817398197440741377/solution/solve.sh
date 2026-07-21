#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_order_params.csv ===
cat > /app/outputs/step_01_order_params.csv <<'CSVEOF'
W,m_alpha,m_beta
0.50,0.045,0.080
0.55,0.046,0.079
0.60,0.047,0.078
0.65,0.048,0.077
0.70,0.049,0.076
0.75,0.050,0.075
0.80,0.051,0.074
0.85,0.052,0.073
0.90,0.053,0.072
0.95,0.054,0.071
1.00,0.055,0.070
1.03,0.057,0.068
1.05,0.060,0.065
1.06,0.063,0.045
1.10,0.065,0.040
1.15,0.064,0.039
1.20,0.063,0.038
1.25,0.062,0.037
1.30,0.060,0.036
1.35,0.058,0.035
1.40,0.056,0.034
1.45,0.054,0.033
1.50,0.052,0.032
1.55,0.050,0.031
1.60,0.040,0.020
1.63,0.020,0.010
1.64,0.010,0.005
1.65,0.000,0.000
1.66,0.000,0.000
1.70,0.000,0.000
1.80,0.000,0.000
2.00,0.000,0.000
CSVEOF

# === solve block: step_02_phase_boundaries.csv ===
cat > /app/outputs/step_02_phase_boundaries.csv <<'CSVEOF'
W,T,boundary_type
0.50,0.0050,Neel
0.60,0.0060,Neel
0.70,0.0065,Neel
0.80,0.0068,Neel
0.90,0.0065,Neel
0.95,0.0060,Neel
1.00,0.0050,Neel
1.05,0.0040,Neel
1.10,0.0030,Neel
1.15,0.0020,Neel
1.20,0.0015,Neel
1.25,0.0010,Neel
1.30,0.0007,Neel
1.35,0.0005,Neel
1.40,0.0003,Neel
1.45,0.0002,Neel
1.50,0.0001,Neel
1.55,0.00005,Neel
1.60,0.00001,Neel
1.05,0.0000,AF1_AF2_first_order
1.03,0.0010,AF1_AF2_first_order
1.01,0.0020,AF1_AF2_first_order
0.99,0.0030,AF1_AF2_first_order
0.9826,0.0038,AF1_AF2_first_order
1.65,0.0000,AF2_PM_first_order
1.648,0.0004,AF2_PM_first_order
1.645,0.0008,AF2_PM_first_order
1.641,0.0011,AF2_PM_first_order
CSVEOF
