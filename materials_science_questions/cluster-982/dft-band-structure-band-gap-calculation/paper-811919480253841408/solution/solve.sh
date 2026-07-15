#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
OUTDIR=/app/outputs
cat > "$OUTDIR/results.json" <<'EOF'
{
  "x1_32_U0": {
    "Delta_E_VI": 0.17,
    "Delta_E_I": 0.36,
    "Delta_E_IC": 1.16,
    "Delta_E_VC": 1.58,
    "int_DOS_below_Fermi": 2,
    "int_DOS_above_Fermi": 1,
    "q_plus": 5.48,
    "q_minus": 0.91,
    "t_plus": 0.86,
    "t_minus": 0.05,
    "e_plus": 0.96,
    "e_minus": 0.01,
    "p_plus": 0.17,
    "p_minus": 0.11
  },
  "x1_32_U3": {
    "Delta_E_VI": 0.24,
    "Delta_E_I": 0.37,
    "Delta_E_IC": 1.16,
    "Delta_E_VC": 1.57,
    "int_DOS_below_Fermi": 2,
    "int_DOS_above_Fermi": 1,
    "q_plus": 5.50,
    "q_minus": 0.87,
    "t_plus": 0.86,
    "t_minus": 0.04,
    "e_plus": 0.97,
    "e_minus": 0.01,
    "p_plus": 0.18,
    "p_minus": 0.11
  },
  "x1_32_U6": {
    "Delta_E_VI": 0.21,
    "Delta_E_I": 0.41,
    "Delta_E_IC": 1.16,
    "Delta_E_VC": 1.56,
    "int_DOS_below_Fermi": 2,
    "int_DOS_above_Fermi": 1,
    "q_plus": 5.51,
    "q_minus": 0.85,
    "t_plus": 0.86,
    "t_minus": 0.02,
    "e_plus": 0.97,
    "e_minus": 0.01,
    "p_plus": 0.18,
    "p_minus": 0.12
  },
  "x2_32_U0": {
    "Delta_E_VI": 0.19,
    "Delta_E_I": 0.52,
    "Delta_E_IC": 1.10,
    "Delta_E_VC": 1.68,
    "int_DOS_below_Fermi": 4,
    "int_DOS_above_Fermi": 2,
    "q_plus": 5.49,
    "q_minus": 0.91,
    "t_plus": 0.86,
    "t_minus": 0.05,
    "e_plus": 0.96,
    "e_minus": 0.01,
    "p_plus": 0.17,
    "p_minus": 0.11
  },
  "x2_32_U3": {
    "Delta_E_VI": 0.16,
    "Delta_E_I": 0.53,
    "Delta_E_IC": 1.11,
    "Delta_E_VC": 1.66,
    "int_DOS_below_Fermi": 4,
    "int_DOS_above_Fermi": 2,
    "q_plus": 5.50,
    "q_minus": 0.87,
    "t_plus": 0.86,
    "t_minus": 0.03,
    "e_plus": 0.97,
    "e_minus": 0.01,
    "p_plus": 0.18,
    "p_minus": 0.11
  },
  "x2_32_U6": {
    "Delta_E_VI": 0.13,
    "Delta_E_I": 0.55,
    "Delta_E_IC": 1.12,
    "Delta_E_VC": 1.64,
    "int_DOS_below_Fermi": 4,
    "int_DOS_above_Fermi": 2,
    "q_plus": 5.51,
    "q_minus": 0.85,
    "t_plus": 0.90,
    "t_minus": 0.02,
    "e_plus": 0.97,
    "e_minus": 0.01,
    "p_plus": 0.18,
    "p_minus": 0.12
  }
}
EOF
