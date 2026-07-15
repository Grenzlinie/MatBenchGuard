#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'EOF'
{
  "Mn2(CO)10_rt": {
    "IAM_O_O": -1.64,
    "IAM_O_C": -5.08,
    "IAM_C_C_rep": 4.37,
    "IAM_C_C_attr": -0.66,
    "IAM_M_O": -1.49,
    "IEM": -29.2
  },
  "Ir6(CO)16_black": {
    "molecules": [
      {
        "IAM_O_O": -2.50,
        "IAM_O_C": -7.44,
        "IAM_C_C_rep": 1.315,
        "IAM_C_C_attr": 0.0,
        "IEM": -21.15
      },
      {
        "IAM_O_O": -2.48,
        "IAM_O_C": -7.49,
        "IAM_C_C_rep": 1.315,
        "IAM_C_C_attr": 0.0,
        "IEM": -21.15
      }
    ]
  },
  "Ir6(CO)16_red": {
    "IAM_O_O": -2.69,
    "IAM_O_C": -8.46,
    "IAM_C_C": -0.11,
    "IEM": -39.1
  }
}
EOF
