#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple sympy

# === solve block: free_energy_polynomials.json ===
cat > $OUTDIR/free_energy_polynomials.json << 'FFEOF'
{
  "TaX2": {
    "order_parameter_dim": 6,
    "transformation_rules": [
      "S6_plus: psi_j -> psi_{j+1}^* (j mod 3)",
      "sigma_d: psi_1 -> psi_1, psi_2 -> psi_3, psi_3 -> psi_2"
    ],
    "polynomial_terms": [
      {"coefficient": "a/2", "monomial": "|psi_1|^2 + |psi_2|^2 + |psi_3|^2"},
      {"coefficient": "u1", "monomial": "|psi_1|^4 + |psi_2|^4 + |psi_3|^4"},
      {"coefficient": "u3", "monomial": "|psi_1|^2|psi_2|^2 + |psi_1|^2|psi_3|^2 + |psi_2|^2|psi_3|^2"}
    ],
    "invariant_constraints": [
      "u1 > 0",
      "u1 + u3 > 0"
    ]
  },
  "TiSe2": {
    "order_parameter_dim": 3,
    "transformation_rules": [
      "S6_plus: psi_j -> -psi_{j+1} (j mod 3)",
      "sigma_d: psi_1 -> -psi_1, psi_2 -> -psi_3, psi_3 -> -psi_2"
    ],
    "polynomial_terms": [
      {"coefficient": "a/2", "monomial": "psi_1^2 + psi_2^2 + psi_3^2"},
      {"coefficient": "u1", "monomial": "psi_1^4 + psi_2^4 + psi_3^4"},
      {"coefficient": "u3", "monomial": "psi_1^2 psi_2^2 + psi_1^2 psi_3^2 + psi_2^2 psi_3^2"}
    ],
    "invariant_constraints": [
      "u1 > 0",
      "u1 + u3 > 0"
    ]
  }
}
FFEOF

# === solve block: mean_field_states.json ===
cat > /app/outputs/mean_field_states.json << 'FFEOF'
{
  "TaX2": {
    "single_Q_condition": "u1 < u3/2",
    "triple_Q_condition": "u1 > u3/2",
    "order_parameter_components": [
      {
        "state": "(3Q)",
        "description": "All three components non-zero with equal amplitudes and arbitrary phases",
        "amplitude": "|psi_i|^2 = |a| / (4(u1 + u3)) for i=1,2,3"
      },
      {
        "state": "(1Q)",
        "description": "Single component non-zero, the other two zero",
        "amplitude_example": "|psi_1|^2 = |a| / (4 u1), |psi_2|^2 = |psi_3|^2 = 0"
      }
    ]
  },
  "TiSe2": {
    "single_Q_condition": "u1 < u3/2",
    "triple_Q_condition": "u1 > u3/2",
    "order_parameter_components": [
      {
        "state": "(3Q)",
        "description": "All three components real with equal squared amplitude; signs can be chosen independently",
        "amplitude": "psi_i^2 = |a| / (4(u1 + u3)) for i=1,2,3"
      },
      {
        "state": "(1Q)",
        "description": "Single component non-zero, the other two zero",
        "amplitude_example": "psi_1^2 = |a| / (4 u1), psi_2 = psi_3 = 0"
      }
    ]
  }
}
FFEOF

# === solve block: rg_fixed_points.json ===
python3 /solution/compute_rg.py > /app/outputs/rg_fixed_points.json
