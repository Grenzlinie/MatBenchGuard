#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: Pna2_1_fractional_coordinates.csv ===
cat > /app/outputs/Pna2_1_fractional_coordinates.csv <<'FFEOF'
atom,x,y,z
Bi(1),0.46821,0.02436,0.01883
Bi(2),0.22034,0.23870,0.71964
Ti(1),0.49128,0.49330,0.99697
Ti(2),0.25941,0.76040,0.75377
O(1),0.30771,0.62654,0.55680
O(2),0.79348,0.11688,0.06149
O(3),0.71201,0.62190,0.95715
O(4),0.17647,0.13538,0.44955
O(5),0.51184,0.81992,0.74272
O(6),0.99726,0.92673,0.25312
O',0.52092,0.87681,0.24008
FFEOF

# === solve block: IR_active_modes_Pna2_1.json ===
cat > /app/outputs/IR_active_modes_Pna2_1.json <<'FFEOF'
[
  {"representation": "A1", "frequency": 54, "I_Imax": 0.15, "epsilon_p": 23.4},
  {"representation": "A1", "frequency": 91, "I_Imax": 0.38, "epsilon_p": 33.7},
  {"representation": "A1", "frequency": 122, "I_Imax": 0.17, "epsilon_p": 11.5},
  {"representation": "A1", "frequency": 131, "I_Imax": 0.12, "epsilon_p": 7.6},
  {"representation": "A1", "frequency": 286, "I_Imax": 0.21, "epsilon_p": 5.7},
  {"representation": "A1", "frequency": 336, "I_Imax": 0.13, "epsilon_p": 3.2},
  {"representation": "A1", "frequency": 356, "I_Imax": 0.10, "epsilon_p": 2.2},
  {"representation": "B1", "frequency": 40, "I_Imax": 0.48, "epsilon_p": 96.7},
  {"representation": "B1", "frequency": 95, "I_Imax": 0.21, "epsilon_p": 18.0},
  {"representation": "B1", "frequency": 113, "I_Imax": 0.88, "epsilon_p": 62.9},
  {"representation": "B1", "frequency": 281, "I_Imax": 0.34, "epsilon_p": 9.8},
  {"representation": "B2", "frequency": 116, "I_Imax": 1.00, "epsilon_p": 69.4},
  {"representation": "B2", "frequency": 267, "I_Imax": 0.11, "epsilon_p": 3.4},
  {"representation": "B2", "frequency": 285, "I_Imax": 0.13, "epsilon_p": 3.6},
  {"representation": "B2", "frequency": 334, "I_Imax": 0.12, "epsilon_p": 2.9}
]
FFEOF
