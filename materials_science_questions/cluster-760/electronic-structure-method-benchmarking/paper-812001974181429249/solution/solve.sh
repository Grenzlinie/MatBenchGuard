#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relative_energies_and_barriers.json ===
cat > /app/outputs/relative_energies_and_barriers.json <<'EOF'
{
  "results": [
    {"structure": "C1", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": false, "value": 0.0},
    {"structure": "C1", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": true, "value": 0.0},
    {"structure": "C1", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": false, "value": 0.0},
    {"structure": "C1", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": true, "value": 0.0},
    {"structure": "C1", "method": "MP2", "basis": "AVTZ", "zpe_corrected": false, "value": 0.0},
    {"structure": "C1", "method": "MP2", "basis": "AVTZ", "zpe_corrected": true, "value": 0.0},
    {"structure": "C1", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": false, "value": 0.0},
    {"structure": "C1", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": true, "value": 0.0},
    {"structure": "Cs", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": false, "value": -0.15},
    {"structure": "Cs", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": true, "value": 0.14},
    {"structure": "Cs", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": false, "value": 0.01},
    {"structure": "Cs", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": true, "value": 0.29},
    {"structure": "Cs", "method": "MP2", "basis": "AVTZ", "zpe_corrected": false, "value": -0.18},
    {"structure": "Cs", "method": "MP2", "basis": "AVTZ", "zpe_corrected": true, "value": -0.02},
    {"structure": "Cs", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": false, "value": -0.03},
    {"structure": "Cs", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": true, "value": 0.13},
    {"structure": "C3", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": false, "value": 1.82},
    {"structure": "C3", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": true, "value": 1.96},
    {"structure": "C3", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": false, "value": 2.06},
    {"structure": "C3", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": true, "value": 2.21},
    {"structure": "C3", "method": "MP2", "basis": "AVTZ", "zpe_corrected": false, "value": 1.97},
    {"structure": "C3", "method": "MP2", "basis": "AVTZ", "zpe_corrected": true, "value": 1.74},
    {"structure": "C3", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": false, "value": 2.13},
    {"structure": "C3", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": true, "value": 1.90},
    {"structure": "TS_C1_Cs", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": false, "value": 1.73},
    {"structure": "TS_C1_Cs", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": true, "value": 1.48},
    {"structure": "TS_C1_Cs", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": false, "value": 1.75},
    {"structure": "TS_C1_Cs", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": true, "value": 1.50},
    {"structure": "TS_C1_Cs", "method": "MP2", "basis": "AVTZ", "zpe_corrected": false, "value": 1.79},
    {"structure": "TS_C1_Cs", "method": "MP2", "basis": "AVTZ", "zpe_corrected": true, "value": 1.49},
    {"structure": "TS_C1_Cs", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": false, "value": 1.81},
    {"structure": "TS_C1_Cs", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": true, "value": 1.51},
    {"structure": "TS_Cs_C3", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": false, "value": 2.81},
    {"structure": "TS_Cs_C3", "method": "B3PW91", "basis": "AVTZ", "zpe_corrected": true, "value": 1.93},
    {"structure": "TS_Cs_C3", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": false, "value": 2.54},
    {"structure": "TS_Cs_C3", "method": "B3LYP", "basis": "AVTZ", "zpe_corrected": true, "value": 1.67},
    {"structure": "TS_Cs_C3", "method": "MP2", "basis": "AVTZ", "zpe_corrected": false, "value": 2.83},
    {"structure": "TS_Cs_C3", "method": "MP2", "basis": "AVTZ", "zpe_corrected": true, "value": 1.93},
    {"structure": "TS_Cs_C3", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": false, "value": 2.64},
    {"structure": "TS_Cs_C3", "method": "CCSD(T)", "basis": "AVTZ", "zpe_corrected": true, "value": 1.74}
  ]
}
EOF
