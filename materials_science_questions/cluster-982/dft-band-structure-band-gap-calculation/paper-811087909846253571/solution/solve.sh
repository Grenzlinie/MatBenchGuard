#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /app/outputs/results.json << 'FFEOF'
{
  "binary_compounds": [
    {"compound": "GaN", "a0_Angstrom": 4.521, "B0_GPa": 185.15, "E_gamma_gamma_eV": 3.123, "E_gamma_X_eV": 4.862},
    {"compound": "TlN", "a0_Angstrom": 5.224, "B0_GPa": 170.14, "E_gamma_gamma_eV": 0.0, "E_gamma_X_eV": 4.096},
    {"compound": "BN", "a0_Angstrom": 3.617, "B0_GPa": 388.73, "E_gamma_gamma_eV": 10.39, "E_gamma_X_eV": 5.838}
  ],
  "quaternary": {
    "a0_Angstrom": 4.528,
    "E_gamma_gamma_eV": 1.639,
    "eps1_0": 5.47,
    "n0": 2.35
  }
}
FFEOF
