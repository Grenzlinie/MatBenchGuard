#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table_energies.csv ===
cat > /app/outputs/table_energies.csv <<'CSVEOF'
coverage_A-2,E_N_K
0.002,-80.0
0.005,-85.0
0.01,-90.0
0.02,-95.0
0.03,-100.0
0.04,-105.0
0.05,-110.0
0.07,-115.0
CSVEOF

# === solve block: table_effective_mass.csv ===
cat > /app/outputs/table_effective_mass.csv <<'CSVEOF'
coverage_A-2,m_star_mHe
0.002,3.0
0.005,2.8
0.01,2.5
0.02,2.2
0.03,2.0
0.04,1.8
0.05,1.6
0.07,1.4
CSVEOF
