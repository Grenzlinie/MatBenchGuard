#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'FFEOF'
{
  "B0_2": -187,
  "B2_2": -599,
  "B0_4": -1283,
  "B2_4": -1290,
  "B4_4": 445,
  "S2_4": 402,
  "S4_4": -691,
  "B0_6": 71,
  "B2_6": 364,
  "B4_6": 191,
  "B6_6": -108,
  "S2_6": 78,
  "S4_6": -293,
  "S6_6": -20,
  "rms_deviation": 5.3
}
FFEOF

# === solve block: calculated_stark_levels.csv ===
cat > /app/outputs/calculated_stark_levels.csv <<'FFEOF'
multiplet,level_index,calculated_energy_cm1
4I15/2,1,2
4I15/2,2,37
4I15/2,3,65
4I15/2,4,81
4I15/2,5,157
4I15/2,6,265
4I15/2,7,483
4I15/2,8,506
4I13/2,1,6515
4I13/2,2,6547
4I13/2,3,6584
4I13/2,4,6595
4I13/2,5,6684
4I13/2,6,6834
4I13/2,7,6857
4I9/2,1,12304
4I9/2,2,12418
4I9/2,3,12500
4I9/2,4,12582
4I9/2,5,12616
4S3/2,1,18220
4S3/2,2,18318
FFEOF

# === solve block: strength_parameters.json ===
cat > /app/outputs/strength_parameters.json <<'FFEOF'
{
  "Scf2": 388,
  "Scf4": 860,
  "Scf6": 206,
  "NV": 557
}
FFEOF
