#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: activation_energies.json ===
cat >"/app/outputs/activation_energies.json" <<'FFEOF'
{
  "N-N_NaGa_Ef": 0.94,
  "N-N_NaGa_Ed": 1.13,
  "C-C_NaGa_Ef": 0.51,
  "C-C_NaGa_Ed": 2.71,
  "C-H_CH_NaGa_Ef": 0.74,
  "C-H_CH_NaGa_Ed": 1.34,
  "C-H_CH4_Ga_Ef": 0.59,
  "C-H_CH4_Ga_Ed": 1.40
}
FFEOF
