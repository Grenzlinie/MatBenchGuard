#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ambient_raman_frequencies.csv ===
echo "mode,frequency_cm1" > /app/outputs/ambient_raman_frequencies.csv
echo "Ba A1g,105" >> /app/outputs/ambient_raman_frequencies.csv
echo "Ba Eg,130" >> /app/outputs/ambient_raman_frequencies.csv
echo "O(2) Eg,535" >> /app/outputs/ambient_raman_frequencies.csv
echo "O(2) A1g,583" >> /app/outputs/ambient_raman_frequencies.csv

# === solve block: pressure_raman_O_A_A1g.csv ===
cat > /app/outputs/pressure_raman_O_A_A1g.csv <<'FFEOF'
pressure_GPa,frequency_cm1
0.0,583
0.6,587
1.0,589.6667
2.0,596.3333
3.0,603.0
4.5,613.0
6.0,623.0
7.5,633.0
FFEOF
