#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: common_gb_composition.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_outputs import write_common_gb_composition; write_common_gb_composition('/app/outputs/common_gb_composition.csv')"

# === solve block: modelI_gb_energy.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_outputs import write_modelI_gb_energy; write_modelI_gb_energy('/app/outputs/modelI_gb_energy.csv')"

# === solve block: modelII_gb_energy.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_outputs import write_modelII_gb_energy; write_modelII_gb_energy('/app/outputs/modelII_gb_energy.csv')"

# === solve block: classical_two_phase_gb_energy.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_outputs import write_classical_two_phase_gb_energy; write_classical_two_phase_gb_energy('/app/outputs/classical_two_phase_gb_energy.csv')"

# === solve block: modelII_analytic_results.json ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_outputs import write_modelII_analytic_results; write_modelII_analytic_results('/app/outputs/modelII_analytic_results.json')"
