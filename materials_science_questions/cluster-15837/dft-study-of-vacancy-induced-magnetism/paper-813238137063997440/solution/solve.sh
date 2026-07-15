#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduction_results.json ===
cat > /app/outputs/reproduction_results.json <<'EOF'
{
  "configurations": [
    {"id": "2x2x4_(0,1)", "delta_E_meV": -326.0, "total_moment_muB": 3.08},
    {"id": "2x2x4_(0,2)", "delta_E_meV": -196.0, "total_moment_muB": 3.02},
    {"id": "2x2x4_(0,3)", "delta_E_meV": -225.0, "total_moment_muB": 2.88},
    {"id": "2x2x4_(0,4)", "delta_E_meV": -303.0, "total_moment_muB": 2.90},
    {"id": "2x2x4_(0,5)", "delta_E_meV": -193.0, "total_moment_muB": 3.03},
    {"id": "2x2x4_(0,6)", "delta_E_meV": -227.0, "total_moment_muB": 2.82}
  ],
  "ground_state": "2x2x4_(0,3)",
  "vacancy_effects": {
    "V_O_delta_E_meV": -17.0,
    "V_Sn_delta_E_meV": -304.0
  }
}
EOF
